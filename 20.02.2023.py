#python program to print all numbers range 1-n
upto = int(input("Find prime numbers upto: "))

print("\nAll prime numbers upto", upto, "are: ")

for num in range(2, upto + 1):

    i = 2

    for i in range(2, num):
        if(num % i == 0):
            i = num
            break;

    if(i != num):
        print(num, end=" ")
              
              
  #write a program to print your name, branch, age using a single print statement

def personal_details():
    name = 'Aakriti Sharma',
    age = 20,
    branch = 'cse'
    print('name: {}\nage: {}\nbranch: {}'.format(name, age, branch))
personal_details()



#_________________________________
CollegeName = 'MIET'
Branch = 'CSE'
Age = 20                                              
print(CollegeName)

print(type(Age))
variable = float(input())











#Write a python program to take the input of the marks and print '1' if the marks are greater than 40 and less than 80 otherwise '0'
grade =int(input("Enter the marks"))

if grade>= 40:
    print(1)
else:
    print(0)
    
    
    
    
    
    
  #Write a python program to check even or odd using bit manipulation 
#write a python program to toggle k the bit of a binary number

#bit manipulation 
def isEven(n):
        
        if((n^1)==(n+1)):
            return True
        else:
            return False
        
if __name__ == "__main__":
    n=10
    print(1) if isEven(n) else print(0)
    

    
    
    
    #toggle k
def toggleBit(n, k):
    
    return(n^(1<<(k-1)));
    
if __name__ == "__main__":
    n=5; k=2;
    print(toggleBit(n,k));
    
    
    
    
  
  
  
  
 #Write a python program to find the total number of unset bits in a number
#Write a python program to find the difference of set and unset bits in the number


#total number 
def countunsetbits(n):
    count= 0
    
    x=1
    while(x<n+1):
        if((x & n)==0):
            count += 1
        x = x << 1
    return count

if __name__ == '__main__':
    n = 17
    print(countunsetbits(n))
    
    
    
    
    
    
    
    
    
    
    #set and unset 
import math 
def totalbits(N):
    return(1+(int)(math.log(N)/math.log(2)))
def absoluteDifference(N):
    arr=N
    total_bits=total_bits(N)
    set_bits=countSetBits(arr)
    unset_bits=total_bits-set_bits
    ans=abs(set_bits-unset_bits)
    return ans
def countSetBits(n):
    count=0
    while(n>0):
        n=n&(n-1)
        count+=1
    return count
N=14
print(absoluteDifference(N))
        
  
  
  
  
  
  
  
