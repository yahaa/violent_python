from numpy import *
from matplotlib import pyplot as plt

def loadDataSet(filename):
    dataMat=[]
    with open(filename,'r') as f:
        for item in f.readlines():
            dataMat.append(map(float,item.split()[:2]))
    return dataMat

def distEclud(vecA,vecB):
	return sqrt(sum(power(vecA-vecB,2)))

def randCent(dataSet, k):
    n = shape(dataSet)[1]
    
    centroids = mat(zeros((k,n)))#create centroid mat
    for j in range(n):#create random cluster centers, within bounds of each dimension
        minJ = min(dataSet[:,j]) 
        rangeJ = float(max(dataSet[:,j]) - minJ)
        centroids[:,j] = mat(minJ + rangeJ * random.rand(k,1))
    return centroids

def kMeans(dataSet,k,distMeas=distEclud,createCent=randCent):
	m=shape(dataSet)[0]
	clusterAssment=mat(zeros((m,2)))
	centroids=createCent(dataSet,k)
	clusterChanged=True
	while clusterChanged:
		clusterChanged=False
		for i in range(m):
			minDist=inf;minIndex=-1
			for j in range(k):
				distJI=distMeas(centroids[j,:],dataSet[i,:])
				if distJI<minDist:
					minDist=distJI;minIndex=j
		if clusterAssment[i,0]!=minIndex:clusterChanged=True
		clusterAssment[i,:]=minIndex,minDist**2

		for cent in range(k):
			ptsInClust = dataSet[nonzero(clusterAssment[:,0].A==cent)[0]]
			centroids[cent,:]=mean(ptsInClust,axis=0)
	return centroids,clusterAssment

data_set=loadDataSet('boynew.txt')
data_set.__iadd__(loadDataSet('girlnew.txt'))
data_set=array(data_set)
k=2

my_cen, my_clu = kMeans(data_set, k)
plt.figure(figsize=(8, 8))
for p in data_set:
    minDist = inf; minIndex = -1
    for j in range(k):
        dist = distEclud(p, my_cen[j, :])
        if dist < minDist:
                    minDist = dist; minIndex = j
    plt.plot(p[0], p[1],  'r*' if minIndex==0 else 'b*')
plt.plot(my_cen[0, 0], my_cen[0, 1], 'r^', markersize=20)
plt.plot(my_cen[1, 0], my_cen[1, 1], 'b^', markersize=20)
plt.show()


# print(dataSet)