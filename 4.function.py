"""function"""  
 # fuction start name with 'def'
   

# def mahi ():
#     print("hello") 

# mahi()    


# def show():
#     print("hello")
# x=show()
# print(x)


# def python():
#     print("welcome to my python class")

# python()    


# def marks(name, mark):
#     print("result",name,mark)
# marks("raj",90)    


# def school():
#     print("in mock test marks","=","raj kurmi","=","age=19","marks","=",97)
# school() 


# def mark(name,mark):
#     print(name,mark)
# mark("raj",98) 



"""addition, subtraction, muliplication. methods """


#def add (a,b):    # fuction define krte waqt parameters.
#     print(a+b)
# add(10,20)       # function call krte waqt arguments.   


# def addition(a ,b):
#     print(a+b) 
# addition(10,20)    


# def subtraction(a,b):
#     print(a-b)
# subtraction(30,10)


# def multi(a,b):
#     print(a*b)
# multi(10,20)    

  

"""return function methods"""


# def demo():
#     print("a")
#     return
#     print("b")
# demo()


# def name():
#     print("raj")
#     print("yash")
#     return
#     print("anuj")
# name()    


# def add(a,b):
#     return a+b
# print(add(5,4)+2)


# def add(a,b):
#     return a+b
# raj = add(10,5)
# print(raj)    


# def add(a,b):
#     return a+b
# ans = (add (5,3)+2)
# print(ans)


# def minus(a,b):
#     return a-b
# raj= (minus(15,7)-2)
# print(raj)


# def add(a,b):
#     return a+b
# result = add(10,5)
# print(result-5)


# def multi(a,b):
#     return a*b
# print(multi(3,4)*2)


# def add(a,b=5):
#     return a+b
# print(add(10,20))


# def add(a,b=5):
#     return a+b
# print (add(10))


# def show ():
#     return "helo" 
# print(len(show()))



"""type hiting"""
# accept an parameter named as 'n' and print factorial of 'n' using function.
 


# def factorial(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact = fact*i 
#     return fact                #shorthand operator
# print(factorial(5)) 



"""def greet(n):
    multi=1
    for i in range(1,n+1):
        multi= multi*i
    return multi
print(greet(3))"""



"""keyword agruments"""


# def info(name,gender,age,address):
#     print(name)
#     print(gender)
#     print(age)
#     print(address)
# info(name="mukesh", gender="m", age=52, address="bhopal")   


# def info(name , gender , age):
#     print(name,gender,age) 
# info(name="raj", gender="m", age=19)        
  


"""def function pallendrome"""
# check if a number is pallendrome or not using keyword argument

# def pallendrome(num):
#     copy = num
#     rev =0
#     while num>0:
#         last = num% 10
#         rev = rev *10 + last
#         num//=10
#     if copy ==rev:
#         print(f"{copy} ,is a pallendrome") 
#     else:
#         print(f"{copy} ,is not pallendrome")    
# pallendrome(121)
              


"""recursion"""


# def display(num):  #num=1
#     if num > 10:
#        return  
#     print(num)                                       
#     display(num+1)  # function calling itself
# display(1) 


# def raj(n):
#     if n>10:
#         return  
#     print(n)
#     raj(n+1)
# raj(1)     


# def display(num):  
#     if num < 1:
#        return
#     print(num)
#     display(num-1)  
# display(10)    



"""factorial using recursion"""


# def factorial(num):
#     if num==0 or num==1:
#         return 1
#     else:
#         return num * factorial (num-1)
# print(factorial(5))                       
 


# lamda, args, kwargs







