import math

nsample = int (input ("Number of Samples: "))
nvar = int (input ("Number of Variables: "))
k = int (input ("Number of Clusters: "))

sampleList = [[0 for x in range(nvar)] for y in range(nsample)]

#Input samples
sampleCount = 0
for sample in sampleList:
	print ("\n\nCollecting Data for Sample #{}:".format(sampleCount+1))
	print ("----------------------------------------")
	i = 0
	while i < nvar:
		sample [i] = int (input ("Data for var-{} : ".format(i+1)))
		i += 1

#First k samples are chosen as cluster centroids
centroidList = [[0 for x in range(nvar)] for y in range(k)]
i = 0
while i < k:
	j = 0
	while j < nvar:
		centroidList[i][j] = sampleList[i][j]
		j += 1
	i += 1

# distanceList maintains Euclidean distance of given sample
# for all clusters k
distanceList = [0.0 for x in range (k)]

#Open file for writing assignments
fileObject = open ("assignment-results.txt","w")

for sample in sampleList:
	n = 0
	for centroid in centroidList:
		var = 0
		total = 0
		while var < nvar:
			temp = (sample[var] - centroid[var]) ** 2
			var += 1
			total += temp
		distanceList[n] = math.sqrt (total)
		n += 1
	#Write assignments to file
	fileObject.write("{} \t {}\n".format(sample, distanceList.index(min(distanceList))+1))

#Close the file
fileObject.close()
print ("\n\n Final assignments successfully written to file! \n")
