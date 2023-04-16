from decimal import *


class LessThanZeroException(Exception):
    "Raised when the input value is less than 0"
    pass


def print_row(name, val1, val2, val3):
    print("%-45s %18s %18s %18s" % (name, val1, val2, val3))


basicA = Decimal("132000")
# Basic Allowance
mpA = Decimal("264000")
# Married Person's Allowance


def intro():
    print("\nSimple HK Salaries Tax Calculator")
    print("For year of assessment 2022/23")
    print("The purpose of this program is to determine mandotory MPF contributions, as well as salaries tax to be paid under seperate or joint assessment")


def brk():
    print()
    print("======================================================================================================")
    print()


def input1():
    # take input from the user
    while True:
        try:
            inc1 = Decimal(input("Enter annual income for person 1: "))
            # Annual Income for Person 1
            if inc1 < Decimal("0"):
                raise LessThanZeroException
        except InvalidOperation:
            print("Invalid input. Please enter a valid number.")
            continue
        except LessThanZeroException:
            print("Invalid input. Income cannot be less than 0.")
            continue
        break

    return inc1


def input2():
    # take input from the user
    while True:
        try:
            inc2 = Decimal(input("Enter annual income for person 2: "))
            # Annual Income for Person 2
            if inc2 < Decimal("0"):
                raise LessThanZeroException
        except InvalidOperation:
            print("Invalid input. Please enter a valid number.")
            continue
        except LessThanZeroException:
            print("Invalid input. Income cannot be less than 0.")
            continue
        break

    return inc2


