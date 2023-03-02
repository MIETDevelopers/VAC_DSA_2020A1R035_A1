#write a python program to find the largest palindrome number that can be created from the list
listt=[2,3,4,5,6,0,8,0,5,45]


#Write a python to reverse a linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse_linked_list(head):
    previous_node = None
    current_node = head

    while current_node is not None:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node

    return previous_node



#Write a python program for linear search on tuples
#Input: kiran sachin 24 12 the
#key: 12
#output: found

def linear_search_tuple(tup, key):
    for item in tup:
        if item == skey:
            return "found"
    return "not found"
tup = ("kiran", "sachin", 24, 12, "the")
key = 12
result = linear_search_tuple(tup, key)
print(result) 


# write a python code of merge sort divide and conquer

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    
    return result

arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_arr = merge_sort(arr)
print(sorted_arr)


#write a python program convert a given string list to a tuple.
#input: virat kohli 18
#output: ('v','i','r','a','t','k','o','h','l','i','1','8')

s_l = input().split()  
tup = tuple(''.join(s_l)) 

print(tup)


#write a python program to find the sum of all the items in a dictionary
#take values in numeric type(n>0)
#Input:
#4
#Arjun
#40
#Varun
#45
#Tharun
#50
#Charan
#55
#Output:190


n = int(input())
d = {}
for i in range(n):
    key = input()
    value = int(input())
    d[key] = value

sum = 0
for value in d.values():
    sum += value

print(sum)

#Write a python program to create a dictionary with key
#as first character and value
#as words starting 
