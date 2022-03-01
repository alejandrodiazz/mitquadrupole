# Making Square Waves

frequency = 2650000
offset = .00000002 # 5 nanoseconds

# 1st sine wave
tdelay = offset
Tperiod  = 1/2650000
Ton = Tperiod/2 - 2*offset
print("period: ", Tperiod)
print("tdelay: ", tdelay)
print("Ton: ", Ton)

# 2nd sine wave
print("tdelay2: ", Tperiod/2+offset)

