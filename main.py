import random
import matplotlib.pyplot as plt
import numpy as np


def ativ1(contract="call", k=9):
    N = 2**k
    u = 2
    s0 = 4
    r = 0.25
    strike = 5
    p = 0.5

    if (contract == "call"):
        v_list = [max((s0*u**i-strike)/(1+r), 0) for i in range(N//2, -N//2 - 1, -1)]
    else:
        v_list = [max((strike-s0*u**i)/(1+r), 0) for i in range(N//2, -N//2 - 1, -1)]
    
    # for i in range(N//2, -N//2 - 1, -1):
        # print ((k-s0*u**i)/(1+r))
        # print(s0, u**i, 1+r)
    # raise Exception

    while len(v_list) > 1:
        vm1_list = [v_list[j]*p + v_list[j+1]*(1-p) for j in range(len(v_list)-1)]
        v_list = vm1_list[:]

    return v_list[0]


def ativ2(contract="call", M=5000, k=9):
    N = 2**k
    u = 2
    s0 = 4
    r = 0.25
    strike = 5
    p = 0.5
    v0 = 0

    if (contract == "call"):
        for m in range(M):
            v0 = (v0*m + ativ1("call", i))/(m+1)
    else:
        for m in range(M):
            v0 = (v0*m + ativ1("put", i))/(m+1)

    return v0


def ativ3(M=5000, k=9):
    return



if __name__ == "__main__":
    # # with open("ativ1_put.txt", "w") as filename:
    # with open("ativ1_call.txt", "w") as filename:
    #     for i in range(1, 13):
    #         # filename.write(str(i) + " -> " + str(ativ1("put",i)) + "\n")
    #         filename.write(str(i) + " -> " + str(ativ1("call",i)) + "\n")

    with open("ativ2.txt", "w") as filename:
        for i in range(1, 13):
            filename.write(str(i) + " -> " + str(ativ2("call", M=5000, k=i)) + " CALL\n")
            filename.write(str(i) + " -> " + str(ativ2("put", M=5000, k=i)) + " PUT\n")