def main(inc1, inc2):
    minc1 = inc1/Decimal("12")
    # Monthly Income for Person 1
    minc2 = inc2/Decimal("12")
    # Monthly Income for Person 2

    if minc1 < Decimal("7100"):
        mmpf1 = Decimal("0")
    elif minc1 >= Decimal("7100") and minc1 <= Decimal("30000"):
        mmpf1 = minc1*Decimal("0.05")
    elif minc1 > Decimal("30000"):
        mmpf1 = Decimal("1500")

    mpf1 = mmpf1*Decimal("12")
    # mmpf1 = Person 1 Monthly Mandotory MPF Contributions
    # mpf1 = Person 1 Yearly Mandatory MPF Contributions

    if minc2 < Decimal("7100"):
        mmpf2 = Decimal("0")
    elif minc2 >= Decimal("7100") and minc2 <= Decimal("30000"):
        mmpf2 = minc2*Decimal("0.05")
    elif minc2 > Decimal("30000"):
        mmpf2 = Decimal("1500")

    mpf2 = mmpf2*Decimal("12")
    # mmpf2 = Person 2 Monthly Mandotory MPF Contributions
    # mpf2 = Person 2 Yearly Mandatory MPF Contributions

    jinc = inc1+inc2
    # Joint Total Annual Income
    jmpf = mpf1+mpf2
    # Joint Total Annual Mandotory MPF Contributions

    cinc1 = inc1 - mpf1 - basicA
    if cinc1 < Decimal("0"):
        cinc1 = Decimal("0")
    # Person 1 Annual Chargeable Income

    cinc2 = inc2 - mpf2 - basicA
    if cinc2 < Decimal("0"):
        cinc2 = Decimal("0")
    # Person 2 Annual Chargeable Income

    cjinc = jinc - jmpf - mpA
    if cjinc < Decimal("0"):
        cjinc = Decimal("0")
    # Joint Annual Chargeable Income

    if cinc1 <= Decimal("0"):
        tax1 = Decimal("0")
    elif cinc1 > Decimal("0") and cinc1 <= Decimal("50000"):
        tax1 = cinc1*Decimal("0.02")
    elif cinc1 > Decimal("50000") and cinc1 <= Decimal("100000"):
        tax1 = Decimal("1000")+(cinc1-Decimal("50000"))*Decimal("0.06")
    elif cinc1 > Decimal("100000") and cinc1 <= Decimal("150000"):
        tax1 = Decimal("4000")+(cinc1-Decimal("100000"))*Decimal("0.1")
    elif cinc1 > Decimal("150000") and cinc1 <= Decimal("200000"):
        tax1 = Decimal("9000")+(cinc1-Decimal("150000"))*Decimal("0.14")
    elif cinc1 > Decimal("200000"):
        tax1 = Decimal("16000")+(cinc1-Decimal("200000"))*Decimal("0.17")
    # Person 1 Tax Payable

    if cinc2 <= Decimal("0"):
        tax2 = Decimal("0")
    elif cinc2 > Decimal("0") and cinc2 <= Decimal("50000"):
        tax2 = cinc2*Decimal("0.02")
    elif cinc2 > Decimal("50000") and cinc2 <= Decimal("100000"):
        tax2 = Decimal("1000")+(cinc2-Decimal("50000"))*Decimal("0.06")
    elif cinc2 > Decimal("100000") and cinc2 <= Decimal("150000"):
        tax2 = Decimal("4000")+(cinc2-Decimal("100000"))*Decimal("0.1")
    elif cinc2 > Decimal("150000") and cinc2 <= Decimal("200000"):
        tax2 = Decimal("9000")+(cinc2-Decimal("150000"))*Decimal("0.14")
    elif cinc2 > Decimal("200000"):
        tax2 = Decimal("16000")+(cinc2-Decimal("200000"))*Decimal("0.17")
    # Person 2 Tax Payable

    if cjinc <= Decimal("0"):
        jtax = Decimal("0")
    elif cjinc > Decimal("0") and cjinc <= Decimal("50000"):
        jtax = cjinc*Decimal("0.02")
    elif cjinc > Decimal("50000") and cjinc <= Decimal("100000"):
        jtax = Decimal("1000")+(cjinc-Decimal("50000"))*Decimal("0.06")
    elif cjinc > Decimal("100000") and cjinc <= Decimal("150000"):
        jtax = Decimal("4000")+(cjinc-Decimal("100000"))*Decimal("0.1")
    elif cjinc > Decimal("150000") and cjinc <= Decimal("200000"):
        jtax = Decimal("9000")+(cjinc-Decimal("150000"))*Decimal("0.14")
    elif cjinc > Decimal("200000"):
        jtax = Decimal("16000")+(cjinc-Decimal("200000"))*Decimal("0.17")
    # Joint Tax Payable

    stax1 = (inc1-mpf1)*Decimal("0.15")
    stax2 = (inc2-mpf2)*Decimal("0.15")
    sjtax = (jinc-jmpf)*Decimal("0.15")

    if stax1 < tax1:
        tax1 = stax1
    if stax2 < tax2:
        tax2 = stax2
    if sjtax < jtax:
        jtax = sjtax

    btax = tax1 + tax2
    # Person 1 + Person 2 Tax Payable

    print()
    print_row("", "Person 1", "Person 2", "Joint Assessment")
    print_row("Total Income:", round(inc1, 2), round(inc2, 2), round(jinc, 2))
    print_row("Deduction (MPF):", round(mpf1, 2),
              round(mpf2, 2), round(jmpf, 2))
    print_row("Basic/Married Person's Allowances:",
              round(basicA, 2), round(basicA, 2), round(mpA, 2))
    print_row("Net Chargeable Income:", round(
        cinc1, 2), round(cinc2, 2), round(cjinc, 2))
    print_row("Tax Payable:", round(
        tax1, 2), round(tax2, 2), round(jtax, 2))
    print("%-45s %27s %28s" % ("Total Tax Payable By Both:",
          round(btax, 2), round(jtax, 2)))
    print()
    if btax > jtax:
        print("As seen from above calculations, a Joint Assessment will result in tax savings amounting to $"+str(round((btax-jtax), 2)
                                                                                                                  )+" ($"+str(round(btax, 2))+" - $"+str(round(jtax, 2))+"), and as such a Joint Assessment is recommended.")
    elif btax < jtax:
        print("As seen from above calculations, Individual Assessments will result in tax savings amounting to $"+str(round((jtax-btax), 2)
                                                                                                                      )+" ($"+str(round(jtax, 2))+" - $"+str(round(btax, 2))+"), and as such Individual Assessments are recommended.")
    elif btax == jtax:
        print("As seen from above calculations, there are no savings between a Joint Assessment or Individual Assessments ($" +
              str(round(btax, 2))+" = $"+str(round(jtax, 2))+"), and as such either assessment methods can be used.")

    # check if user wants another calculation
    next_calc = input(
        '\nType "exit" to end program, otherwise type anything to restart: ')
    return next_calc, mpf1, mpf2, jtax, btax


if __name__ == "__main__":
    intro()
    while True:
        brk()
        next_calc, mpf1, mpf2, jtax, btax = main(input1(), input2())
        if next_calc == "exit":
            break
