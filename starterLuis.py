from matplotlib import pyplot as plt
import numpy as np
# import pandas as pd
import math
# from scipy import stats





# 1st stability region
a = .23
q = .7						# another default constant
h = 15 						# constant dependent on stability region- 1st: 10-20, 2nd:.73-1.43
# 2nd stability region
# a = 3.16
# q = 3.23
# h = 1 						# constant dependent on stability region- 1st: 10-20, 2nd:.73-1.43

ez = 5 * 1.60218*10**-19	# making assumption of 5 electron volts & convert to joules
# m = 4.981* 10**-25		# 300 amu
# m = 1.66054 * 10**-25		# 100 amu
m = 6.64216*10**-26			# 40amu
# m = 1.82659 * 10**-27		# 1.1 amu
# m = 1.66054* 10**-27		# 1 amu
e = 1.60217662*10**-19
vz = 2*(ez/m)**(1/2)		# axial ion velocity
resolutions = list()
voltages = list()
frequencies = list()
lengths = list()


# in Hz and meters
def evaluate(frequency, L, r0, m, e, ez, vz, h, q, a):
	resolution = 1/h*(frequency*(L/vz))**2
	print("resolution: ", resolution)
	# delta_m = 2*h*ez/(frequency**2*L**2)
	# m = resolution*delta_m
	driving_voltage = (math.pi)**2*q*m/e*frequency**2*r0**2
	print("driving_voltage: ", driving_voltage)



	for frequency in range(500000, 4000000, 250000):
		# for L in range(2,9):
		frequencies.append(frequency)
		lengths.append(L)
		resolution = 1/h*(frequency*(L/vz))**2
		resolutions.append(resolution)

		delta_m = 2*h*ez/(frequency**2*L**2)
		m = resolution*delta_m
		e = 1.60217662*10**-19

		driving_voltage = (math.pi)**2*q*m/e*frequency**2*r0**2
		voltages.append(driving_voltage)

	plt.plot(frequencies, voltages, "red")
	plt.xlabel("frequency")
	plt.ylabel("voltage")
	plt.figure()
	plt.plot(frequencies, resolutions, "blue")
	plt.xlabel("frequencies")
	plt.ylabel("resolution")
	plt.figure()
	plt.plot(lengths, resolutions, "blue")
	plt.xlabel("quadrupole length")
	plt.ylabel("resolutions")
	# plt.figure()
	# plt.plot(lengths, frequencies, "red")
	# plt.xlabel("quadrupole length")
	# plt.ylabel("frequency")
	plt.show()


# evaluate(frequency= 2650000, L = .08, r0 = .002, m = m, e=e, ez=ez, vz=vz, h=h, q=q, a=a)
evaluate(frequency= 1440000, L = .08, r0 = .002, m = m, e=e, ez=ez, vz=vz, h=h, q=q, a=a)











