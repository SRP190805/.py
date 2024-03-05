import math as m
import random as r
def genrate_otp(lengtH):
    otp = ''
    for i in range(lengtH-2):
        otp += str(m.floor(r.randint(0,10) * 10))
    return otp

print(genrate_otp(6))