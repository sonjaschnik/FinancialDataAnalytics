import math
import matplotlib

def present_value_calculation(C, r, t):
    """
    present_value_calculation: to calculate the present value of a future cash flow
    C: cash flow at time t
    r: interest rate
    t: time
    PV: present value of C at time t
    """
    PV = C/((1+r)**t)

    return PV

C_ten = 100
r_ten = 0.03
t_ten = 10  

PV_ten = present_value_calculation(C_ten, r_ten, t_ten)

print(PV_ten)

  





