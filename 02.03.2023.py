#------------Graphs--------------------
#A data structure that consists of a set of nodes and set of edges that relate the nodes to each other. Set of edges describe the relationship between the nodes.
#graph= G(V,E)
#V(G)=finite,non empty set of vertices
#E(G)=set of edges
#When edges in the graph have no direction,undirected graph, whereas if they have a direction, they are a directed graph.(order of the vertices is important in dirwcted graph.)
'''
Adjacent nodes= nodes connected by an edge.
Path= sequence of vertices that connect two nodes in a graph.
Number of edges n*(n-1)
Time complexity= 0(n**2)
Weighted Graph= each edge carries a value.
LINKED-LIST IMPLEMENTATION
An 1D array used to represent vertices
A list of edges is maintained..
OPERATIONS IN GRAPHS
Backtracking and Depth-First Search= search till the end for all possible solutions. turn the side if we find a dead end.
when reached dead end, backtrack.
Graphs are represented by a 2-D matrix.
BREADTH FIRST SEARCH= can go in any direction. Used on queues.
1)put any of the graphw vertices in the back of the queue.
2)take the front item of the queue.





#write a python program to solve n queens problem and print all the permutations of a string using backtracking algorithm

#write a python program to find the sum of harmonic series where series is starting 
#from 4 and harmonic difference is 1/3
#till n terms where n is the input
#ex- n=5
#x=1/3 constraint 0<x<1
#output= 4+ 4/3+4/9+4/27+4/81

n=int(input())  
s=0  
x=1/3  

for i in range(n):
    t=4/(x**i)  
    s+=t  
print("Sum of the harmonic series:", s)  




#write a python program to find the absolute difference between addition of even alphabets and odd alphabets
#from all combinations of strings print combinations and absolute difference values of a=1,b=2 and so on 
#ex-asp
#combinations are---> asp absolute difference a+p-s=1+16-19=2, as, p, a
#contraint-string length greater than 5 and less than 20

import itertools

a_v={"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}
def e_o_d(combination):
    e_s=0
    o_s=0
    for char in combination:
        if a_v[char]%2==0:
            
            
            e_s+=a_v[char]
        else:
            o_s+=a_v[char]
    return abs(e_s-o_s)

input_str="asp"

combinations = list(itertools.chain.from_iterable([itertools.combinations(input_str, i) for i in range(len(input_str) + 1)]))
for combination in combinations:
    diff = e_o_d(combination)
    print(combination, diff)
    




    
