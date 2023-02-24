#tuples,sets and dictionaries
#write a python program to print the element with highest frequency
#arr=[4,56,67,78,45,56,56,45,45,23]
maxx=0
listtt=0
listt=input().split()
for i in listt:
    if listt.count(i)>=maxx:
        maxx=listt.count(i)
        element=i
    if i not in listtt:
        listtt.append()

    if listt.count(i)==maxx:
        for i in listtt:
            if listt.count()==max:
                pass
            else:
                listt.remove()


print(element,'frequency is',maxx)



#-hackerrank
n,k=list(map(int,input().split()))
arr=list(map(int,input().split()))
amount=int(input())

arr.pop(k)
amount_anna=sum(arr)/2
if amount_anna==amount:
    print("bon appetit")
else:
    print(abs(amount-amount_anna))
    
    
    
    
    
    

#tuples data structures
tup=(23,23,True,"class")




#write a python program to sort all the elements of the list based on the function you are passing in sort method
def elements():
    pass 
listt=[23,23,24,22]
print(listt.sort(elements))





#tuples are used as a permanent storage as it is secure and cannot be modified
#tuple packing
t=23,34,3,4,45,45,34,2,1,2,456,6
print(t)
a,b,c,d,*e=t
print(a,b,c,d,*e)
print(t[::3])





'''listt=[23,34,34,45]
listtt=list(i for i in listt if i%2==0 )
print(listtt)





#sets
#duplicates not allowed,no indexes,insertion order is not present.
#used concept called hashing to store elements.
#cannot be kept empty as it will be a empty dictionary. can be kept empty using constructors with parameters.set().
#iterables=lists,tuples
#discard()
sett={12,12,14,56,78}
sett1={3,12,56,77,55}
sett.add(90)
print(sett)
re= sett.pop()
print(re)
x=sett.union(sett1)
print(x)





x=input("enter the string!:-")
#x="learning python is very easy"
y=x.split()
z=y[::-1]       
print("----------".join(z))




#write a python program to count the even and odd digits in a given number
even=0
odd=0
number=int(input("enter the number: "))
while number:
    z=number%10
    number//=10
    if z%2==0:
        even+=1
    else:
        odd+=1
    
print("even digits:-",even, "odd digits:- ",odd)
    
