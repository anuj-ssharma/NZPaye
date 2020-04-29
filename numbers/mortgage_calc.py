"""
Mortgage Calculator - Calculate the monthly payments of a fixed term mortgage over given Nth terms at a given interest rate.
Also figure out how long it will take the user to pay back the loan.
For added complexity, add an option for users to select the compounding interval (Monthly, Weekly, Daily, Continually).

Loan Amortisation

Capital Recovery factor helps in the preparation of a loan amortisation schedule aka loan repayment schedule
Capital Recovery is the annuity of an investment made today, for a specified period of time, at a given rate of interest.
A = P X (1/PVFA(n, i))
A = P x CRF

CRF = 1/((1/i) - (1/i(1+i)^n))
"""

import math
from tabulate import tabulate


P = 360000
n = 2
interest_rate = 3.75
# annually = 1
# monthly = 12
# fortnightly = 24
# weekly = 52
time_factor = 12

eir = (interest_rate/time_factor)/100

A = 1/eir
B = 1/(eir * (math.pow(1+eir, n*time_factor)))
CRF = 1/(A-B)
regular_payments = (P * CRF)

outstanding_principal = P
total_interest = 0
lump_sum_payment = 0
monthly_summary = []
for month in range(0, n * time_factor + 1):
    if(outstanding_principal < 0):
        break
    interest_charges = outstanding_principal * eir
    total_interest = total_interest + interest_charges
    if(interest_charges > regular_payments):
        principal_repayment = interest_charges - regular_payments
    else:
        principal_repayment = regular_payments - interest_charges
    if(regular_payments > outstanding_principal):
        principal_repayment = outstanding_principal
    outstanding_principal = outstanding_principal - principal_repayment
    outstanding_principal = outstanding_principal - lump_sum_payment
    monthly_summary.append([month, format(regular_payments, '.0f'), format(interest_charges, '.0f'), format(principal_repayment, '.0f'), format(outstanding_principal, '.0f')])

print(tabulate(monthly_summary, headers= ["End of month", "Payment", "Interest", "Principal Repayment", "Outstanding Balance"]))
print()
print("Total interest paid will be : $" + format(total_interest, '.0f'))