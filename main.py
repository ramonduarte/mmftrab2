import random
import matplotlib.pyplot as plt
import numpy as np

## TODO: generate stocks final values 2019-06-04 22:11:51
## TODO: generate intermediate values for each n-1 2019-06-04 22:12:26
## TODO: get to v0


def alg(k=9):
    N = 2**k
    u = 2
    s0 = 4
    r = 0.25
    strike = 5
    p = 0.5

    v_list = [s0*u**i for i in range(N//2, -N//2 - 1, -1)]

    while len(v_list) > 1:
        vm1_list = [v_list[j]*p + v_list[j+1] for j in range(len(v_list)-1)]
        v_list = vm1_list[:]

    return v_list[0]


if __name__ == "__main__":
    with open("filename.txt", "w") as filename:
        for i in range(1, 13):
            filename.write(str(i) + " -> " + str(alg(i)) + "\n")
