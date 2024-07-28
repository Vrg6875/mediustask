#sum of list

l=[10,20,30]
s=0
for i in l:
    s+=i

print(s)    

#ya

print(sum(l))




#multiply all items in alist
a=[10,20,40]
mul=1
for i in a:
    mul*=i
print(mul)    





#find largest number list

a=[10,30,50,77]
max_no=a[0]

for i in a:
    if i>max_no:
        max_no=i
print(max_no)


#find smallest number list
b=[66,88,44,33,8]
min_no=b[0]
for i in b:
    if i<min_no:
        min_no=i
print(min_no)        


#write a program to check the first and last character are same from a given list of string 
#expexted output:2
word=["madam","323","apple","3756"]

ch=0

for i in word:
    if len(i)>1 and i[0]==i[-1]:
        ch+=1
print(ch)        


#remove dublicates from a list
v=[10,33,44,10,33,55]
dup=set(v)
print(list(dup))

#ya
k=[]
for i in dup:
    k.append(i)
print(k)    

#check list empty or not
kk=[]
if not kk:
    print('empty')
else:
    print('not empty')    


#write a program to clone or copy a list
old_list=[10,20,30]
new_list=list(old_list)
print(new_list)


#find the list of word that are longer than a from a given list of words

n=int(input('enter no'))

str_="my name is vicky kumar tumhara naaaam kya hai"

new_l=[]

text=str_.split()

for i in text:
    if len(i) > n:
        new_l.append(i)
print(new_l)        


#write a program that get two list as input and check if they nhave at less one common member

list1=[10,20,40,77]
list2=[22,33,40,77]

for i in list1:
    for j in list2:
        if i==j:
            result=True
print(result)
