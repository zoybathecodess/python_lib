import numpy as np
#print(np.__version__)
""""
array = np.array([1,2,3,4])
array = array *2
print(array)
"""
#array dimensions
array = np.array([['a','b', 'c'],
                 ['we', 'rw', 'te']])
print(array.ndim)


array = np.array ([[['A','B','C'],['D','E','F'], ['G','H','I']]])
print(array.ndim)
print(array.shape) #depth, no. of rows, no. of columns


array = np.array ([[['A','B','C'],['D','E','F'], ['G','H','I']],
                   [['A','B','C'],['D','E','F'], ['G','H','I']]])
print(array.ndim)
print(array.shape)

#accessing elements
print(array[0][0][0]) #chain indexing
print(array[1,1,1]) #multidimentional indexing

#string concatenation
word =  array[0,0,1] + array[0,1,1] + array[0,1,0]
print(word)

#slicing
# array[start:stop:step]
array=np.array([[[1,2,3,4],
                 [5,6,7,8],
                 [9,10,11,12]]])
print(array.shape)
print(array.ndim)
print(array[:,:,0:2])


#scalar arithmetic
array = np.array([1.01,2.5,3.99])
print(array+1)
print(array*2)
print(array-1)
print(array/2)
print(array**2)


#vectorised arithmetic
print(np.sqrt(array))
print(np.round(array))
print(np.ceil(array))
print(np.floor(array))
print(np.pi)



#area of circle
radii = np.array([1,2,3])
print(np.pi * radii**2)


#element-wise arithmetic
array1 = np.array([10,20,30])
array2 = np.array([1,2,3])

print(array1+array2)
print(array1-array2)
print(array1*array2)
print(array1/array2)
print(array1%array2)

#comparision operators
scores = np.array([90,89,100,100,50])
print(scores==100)
print(scores>=70)
print(scores<=50)

#assigning any scores below 60 as 0
scores[scores<60] = 0
print(scores)

#matrix multiplication
# [] 2x4 * []4*1
array1 = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
print(array1.shape)

array2 = np.array([[1,2,3,4,5,6,7,8,9,10]])
print(array2.shape)

print(array1*array2)


#aggregate functions
array3 = np.array([[1,2,3,4],
                   [5,6,7,8]])
print(np.sum(array3))
print(np.mean(array3))
print(np.std(array3))
print(np.var(array3))
print(np.min(array3))
print(np.max(array3))
print(np.argmin(array3)) #postion of min value
print(np.argmax(array3)) #position of max value
#sum all columns
print(np.sum(array3,axis=0))
#sum all rows
print(np.sum(array3,axis=1))



#filtering
ages = np.array([[20,18,19,99],
                 [29,38,18,67]])
teens = ages[ages<=19]
print(teens)

adults = ages[ages>=20]
print(adults)

seniors = ages[ages>50]
print(seniors)
#where(condition, array, replacing_ value)
adults = np.where(ages >= 50, ages, np.nan) #retaining elements in the array that are greater than 50
print(adults)

#random numbers
rng = np.random.default_rng(seed=1) #using seed generates the same set of random values
print(rng.integers(low=1, high=7, size=3)) #size: number of random numbers to generate
#to generate random floating values, use uniform func
#to generate the same set of random values use seed func
np.random.seed(seed=1)
print(np.random.uniform(low=-1, high=1, size=(3,2))) #uniform func distributes values and every value has an equal probability of being seleted


#suffling an array
rng = np.random.default_rng()
array = np.array([1,2,3,4,5])
rng.shuffle(array)
print(array)


#choice
fruits = np.array(["apple", "banana", "pineapple", "kiwi"])
fruit_choice = rng.choice(fruits, size=(2,3))
print(fruit_choice)


# --> arithmetic --> linspace function
array= np.linspace(1,10,5) #evenly divide numbers from 1 to 10 by 5
print(array)

# stacking arrays
a = np.array([1,2,3])
b = np.array([4,5,6])

horizontal = np.hstack((a,b))
print(horizontal)

vertical = np.vstack((a,b))
print(vertical)

#numpy functions
array = np.zeros((2,2),int)
print(array)

array = np.ones((5,6),int)
print(array)

array = np.full((3,2), 6)
print(array)

print()
array = np.eye(2,2) #eye function fills the array with identity values (0 and 1)
print(array)

print()
array = np.empty((2,3)) #prints garbage values
print(array)

print()
array = np.arange(0,100, 1) #values between start and stop with a step value (start, stop,step)
print(array)

