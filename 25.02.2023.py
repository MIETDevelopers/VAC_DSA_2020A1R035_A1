#write a python program for following details
''''input=day num 3
you need to count number of likes
5 people they will share
5//2
will like 
5 got advertisement---> 2 liked
6 people got----> 3 liked
9 people got---> 4 liked
12--->6
18--->9''''

d_n = int(input())
people=5
total=0
for i in range(d_n):
    total=total+people//2
    people=(people//2)*3
print(total)



#write a python program to print all the permutations of a string
def permute(s, l, r):
    if l == r:
        print("".join(s))
    else:
        for i in range(l, r + 1):
            s[l], s[i] = s[i], s[l] 
            permute(s, l + 1, r)
            s[l], s[i] = s[i], s[l]
string = input("Enter a string: ")
n = len(string)
s = list(string)
print("Permutations of the string:")
permute(s, 0, n - 1)




class name():
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print(self.b)
        print('miet')
    def display(self,rt):
        print(rt)
obj=name()



#write a python program to create a class 'emp'
''''method employee data
what you need to store employee id name,phone,salary add one more method
salary calculation 
take input of number of days present and calculate the exact salary you need to''''



class Employee:
    def __init__(self, emp_id, name, salary, address, phone_number):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
        self.address = address
        self.phone_number = phone_number
    
    def calculate_salary(self, days_present):
        daily_salary = self.salary / 31
        exact_salary = daily_salary * days_present
        return exact_salary
emp = Employee("1234", "Aakriti Sharma", 50000000, "Jammu", "1234567890")
salary = emp.calculate_salary(25)
print(f"{emp.name}'s salary is {salary}")



class arya():
    def __init(self):
        pass
    def display(self):
        print("Hello class")
        def display(self,name):
            print(name)

obj=arya()
obj.display()



class A():
    def __init__(self,name,id):
        self._name=name
        self.i=i
class B(A):
    def _display(self):
        print(self._name)
class C(B):
    pass
obj=C('atul',34)

obj._display()
        
  
  
  #Searching and sorting 
linear search 
binary search
jump search
interpolation search 

#sorting
bubble
selection 
insertion 
merge
quick
heap
shell
radix
count


#write a python program to sort the string 'miet'
strr=input()
l=sorted(strr)
strr1=''.join(l)
print(strr1)
print(l)



#write a python program to find sum of digit of elements in a list'
#ex=[23,34,45,56]
#output=2+3+3+4+4+5+5+6=32



ex = [23, 34, 45, 56]
def sum_of_digits(num):
    num_str = str(num)
    digit_sum = 0
    
    for digit in num_str:
        digit_sum += int(digit)
    return digit_sum
total_sum = 0
for num in ex:
    total_sum += sum_of_digits(num)
print(total_sum)



#write a python program to generate a list where next term is the square addition of the even digits of the previous terms 
#default is list=[42]

def generate_list(n=1):
    lst = [42] 
    for i in range(n):
        prev = lst[-1]
        even_digits = [int(digit)**2 for digit in str(prev) if int(digit)%2 == 0]
        next_term = sum(even_digits)
        lst.append(next_term)
    return lst

  
  
  #Write a  python program to generate a list where every next elements is 
#power of place value of even digits of the number
#if output generated is one digit then square it
#until it is two digit

[1234]
4+8=12
12-2-4-16
16-6-36
[1234,12,36,36,36]
list will keep on adding elements unless a element is 
repeated three times consecutively


listt=[1234]
count=True
while count:
