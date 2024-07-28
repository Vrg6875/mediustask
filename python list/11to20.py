#write a program to print a specified list after removing the 0th,4th and 5th

animal=['kutta','dog','billi','fox','elephant']
animal=[x for (i,x) in enumerate(animal) if i not in(0,2,3) ]

print(animal)

#write a program to print the numbers of a specified list after removing even numbers from it
a=[10,11,13,14,14,16,17,18]
a=[x for x in a if x%2!=0]
print(a)

#writw a program to shuffle and print specified list
from random import shuffle
animal=['kutta','dog','billi','fox','elephant']
shuffle(animal)
print(animal)

#write a program to genrate and print a list first and last five elements where the values are square of numbers beetween 1 to 30
l=list()
for i in range(11,25):
    l.append(i**2)


print(l[:5])
print(l[-6:-1])

#write a program to give all permutation 
import itertools
print(list(itertools.permutations([1,2,3])))

#write a program to convert a list of chracters in to string
s=['v','i','c','k','y']
s1=''.join(s)
print(s1)

#find the item in list
x=[10,20,40,38]
print(x.index(10))