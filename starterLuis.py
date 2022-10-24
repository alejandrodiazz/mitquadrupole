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


# in kilograms
# m = 4.981* 10**-25		# 300 amu
m_100 = 1.66054 * 10**-25		# 100 amu
m_argon40 = 6.64216*10**-26		# 39.948amu argon
m_carbon12 = 1.99447*10**-26	# 12.011 amu carbon
m_1_1 = 1.82659 * 10**-27		# 1.1 amu
m_hydrogen1 = 1.66054* 10**-27		# 1.00784 amu




resolutions = list()
voltages = list()
frequencies = list()
lengths = list()


# in Hz and meters
def evaluate(frequency, L, r0, m, h, q, a):

	ez = 5 * 1.60218*10**-19	# making assumption of 5 electron volts & convert to joules
	e = 1.60217662*10**-19
	vz = 2*(ez/m)**(1/2)		# axial ion velocity


	resolution = 1/h*(frequency*(L/vz))**2
	print("resolution: ", resolution)
	# delta_m = 2*h*ez/(frequency**2*L**2)
	# m = resolution*delta_m
	rf_voltage = (math.pi)**2*q*m/e*frequency**2*r0**2
	print("rf_voltage: ", rf_voltage)
	dc_voltage = math.pi**2*a*frequency**2*m*r0**2/(2*e)
	print("dc_voltage: ", dc_voltage)



	for frequency in range(500000, 4000000, 250000):
		# for L in range(2,9):
		frequencies.append(frequency)
		lengths.append(L)
		resolution = 1/h*(frequency*(L/vz))**2
		resolutions.append(resolution)

		delta_m = 2*h*ez/(frequency**2*L**2)
		m = resolution*delta_m
		e = 1.60217662*10**-19

		rf_voltage = (math.pi)**2*q*m/e*frequency**2*r0**2
		voltages.append(rf_voltage)

	print()
	# plt.plot(frequencies, voltages, "red")
	# plt.xlabel("frequency")
	# plt.ylabel("voltage")
	# plt.figure()
	# plt.plot(frequencies, resolutions, "blue")
	# plt.xlabel("frequencies")
	# plt.ylabel("resolution")
	# plt.figure()
	# plt.plot(lengths, resolutions, "blue")
	# plt.xlabel("quadrupole length")
	# plt.ylabel("resolutions")
	# # plt.figure()
	# # plt.plot(lengths, frequencies, "red")
	# # plt.xlabel("quadrupole length")
	# # plt.ylabel("frequency")
	# plt.show()

print()
# evaluate(frequency= 2650000, L = .1, r0 = .002, m = m, e=e, ez=ez, vz=vz, h=h, q=q, a=a) # original
# evaluate(frequency= 2650000, L = .1, r0 = .00175, m = m, e=e, ez=ez, vz=vz, h=h, q=q, a=a) # radius -s equal to 2.25mm
# evaluate(frequency= 2650000, L = .1, r0 = .002, m = m, e=e, ez=ez, vz=vz, h=h, q=q, a=a) # radius -s equal to 2.25mm
# evaluate(frequency= 2650000, L = .1, r0 = .002, m = m, e=e, ez=ez, vz=vz, h=h, q=q, a=a) # radius -s equal to 2.25mm
# evaluate(frequency= 1440000, L = .08, r0 = .002, m = m, e=e, ez=ez, vz=vz, h=h, q=q, a=a)
# evaluate(frequency= 930000, L = .0484, r0 = .002, m = m, e=e, ez=ez, vz=vz, h=h, q=q, a=a) # original

# evaluate(frequency= 930000, L = .0484, r0 = .002, m = 1.14577*10**-25, e=e, ez=ez, vz=vz, h=h, q=q, a=a) # fc-43 69 amu
# evaluate(frequency= 930000, L = .0484, r0 = .002, m = 2.1753*10**-25, e=e, ez=ez, vz=vz, h=h, q=q, a=a) # fc-43 131 amu
# evaluate(frequency= 930000, L = .0484, r0 = .002, m = 3.6366*10**-25,  e=e, ez=ez, vz=vz, h=h, q=q, a=a) # fc-43 219 amu 
# evaluate(frequency= 930000, L = .0484, r0 = .002, m = 4.3838*10**-25,  e=e, ez=ez, vz=vz, h=h, q=q, a=a) # fc-43 264 amu
# evaluate(frequency= 930000, L = .0484, r0 = .002, m = 6.6421*10**-26,  e=e, ez=ez, vz=vz, h=h, q=q, a=a) # fc-43 40 amu argon

# evaluate(frequency= 1780000, L = .0734, r0 = .002, m = m_hydrogen1, h=h, q=q, a=a)
# evaluate(frequency= 1780000, L = .0734, r0 = .002, m = m_1_1, h=h, q=q, a=a)  
# evaluate(frequency= 1780000, L = .0734, r0 = .002, m = m_carbon12, h=h, q=q, a=a)
# evaluate(frequency= 1780000, L = .0734, r0 = .002, m = m_argon40, h=h, q=q, a=a) 
evaluate(frequency= 2200000, L = .0734, r0 = .002, m = m_100, h=h, q=q, a=a)


# evaluate(frequency= 2650000, L = .1, r0 = .002, m = m_100, h=h, q=q, a=a)










