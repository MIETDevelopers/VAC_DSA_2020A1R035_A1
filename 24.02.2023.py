#Write a python program to convert a list into a list of dictionaries
arr=['miet','model','aakriti','institute']
arr_2=[23,34,45,56]
output=[{'miet':23},{'model':34},{'aakriti':45},{'institute':56}]
arr=input().split()
arr_2=input().split()
dictt={}
listt=[]
for i in range(len(arr)):
    dictt[arr[i]]=arr_2[i]
    listt.append(dictt)
print(listt)




#Your local library needs your help! Given the expected and actual return dates for a library book, create a program that

#the fine (if any) The fee structure is as fotos

#If the book is returned on or before the expected return date, no line will be charged (ce fine-0).

#21 the book is retumed aller the expected returis day but still within the same calendar month and year as the expect date, fine 15 Hackos x (the number of days late).

#3 If the book is returned after the expected retum month but still within the same calendar year as the expected return

#fine = 500 Hackos x (the number of months late)

#4.If the book is returned after the calendar year in which it was expected, there is a found line of 10000 Hackos Charges are based only on the least precise measure of lateness. For example, whether a book is de January 1, 201 December 31, 2017 if it is returned January 1, 2018, that is a year late and the line would be 10,000 Hackos

#Example

#dl, ml, pl-14,7, 2018


def calculate_fine(d1, m1, y1, d2, m2, y2):
    if y2 < y1:
        return 10000
    elif y2 == y1:
        if m2 < m1:
            return 500 * (m1 - m2)
        elif m2 == m1 and d2 <= d1:
            return 0
        else:
            return 15 * (d2 - d1)
    else:
        return 10000


d1, m1, y1 = map(int, input("Enter the expected return date (dd mm yyyy): ").split())
d2, m2, y2 = map(int, input("Enter the actual return date (dd mm yyyy): ").split())
fine = calculate_fine(d1, m1, y1, d2, m2, y2)
print("Fine:", fine, "Hackos")


#write a python program to calculate a factorial of number using reccurison
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
a = int(input())
result = fact(a)
print("Factorial of", a, "is", result)





#Write a python program to calculate prime number between 1-100 using recursion

def p_n(n, div=2):
    if n < 2:
        return False
    elif div == n:
        return True
    elif n % div == 0:
        return False
    else:
        return p_n(n, div+1)

def prime(low, up):
    if low > up:
        return
    elif p_n(low):
        print(low)
    prime(low+1, up)

prime(1, 100)




#Write a python program to calculate prime number between 1-n using recursion
def check_prime(n, i=2):
    if n==i:
        return True 
    elif n%i==0:
        return False 
    else:
        return check_prime()
      
      
      
      #OOPS
#Classes- Definitions which will contain the methods of  a partivular class
#Objcects- Instance of a class
class miet():
    def addition(self):
        pass
    def sub(self):
        pass
    
print(miet)


class miet():
    def addition(self):
        pass
    def sub(self):
        pass

arr=miet()
x=10
def miet(er):
    global x
    x=23
miet(34)
x=9
print(x)



#write a program to create a class 'cse' and in that class create methods as name and data

class cse():
    x=27
    def __init__(self,n,b):
        self.name=name
        self.b=b
    def branch(self):
        print(self.name)
        
    def name(self):
        pass
    def create_dict(self):
        dictt={self.n:self.b}
        print(dictt)
        print(x)
arr=miet('atul','cse')
arr.create_dict()



#In an interview, following code snippets were provided.
#The lists present were:
import copy
list1=[2,5,[8,0],7]
list2=[3,9,1]
list3=copy.copy(list1)
list4=copy.deepcopy(list2)
list1[2][0]=777
list2[2]=888

print("List 3 elements")
for i in range(0,len(list3)):
    print(list3[i],end=" ")
print("/r")

print("List 4 elements - ")
for i in range(0,len(list4)):
    print(list4[i],end=" ")

    
    
    
    
    '''given a list, the task is to write a python program to find the index containing 
string.
input= Navya,98,Hema,Siroj,Tarun,78,90,Ramya
output=0 2 3 4 7'''


L1=['Navya',98,'Hema','Siroj','Tarun',78,90,'Ramya']
for i in range(len(L1)):
    if str(L1[i]).isalpha():
        print(i,"",end="")

        
        
                
