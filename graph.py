import random
import matplotlib.pyplot as plt
import numpy as np
from itertools import zip_longest


call = []
with open("ativ1_call.txt") as fil:
    call = fil.readlines()

call = [i.split(" -> ") for i in call]
call = [[int(a[0]), float(a[1])] for a in call]
call = list(map(list, zip_longest(*call)))

put = []
with open("ativ1_put.txt") as fil:
    put = fil.readlines()

put = [i.split(" -> ") for i in put]
put = [[int(a[0]), float(a[1])] for a in put]
put = list(map(list, zip_longest(*put)))


plt.plot(put[0], put[1], 'bo')
plt.xlabel(r'$k = log_{2} N$')
plt.ylabel(r"Contract value at start ($V_{0}$)")
plt.title('European PUT option')
plt.show()

plt.plot(call[0], call[1], 'ro')
plt.yscale('log')
plt.xlabel(r'$k = log_{2} N$')
plt.ylabel(r"Contract value at start ($log_{10} V_{0}$)")
plt.title('European CALL option')
plt.show()


call2 = []
with open("ativ2_call.txt") as fil:
    call2 = fil.readlines()

call2 = [i.split(" -> ") for i in call2]
call2 = [[int(a[0]), float(a[1])] for a in call2]
call2 = list(map(list, zip_longest(*call2)))

put2 = []
with open("ativ2_put.txt") as fil:
    put2 = fil.readlines()

put2 = [i.split(" -> ") for i in put2]
put2 = [[int(a[0]), float(a[1])] for a in put2]
put2 = list(map(list, zip_longest(*put2)))

# raise Exception
y = [(put[1][i] - put2[1][i])**2 for i in range(len(put[1])) ]
plt.plot(put[0], y, 'bo')
plt.xlabel(r'$k = log_{2} N$')
plt.ylabel(r"Montecarlo simulation's mean square error")
plt.title('Montecarlo simulation of an European PUT option')
plt.show()

y = [(call[1][i] - call2[1][i])**2 for i in range(len(call[1])) ]
plt.plot(call[0], y, 'ro')
plt.yscale('log')
plt.xlabel(r'$k = log_{2} N$')
plt.ylabel(r"Montecarlo simulation's mean square error")
plt.title('Montecarlo simulation of an European CALL option')
plt.show()


call3 = []
with open("ativ3.txt") as fil:
    call3 = fil.readlines()

call3 = [i.split(" -> ") for i in call3]
call3 = [[int(a[0]), float(a[1])] for a in call3]
call3 = list(map(list, zip_longest(*call3)))

plt.plot(call3[0], call3[1], 'ro')
plt.yscale('log')
plt.xlabel(r'$k = log_{2} N$')
plt.ylabel(r"Contract value at start ($log_{10} V_{0}$)")
plt.title('Montecarlo simulation of an European CALL lookback option')
plt.show()
