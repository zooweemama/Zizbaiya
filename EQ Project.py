import matplotlib.pyplot as plt
plt.clf()

#open the file
EQdata = open("currentQuakes.txt")
EQdata.readline()

#give lists a name
ShallowLongitude = []
ShallowLatitude = []
DeepLongitude = []
DeepLatitude = []

#add data to lists
#change color according to depths
for line in EQdata:
    line = line.split(',')
    #print(line)
    if float(line[3]) > 50:
        DeepLatitude.append(float(line[1]))
        DeepLongitude.append(float(line[2]))
    else:
        ShallowLatitude.append(float(line[1]))
        ShallowLongitude.append(float(line[2]))

#plot dots on graph        
plt.scatter(ShallowLongitude, ShallowLatitude, alpha=0.5,color='r')
plt.scatter(DeepLongitude, DeepLatitude, alpha=0.5,color='b')

#inserting the image as a background
img = plt.imread("Earth.jpg")
plt.imshow(img, extent= [-197,197,-63,87])
 
#label axes and including a title   
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.suptitle("Zizbaiya Earthquake Plot")

plt.show()
