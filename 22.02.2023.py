#strings
art="miet"
art[2]
for i in art:
    print(i)


#slicing syntax


#name_string[start,end,step]
#timecomplexity=O(1)
print(art[1:3])#1,n-1




# write a python program to print all the sub-strings from the original strings
x="jeon jungkook"
n=len(x)
for i in range(n):
    for j in range(i+1,n+1):
        print(x[i:j])




#write a python program to print all substrings where some vowels in substrings equals 6
x='abcdefghijklmnopqrstuvwxyz'
vowels='aeiou'
key=6
ex=input("enter the string: ")
n=len(ex)
for i in range(n):
    for j in range(i+1,n+1):
        total=0
        for a in (ex[i:j]):
            if a in vowels:
                value=x.index(a)
                total+=value+1
        if total==key:
           print(ex[i:j])




#program:- input:a4b3c2; output=aaaabbbcc
x=input("enter the string and number: ")
y=len(x)
alphabets=""
digits=""
for i in range(y):
    if i.isaplha():
        print()
    else:
        print(i*alphabets)


#methods in string



#validation methods= isaplha,isdigit,split,strip()
a="aakriti  "
print(a.strip())
print("miet".split())
a='aditi'
print(a.count('e'))
print(a.find('e'))
if a.alnum():
    print(a)
    

#replace()
a.replace('a','t')


#if we get the address of the single part of the database, the whole database can be breached.



#write a python program to merge two strings
s1='DNATA'
s2="OMNHN"
new_string=""
for i in range(len(s1)):
    new_string=new_string+ s1[i]+ s2[i]
print(new_string)




#functions
#write a python function to print all combinations to get 26 after addition
sum=int(input())
def add(num):
    for i in range(1,num):
        if i==1:
            print("1"*num)
        for j in range(1,i):
            if i+j==sum:
                print(i,j)
                for a in range(num):
                    if a+i+j==num:
                        print(a,i,j)
add(sum)





#list data structure
arr=[1,2,3+5j,True]
for i in range(len(arr)):
    print(arr[i])
for i in arr:
    print(i)





#methods
addition:
append()
insert(index:value)
delete()
pop()
remove()/discard()
clear()






#retrive
#arr[index]
#count()
#index()
#copy()








#write a python program to find factorial of n
n=int(input("enter the number: "))
fact=n
for i in range(1,n+1):
    fact=fact*i
print(fact)






#write a python program to print the factors of n
ch=int(input("enter the number: "))
def fact(ch):
    for i in range(1,ch+1):
        if ch%i==0:
            print(i)
print(fact(ch))





#write a python program to  print inverted pyramid
ch=int(input("enter the number: "))
k=0
for i in range(ch,0,-1):
    k+=1
    for j in range(1,i+1):
        print(k,end=" ")
    
    print('\n')


#
'''s="abra ka dabra"
print(s.capitalize())
print(s.upper())



#Pooja would like to withdraw Xrs from an ATM. The cash machine will only accpet the transaction if x is multiple of 5 and Pooja's account balance has enough cash to perform the transaction.
#calcualte balance after transaction
initial_balance= 10000

x=int(input("enter the amount: "))
count=1
while count:
    if x%5==0:
        if x>=initial_balance:
            print("NOT ENOUGH BALANCE!")
        else:
            debit= initial_balance-x-1.5
            transactions=debit
            if transactions<3:
                print("money debitted successfully",(initial_balance-x-1.5))
            if transactions>=3:
                print("attempts over")
            
        count=0    
    else:
        print("not possible")





#basketball wala code
apple_3points=int(input("enter the number of 3 pointers of a: \n"))
apple_2points=int(input("enter the number of 2 pointers of a: \n"))
apple_1points=int(input("enter the number of 1 pointers of a: \n"))
bananas_3points=int(input("enter the number of 3 pointers of b: \n"))
bananas_2points=int(input("enter the number of 3 pointers of b: \n"))
bananas_1points=int(input("enter the number of 3 pointers of b: \n"))
scoreA=3*apple_3points+2*apple_2points+1*apple_1points
scoreB=3*bananas_3points+2*bananas_2points+1*bananas_1points
print("score is",scoreA)
print("score is",scoreB)
if scoreA>scoreB:
    print("a wins")
if scoreB>scoreA:
    print("B wins")
if scoreA==scoreB:
    print("tie")

