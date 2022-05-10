f = open("exampleQuadrupoleData.txt", mode = "w")
for i in range(0,100):
	for x in range(0, 100):
		f.write("99.99,")
f.close