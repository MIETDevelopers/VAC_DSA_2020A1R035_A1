#stack data structures
#implementation of stack using list data structures 
##lifo----last in first out 
##filo----first in last out
##only you can add or delete element from top
##underflow=deleting a element when your stack is empty
##overflow=adding a element when your stack is full.

stack=[23,34]
stack.append(45)
stack[-1]



#you need to design a code for len() function
listt=[34,45,56]
count=0
for i in listt:
    count+=1
count


from collections import deque
stack=deque()
stack.append()
stack.appendleft()
stack.popleft()


class list:
    def pop(self,index=len(arr)-1)
    
    
    #Balanced parenthesis
#Input format:
#The first line contains a single integer n, the number of strings.
#Each of the next n lines contains a single string s, a sequence of brackets
#Output format:
#For each string, return YES or NO



def parenthesis(strr):
    stack=[]
    listt1=['[','(','{']
    listt2=[']',')','}']
    for i in strr:
        if i in listt1:
            stack.append(i)
            #index=listt1.index(i)
        elif i in listt2:
            if len(stack) ==0:
                 print('unbalanced parenthesis')
                 return 
            elif listt1[listt2.index(i)]==stack[-1]:
                 stack.pop()
                 continue
            else:
                print('unbalanced parenthesis')
                return
    if len(stack)==0:
        print('Balanced parenthesis')
        return
    else:
        print('unbalanced parenthesis')
        
        
s=input()
parenthesis(s)


arr=[34,45]
arr.pop()
arr.insert(0,12)
print(arr)
arr.pop()
arr.pop()


from collections import deque
queue=deque()
queue.appendleft(34)
queue
.appendleft(90)
print(queue)


from collections import deque
deque1=deque()


#write a python program to reverse a string without using inbuilt python functionality


# Write a python program to Check the given number is power of 2 or not


#write a program to add all the elements given in the list
list1=[1,2,3,4,5]
listt=sum(list1)
print(listt)

#---------
'''listt=list(map(int,(input().split())))
y=listt
print(sum(y))'''

#--------------
'''listt=list(map(int,(input().split())))
sum=0
for i in listt:
    sum=sum+i
print(sum)'''

val=input().split()
key=[]
dict={}
for i in val:
    key+=[i[0]]
for i in range(len(val)):
    print(key[i],":",[val[i]])
