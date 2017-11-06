import matplotlib.pyplot as plt
plt.clf()

#open the file
EQdata = open("currentQuakes.txt")
EQdata.readline()

import matplotlib.image as mpimg
image = mpimg.imread("worldMap.jpg")
plt.imshow(image)

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

plt.scatter(Longitude, Latitude, alpha=0.5)
plt.show()