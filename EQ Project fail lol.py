import matplotlib.pyplot as plt
plt.clf()

#open the file
EQdata = open("currentQuakes.txt")
EQdata.readline()

#give your data a name
Longitude = []
Latitude = []
#Color = 

for line in EQdata:
   line = line.split(',')
   print(line)
   Latitude.append(float(line[1]))
   Longitude.append(float(line[2]))

plt.xlabel("Longitude")
plt.ylabel("Latitude")  

img = plt.imread("worldMap.jpg")

plt.imshow(img, extent= [-180, 180, -180, 180])

plt.scatter(Longitude, Latitude, alpha=0.5)
plt.show()