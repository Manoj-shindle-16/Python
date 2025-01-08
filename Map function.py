# sort a list of tuple based on second element 
# input data = [(1,3),(4,1),(2,2)]
# Expected output  [(4,1),(2,2),(1,3)]

data = [(1,3),(4,1),(2,2)]
# l = len(lst)
# for i in range (0,l):
#     for j in range (0,l-i-1):
        
sorted_data = sorted(data ,key=lambda x : x[1])
print(sorted_data)