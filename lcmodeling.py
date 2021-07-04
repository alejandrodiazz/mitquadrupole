from matplotlib import pyplot as plt
import numpy as np
import math


# a lower inductance and/or capacitance means a higher frequency can be achieved/used for resonance
L = 100 * 10**-6 	# measured in henries
C = 600 * 10**-12
frequency = 1 / (2*math.pi*math.sqrt(L*C))

print(frequency)

# plt.plot(frequencies, voltages, "red")
# plt.xlabel("frequency")
# plt.ylabel("voltage")
# plt.figure()
# plt.plot(frequencies, resolutions, "blue")
# plt.xlabel("frequencies")
# plt.ylabel("resolution")
# plt.show()













