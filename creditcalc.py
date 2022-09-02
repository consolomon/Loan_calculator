# write your code here

from math import ceil
from math import log
from math import pow
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--type", choices=["annuity", "diff"], help="Incorrect parameters")
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")

args = parser.parse_args()
is_incorrect = False

if args.interest is None or float(args.interest) < 0:
    is_incorrect = True
if args.type == "diff" and args.payment is not None:
    is_incorrect = True
elif args.type == "diff" and (args.principal is None or args.periods is None or args.interest is None):
    is_incorrect = True
elif args.type == "diff" and (int(args.principal) < 0 or int(args.periods) < 0 or float(args.interest) < 0):
    is_incorrect = True
if args.type == "annuity":
    if args.payment is not None:
        if int(args.payment) < 0 or (args.principal is None and args.periods is None):
            is_incorrect = True
    if args.principal is not None:
        if int(args.principal) < 0 or (args.payment is None and args.periods is None):
            is_incorrect = True
    if args.periods is not None:
        if int(args.periods) < 0 or (args.payment is None and args.principal is None):
            is_incorrect = True

if is_incorrect:
    print("Incorrect parameters")
else:
    if args.type == "annuity":
        if args.principal is not None and args.payment is not None:
            principal = int(args.principal)
            payment = int(args.payment)
            interest = float(args.interest)
            interest = interest / 1200

            m_num = ceil(log(payment / (payment - interest * principal), 1 + interest))
            overpayment = payment * m_num - principal
            y_num = m_num // 12
            m_num -= y_num * 12

            if y_num == 0:
                print("It will take", m_num, "months" if m_num > 1 else "month", " to repay this loan!")
            elif m_num == 0:
                print("It will take", y_num, "years" if y_num > 1 else "year", " to repay this loan!")
            else:
                print("It will take", y_num, "year", "s" if y_num > 1 else "", "and",
                      m_num, "month", "s" if m_num > 1 else "", "to repay this loan!")
            if overpayment > 0:
                print("Overpayment =", overpayment)

        elif args.principal is not None and args.periods is not None:
            principal = int(args.principal)
            per_num = int(args.periods)
            interest = float(args.interest)
            interest = interest / 1200
            annuity = ceil(principal * interest * pow(1 + interest, per_num) / (pow(1 + interest, per_num) - 1))
            print("Your monthly payment =", annuity, "!")

        elif args.payment is not None and args.periods is not None:
            annuity = float(args.payment)
            per_num = int(args.periods)
            interest = float(args.interest)
            interest = interest / 1200
            principal = ceil(annuity * (pow(1 + interest, per_num) - 1) / (interest * pow(1 + interest, per_num)))
            print("Your loan principal =", principal, "!")

    elif args.type == "diff":
        principal = int(args.principal)
        per_num = int(args.periods)
        interest = float(args.interest)
        interest = interest / 1200
        overpayment = 0
        for i in range(1, per_num + 1):
            diff_payment = ceil((principal / per_num) + interest * (principal - (principal * (i - 1) / per_num)))
            overpayment += diff_payment
            print("Month", i, ": payment is", diff_payment)
        overpayment -= principal
        if overpayment > 0:
            print("Overpayment =", overpayment)
