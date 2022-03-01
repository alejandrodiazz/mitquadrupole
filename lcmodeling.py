from matplotlib import pyplot as plt
import numpy as np
import math


e0 = 8.854*10**-12	# permitivity of space
k = 1 				# relative permitivity of air

A = .12 * .00346/2  	# 12 cm * 3.46mm area of rods
d = .000379 		# .379mm of separation between +- rods

# A = .04 * .0045/2  	# 4 cm * 3.46mm area of rods in dlp paper
# d = .000721 		# .733mm of separation between +- rods in dlp paper

# A = .09 * .000600/2  	# JMEMS paper
# d = .0001 		# 


capacitance_of_one_rod = k*e0*A/d
print()
print("Capacitance of one rod: ", capacitance_of_one_rod)
print("Total Capacitance: ", capacitance_of_one_rod*2)
print("Actual Likely Total Capacitance: ", capacitance_of_one_rod*10)
actual_capacitance = capacitance_of_one_rod*10


# a lower inductance and/or capacitance means a higher frequency can be achieved/used for resonance
relative_permeability_of_core = 1
n2 = 2			# number of turns
diameter = .0273	# It is recommended that the coil diameter is 50% to 80% coil length for optimum Q and those are dependant on how much space can the coil take up. 
radius = diameter/2	# 
l = .05			# length of winding
L = relative_permeability_of_core * ( n2**2 * math.pi**2 * radius**2 / l ) * 0.00000126
print("inductance1: ", L)



# a lower inductance and/or capacitance means a higher frequency can be achieved/used for resonance
relative_permeability_of_core = 1
n2 = 40			# number of turns
diameter = .0273	# It is recommended that the coil diameter is 50% to 80% coil length for optimum Q and those are dependant on how much space can the coil take up. 
radius = diameter/2	# 
l = .05			# length of winding
L = relative_permeability_of_core * ( n2**2 * math.pi**2 * radius**2 / l ) * 0.00000126
print("inductance2: ", L)
# L = 25 * 10**-6 			# measured in henries
C = actual_capacitance 	# probably around 50pF

# 18 gauge Wire perhaps? 0.106172 cm diameter
ohms_per_kilometer = 13.2
ohms_per_meter = ohms_per_kilometer/1000
meters_of_wire = n2*(2*math.pi*radius)
print("meters_of_wire1: ", meters_of_wire)
print("inductor_resistance:1", ohms_per_meter*meters_of_wire)




# # a lower inductance and/or capacitance means a higher frequency can be achieved/used for resonance
# relative_permeability_of_core = 1
# n2 = 4			# number of turns
# diameter = .08	# It is recommended that the coil diameter is 50% to 80% coil length for optimum Q and those are dependant on how much space can the coil take up. 
# radius = diameter/2	# 
# l = .0045			# length of winding
# L = relative_permeability_of_core * ( n2**2 * math.pi**2 * radius**2 / l ) * 0.00000126
# print("inductance2: ", L)
# # L = 25 * 10**-6 			# measured in henries
# C = actual_capacitance 	# probably around 50pF

# # 18 gauge Wire perhaps? 0.106172 cm diameter
# ohms_per_kilometer = 13.2
# ohms_per_meter = ohms_per_kilometer/1000
# meters_of_wire = n2*(2*math.pi*radius)
# print("meters_of_wire2: ", meters_of_wire)
# print("inductor_resistance2: ", ohms_per_meter*meters_of_wire)





Rs = ohms_per_meter*meters_of_wire 			# resistive value of inductor in ohms
frequency = 1 / (2*math.pi) * math.sqrt(1/(L*C)-(Rs/L)**2)
# frequency = 1 / (2*math.pi * math.sqrt(L*C))
print("Frequency: ", frequency)

cap_reactance = 1/ (2*math.pi*frequency*capacitance_of_one_rod)
inductive_reactance = 1/ (2*math.pi*frequency*L)
q = inductive_reactance/Rs
print("Cap reactance (in ohms)", cap_reactance)
print("Q: ", q)

current_to_drive = 200/cap_reactance
print("Current_to_drive: ", current_to_drive)

print("Current_to_drive both rods: ", current_to_drive*2, "A")
# plt.plot(frequencies, voltages, "red")
# plt.xlabel("frequency")
# plt.ylabel("voltage")
# plt.figure()
# plt.plot(frequencies, resolutions, "blue")
# plt.xlabel("frequencies")
# plt.ylabel("resolution")
# plt.show()



print()
phi = 1.148 		# aspect ration from r to r0
epsilon = 8.85418782 * 10**-12
k = 25
D = .004
capacitance_from_2018_paper = (8*(2*phi+1)*math.sqrt(phi**2+phi))*epsilon*k*D
print("capacitance_from_2018_paper: ", capacitance_from_2018_paper)
cap_reactance = 1/ (2*math.pi*frequency*capacitance_from_2018_paper)
print("corresponding_reactance: ", cap_reactance)
current_to_drive = 200/cap_reactance
print("Current_to_drive: ", current_to_drive)
print("Current_to_drive: ", 2*math.pi*frequency*capacitance_from_2018_paper*200)
resistance = 100000
print("Current_to_drive with resistance: ", 200/(math.sqrt(cap_reactance**2+resistance**2)))

print()














