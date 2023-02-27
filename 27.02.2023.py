#--------------------binary search------------------------
#divide and conquer algorithm
#binary search= 0+len(arr)-1//2; mid=middle index of the array.
'''l=[2,3,4,5,6,7]  #ascending array
key=6
low=0
high=len(l)
mid=low+high//2
if l[mid]==key:
    print("we have found our number")
elif l[mid]<key:
    l=mid+1
elif key<mid:
    high=mid-1'''
#again repeat all these steps until the length of array becomes one.
#time complexity= ''k=log2(n)''
'''listt=list(map(int,input().split()))
listt.sort()   #it will sort the array into ascending order.
low=0
key=int(input())
high=len(listt)-1
while low<=high:
    mid=low+high//2
    if listt[mid]==key:
        print("element found at index: ",mid)
        break
    elif key>listt[mid]:
        low=mid+1
    elif key<listt[mid]:
        high=mid-1'''
    

#---------------ternary search---------------------------
#it will divide the array into three parts.
'''arr=list(map(int,input().split()))
l=0
key=45
high=len(arr)-1
mid1=high-(l+high)//3
mid2=l+(l+high)//3
while l<=high:
    if key==arr[mid1]:
        print("element found at index:-",mid1)
        break
    elif key==arr[mid2]:
        print("element found at index:-",mid2)
    elif key>arr[mid1]:
        l=mid1+1
    elif key>arr[mid2] and key<arr[mid1]:
        l=mid2+1
        high=mid1-1
    elif key<arr[mid2]:
        high=mid2-1'''
#---------jump search-----------------------------------------
#time complexity=O(underoot(n))
#--------------interpolation search-------------------------
#only applicable in uniformly sorted data.
#arr[high]=y *m(high)+c--1
#arr[low]=y *m(low)+c--2
#subtracting both equations 1 and 2
#arr[high]-arr[low]=m*[high-low]--3
#m=arr[high]-arr[low]//high-low--4
#key=m*pos+c---4
#subtract 2 and 4
#arr[high]-key=m(high-pos)
#m=(ar[high]-key)/(high-pos)
#m=(ar[high]-key)/(high-pos)--5
#pos= low+(high-low)//(x-arr[low]*(arr[high]-arr[low]))
'''listt=list(map(int,input().split()))
key=int(input())
low=0
high=len(listt)-1
while low<=high and key<=listt[high] and key>=listt[low]:
    pos=low+((key-listt[low])*(listt[high]-listt[low]))//
    if listt[pos]==key:
        print("element found at index:-",pos)
        break
    elif listt[pos]<=key:
        low=pos+1
    elif listt[pos]>=key:
        high=pos-1 '''
#write a program to search the index of the second element occurence if it is present more than one time ex-[23,3,4,45,56,67] searching by default wil give you 
#first occurence index need to apply logic to fijnd the second occurence.
#that is in this case i=4 by default you will get =4
#-------------------------------bubble sort-----------------------------
'''arr=list(map(int,input("Enter the List: ").split()))
for i in range(len(arr)):
    for j in range(len(arr)-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)'''
#time complexity=O(n**2)
#------------------selection sort-----------------------------
'''arr=[23,34,45,11,21,78]
minimum= arr[0]
for i in range(len(arr)):
    minimum=i
    for j in range(i+1,len(arr)):
        if arr[j]<arr[minimum]:
            minimum=j
    arr[i],arr[minimum]=arr[minimum],arr[i]
print(arr)'''
#selection sort steps
#1) find the smalllest value in the given array/list.
#2) swap it and bring it to the first position.

#----------------------merge sort----------------------------------------
#---------------merging two sorted arrays--------------------------------
#write a program to implement merge sort---------------------------------
#-------------------------------insertion sort---------------------------
