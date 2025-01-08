# Create a lambda functionn to find the maximum of Two Numbers
# input = 5,10
# output = 50

# max = lambda x,y,z : x if x>y and x>z else y if y>z else z
# print("The max value is : ",max(5,10,12))

# Check if a string is Starts with a specific character  using lamda
# input = hello , h
# output = True

# check = lambda x,y : x.startswith(y) 
# print(check("hello","h"))

#Filter out All the Vowels from A list of Characters 
# input = Chars = ['a','b','e','i','o','u','z']
# output = ['a','e','i','o','u']

# Chars = ['a','b','e','i','o','u','z']
# Result = list(filter(lambda x : x in "aeiou" , Chars))
# print(Result)

#Given a list of integer filter out all 
# the numbers thet are divisible by 3 & 5 
#input :  Numbers = [15,30,10,45,60,22]
#output : [15,30,45,60]

# Numbers = [15,30,10,45,60,22]
# Result = list(filter(lambda x : x%3==0 and x%5==0,Numbers))
# print(Result)

#Filter out all strings longer than 5 characters in a list 
# input : ['apple','banana','cat','dog','elephant','dianosours']
# output : ['apple','cat','dog']

# lst = ['apple','banana','cat','dog','elephant','dianosours']
# Result = list(filter(lambda x : len(x)<=5,lst))
# print(Result)


#Square every number in list using map function 
#input : numbers = [1,2,3,4,5]
#output : [1,4,9,16,25] 

# numbers = [1,2,3,4,5]
# sq_list = list(map(lambda i : i**3 , numbers))
# print(sq_list)

#convert a list of strings to upper case using map()
#input : words = ['hello','world']
# output : ['HELLO','WORLD']

# words = ['hello','world']
# up_words = list(map(lambda a : a.upper(),words))
# print(up_words)

#add 10 to each number in a list using map()
#input : numebrs = [1,2,3]
#output : [11,12,13]

# numebrs = [1,2,3]
# add_nums = list(map(lambda x :x+10,numebrs))
# print(add_nums)

#find the product of all the numebers in a list using reduese function
#input : numbers = [1,2,3,4]
#output : [24]

# from functools import reduce
# numbers = [1,2,3,4]
# res = reduce(lambda a,b : a*b ,numbers)
# print(res)

#find the longest word in a list of strings using reduce()
#input : words = ['apple','banana','cat','elephant']
#output : 'elephant'

# from functools import reduce
# words = ['apple','banana','cat','elephant']
# str = reduce(lambda a,b :a if len(a)>len(b) else b ,words)
# print(str)
# 1st iteration: a=apple, b=banana =>banana
# 2nd iteration: a=banana, b=cat =>banana
# 3rd iteration: a=banana, b=elephant =>elephant

#concatinate list of strings into a single string using reduce function 
#input : ['welcome','to','skyllx']
#output : 'welcometoskyllx'

# from functools import reduce
# words = ['welcome','to','skyllx']
# str = reduce(lambda a,b : a+b ,words)
# print(str)
# 1st iteration: a='welcome', b='to' => str=  'welcometo'
# 2nd iteration: a='welcometo', b='skyllx' => str = 'welcometoskyllx'

#Given a list of numbers ,filter out even numbers , squre them , and find their sum
#input : [1,2,3,4,5,6]
#output : 56

# from functools import reduce
# lst = [1,2,3,4,5,6]
# sum = reduce(lambda a,b : a+b ,map(lambda i : i**2 ,filter(lambda x : x%2==0,lst)))
# or
# even_numbers = list(filter(lambda x : x % 2 == 0, lst ))
# even_squares = list(map(lambda x : x**2,even_numbers))
# sum = reduce(lambda a, b : a+b, even_squares)
# print(sum)

#using lambda,filter,map function ,process a list of dictionaries to extract and transform a specific values 
#input : data = [{'name':'Manoj' , 'age': 25},{'name': 'Kumar' , 'age': 20},{'name': 'Shindle','age': 28}]
#task 1 : Extract the names of the peaple older than 25 in upper case
#output : ['SHINDLE']

# res = list(map(lambda x : x['name'].upper() ,filter(lambda a : a['age']>25 , data)))
# or
#data = [{'name':'Manoj' , 'age': 25},{'name': 'Kumar' , 'age': 20},{'name': 'Shindle','age': 28}]
# filtered_data = list(filter(lambda a : a['age']>25 , data))
# extract_name = list(map(lambda x : x['name'].upper() ,filtered_data))
# print(extract_name)

#find the factorial of a number using reduce ,lamda function
#input : 5
#output : 120

# from functools import reduce
# n = int(input("Enter the number to find Factorial..."))
# fact = reduce(lambda x,y :x*y ,range(1,n+1))
# print(fact)
# range(1,n+1)=>range(1,6)=[1,2,3,4,5]
# 1st iteration : x=1, y=2 =>1*2=2
# 2nd iteration : x=2, y=3 =>2*3=6
# 3nd iteration : x=6, y=4 =>6*4=24
# 4th iteration : x=24, y=5 =>24*5=120

#Create a lambda finction to calculate the cube of a number
#input : 3 
# output : 27

# cube = lambda x : x**3 
# print(cube(3))

#Create a lambda function to reverse a string
#input : python 
#output : nohtyp

# rev = lambda x : x[::-1]
# print(rev('python'))

#write a lambda function to check if a number is a palindrome
#input : 121
#output : True

# str = input('Enter a number to check...')
# rev = lambda x : x[::-1]
# print(rev(str)==str)


# Use a lambda function to create a list of squares for numbers 1 through 10.
#  Expected Output: [1, 4, 9, ..., 100]

# lst = list(map(lambda x : x**2 ,range(1,11)))
# print(lst)
#1st iteration x=1 --[1]
#1st iteration x=2 --[1,4]
#1st iteration x=3 --[1,4,9]


# Filter out all prime numbers from a list.
# Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Output: [2, 3, 5, 7]

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# res = list(filter(lambda x : x if not any(x % i == 0 for i in range(2,x))))
# print(res(lst))

# def is_prime(num) :
#     if num < 2 :
#         return False# 1
#     for i in range(2, num) :
#         if num % i==0 :
#             return False# 4,6,8,9,10
#     return True# 2,3,5,7
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# prime_numbers=list(filter(is_prime,nums))
# print(prime_numbers)

#Write  a program to remove a dublicates in list while maintaining  the order 
# input : [1,2,3,4]
# output : [1,2,3,4]
# lst = [1,2,3,4,4]
# new = []
# for i in lst:
#     if i not in new:
#         new.append(i)
# print(new)
# or
# print(list(dict.fromkeys(lst)))
res=[]
for i in range(1,1001):
    if i%7==0 and i%5!=0:
        res.append(i)
print(res)
# or 
print(list(filter(lambda i : i%7==0 and i%5!=0,range(1,1001))))