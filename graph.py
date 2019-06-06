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
plt.title('American PUT option')
plt.show()

plt.plot(call[0], call[1], 'ro')
plt.yscale('log')
plt.xlabel(r'$k = log_{2} N$')
plt.ylabel(r"Contract value at start ($log_{10} V_{0}$)")
plt.title('American CALL option')
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
plt.plot(put[0], [(i - j)**2 for i in put[1] for j in put2[1]], 'bo')
plt.xlabel(r'$k = log_{2} N$')
plt.ylabel(r"Montecarlo simulation's mean square error")
plt.title('American PUT option')
plt.show()

plt.plot([(i[0] - j[0])**2 for i in call for j in call2], call[1],'ro')
plt.yscale('log')
plt.xlabel(r'$k = log_{2} N$')
plt.ylabel(r"Montecarlo simulation's mean square error")
plt.title('American CALL option')
plt.show()


