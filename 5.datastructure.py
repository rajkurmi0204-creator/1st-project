"""data structure (advance data type)"""

# 1. list 
# 2. dictionary
# 3. tuples
# 4. set



"""#1. list, denoted by -> [] square bracket"""

""" 1. hetrogenous data structure = multiple types ke data ko store krwa skte h.
    2. duplicacy allowed
    3. list is order
    4. mutable -> we can change the value of the item in list"""


# l = [] empty list

# l = [10,20,30,40,50]
# print(l)
# print(type(l)) 


# l= [12,34,4,2,62]
# print(l)
# print(type(l))


# l = [10,20,30,40,50]
# print(l[3])            # item at index


# l = [12,23,24,25,16]
# print(l[4])



"""item assingment"""


# l = [10,20,30,40,50]
# l[3] = 400     
# print(l)


# l = [12,13,133,122,14]
# l[2] = 4
# print(l)

# l[5] = 100    # index out of range



"""item wise loop"""   # i means indexx ke number jo pr jo bhi item number h usko print krta h


# l = [10,20,30,40,50]
# for i in l:
#     print(i)


# l=[13,1,3,23,42,4]
# for i in l:
#     print(i)



"""index wise loop"""


# i -> index of list       list me number konse index number par h ye batata h, list ke numbers ki indexing value batata h.
# l[i] -> item at index    index ke number pr konsa element number h uski value deta h.


# l = [10,20,30,40,50]
# for i in range(len(l)): 
#     print(i, l[i])


# l =[1,67,10,25,14,77]
# for i in l:
#     if i >15:
#         print(i)    
       

# l = [1,67,10,25,14,77]
# for i in range(len(l)):
#     if l[i] >15:
#         print(i)



"""sum all the elements of the list"""


# l = [10,20,30,40,50]
# sum = 0
# for i in l:
#     sum += i
# print(sum)    
  

# l = [2,4,6,8,10]
# sum = 0
# for i in l:
#     sum +=i
#     print(sum)



"""slicing
[start=0;stop-1;step=1]"""

# l = [10,20,30,40,50]



"""methods in list"""


"""# 1.  .append()"""          # = adding element at the last of list, but append only accept one value

# l = [10,20,30,40,50]
# l.append(100)
# print(l)


"""# 2. .extend()"""

# l1 = [10,20,30,40,50]
# l2 = [60,70,80]
# l1.extend(l2)
# print(l1)


"""# 3. .insert(index,value)"""          # = add value in the list , index type krne prr value add krta h

# l1 = [10,20,30,40,50]
# l1.insert(1,100)
# print(l1)


"""# 4. .pop() """          # = remove value in the list, but remove only one value, index type krne prr value remove krta h

# l1 = [10,20,30,40,50]
# l1.pop(1)
# print(l1)


"""# 5. .remove (element)"""

# l1= [1,5,5,5,2,3,4,5]
# l1.remove(5)             # = agr duplicate value h toh first vlaue remove
# print(l1)


"""# 6. len()"""           # = list length

# l1 = [1,5,5,5,5,2,3,4,5]
# print(len(l1))


"""# 7. bubble sort"""

# l = [1,5,3,7,4,10]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]>l[j]:
#             l[i],l[j] = l[j],l[i]
# print(l)   


"""# enumerate = list = [10,20,30,40,50] = index = 0,1,2,3,4 """
"""# enumerate = index ke sath unki values bhi dega. """

# l = [10,20,30,40,50]
# # for index ,value in enumerate(l):
# #     print(index,value)
# for index, value in  enumerate(l):
#     print(index+1, value)



"""questions"""


"""# 1. Accept List elements and reprint it"""

# n = int(input("entre the size of the list:"))
# l = []
# for i in range(n):  # 0,1,2,3,4
#     element = input(f" entre element {i} for your list:")
#     l.append(element)
# print(l)    


"""# 2. Print positive and negative elements of an List"""

# l = [10,-9,20,30,-12,-15]
# neg = []
# pos = []
# for i in l:
#     if i <0:
#         neg.append(i)
#     else:
#         pos.append(i)
# print(neg)
# print(pos)            
                  

"""# 3. reverse the list without using slicing"""

# l = [10,20,30,40,50]
# rev_l= []
# for i in range(len(l)-1,-1,-1): 
#     print(l[i])


"""# 4. Find the greatest element and print its index too."""        

# l = [2,96,69,77,145,20]
# max =l[0]  #2
# index = 0
# for i in range(len(l)):
#     if l[i] > max:
#         max = l[i]
#         index = i
# print(f"max element from the list is {max} and at index {index}")    


"""# 5. average  of List elements."""

# l = [1,5,6,8,9]
# sum =0
# for i in l:
#     sum = sum +i
# print(sum/len(l))   


"""# 6. pallindrome list."""

# l = [1,2,2,1]
# for i in range(len(l)):
#     if l[i]!=l[len(l)-1-i]:
#         print("list is not pallindrome")
# else:
#     print("list is pallindrome")
    

"""#7. check list is sorted."""

# l=[5,10,15,20]
# for i in range(1,len(l)-1):
#     if l[i]>l[i-1]:
#         print(f"the list is sorted")
#         break
#     else:
#         print(f"the list is not sorted")
#         break



""" 2. Dictionary , keys - values pair ,
keys cannot be duplicate but values can be duplicate ,
# {} = curly bracket """   

""" 1. hetrogeneous
    2. mutable
    3. ordered """


# d = {'a':10, 'b':20, 'c':30, 'd':40}
# print(d['b'])


# d= {'a':10, 'b':20, 'c':30, 'd':40}
# d['e'] = 100                                #  creating a new key and assigning  value to it
# print(d) 


# d= {'a':10, 'b':20, 'c':30, 'd':40, 'e':100}
# d['e'] = 200                                  #  old value at key 'e' will be overwrite
# print(d) 


# info = {'name': 'rahul', 'age': 21, 'marks':50.25, 'present': True}
# info['age'] = 25                                # item assignment
# print(info)       



"""methods in dictionary"""


"""# 1. .values () """                                                   # sirf dictionary ki values

# info = {'name': 'rahul', 'age': 21, 'marks':50.25, 'present': True}
# print(info.values())


"""# 2. .keys () """                                                     # sirf dictionary ki keys milegi

# info = {'name': 'rahul', 'age': 21, 'marks':50.25, 'present': True}
# print(info.keys())


"""# 3. .items ()"""

# info = {'name': 'rahul', 'age': 21, 'marks':50.25, 'present': True}
# print(info.items())


"""# 4. .pop() """                                                       # it accepts key and will remove key and values

# info = {'name': 'rahul', 'age': 21, 'marks':50.25, 'present': True}
# info.pop("name")
# print(info) 


"""# 5. .get()"""            # gives you value of a key and if not present gives you none

# d ={'a':10, 'b':20, 'c':30}
# print(d.get('a'))


"""# 6. .update ({key :value})"""

# d ={'a':10, 'b':20, 'c':30}
# d.update({'c':500})
# print(d)


"""# 7. .clear() """         # remove all elements

# d = {'a':100, 'b':200, 'c':300}
# d.clear()
# print(d)


"""# 8. del d"""             # its a key word

# d = {'a':100, 'b':200, 'c':300}
# d.clear()
# print(d)
# del d


"""# 9. print(len(info))   jitni keys utni length"""

# info = {'name': 'rahul', 'age': 21, 'marks':50.25, 'present': True}
# print(len(info)) 


# info = {'name': 'rahul', 'age': 21, 'marks':50.25, 'present': True}
# for i in info:                                                         # i = keys
#     print(i,info[i])                                                   # info [i] = values 


# info = {'name': 'rahul', 'age': 21, 'marks':50.25, 'present': True}
# for i in info.values():                                                # only get values from dictionary
#     print(i)



""" question """


""" # 1. we have two lists and we have to make list1 as key and list2 as values merge both list into a dictionary in values and kye .  """

# l1 = ['a', 'b', 'c', 'd']
# l2 = [10, 20, 30, 40]
# d= {}
# for i in range(len(l1)):     #i 0123
#     d[l1[i]] = l2[i]
# print(d) 
  

"""# 2. you have a list make the index as the keys and element present on those indexs as values """

# l = [10,20,30,40,50]
# d={}
# for i in range(len(l)):
#     d[i]=l[i]
# print(d) 
     

"""# 3. merge 2 dictionaries"""

# d1 = {'a':10, 'b':20}
# d2 = {'c':30, 'd':40}
# for i in d2:
#     if i not in d1:
#         d1[i] = d2[i]
# print(d1)             


"""#4. frequency count """

#l = [1,1,1,2,2,3,3,6,6,7,6,3,4,1,2]
# d = {}
# for i in l:
#     if i not in d:
#         d[i]= 1
#     else:
#         d[i] = d[i] +1
# print(d)      
      

"""#5. you have a list [1,2,3,4,5] and you have a variable k =2 and you just have to rotate the list by k elements."""    

# l = [1,2,3,4,5]
# k = 2
# for i in range(k):
#     last = l[-1]          # storing last value of the list 
#     for j in range(len(l)-1,0,-1):
#         l[j] = l[j-1]                     
#     l[0] = last
# print(l)    

# l = [1,2,3,4,5]
# k = 2
# k = k % len(l)
# rotate = l[-k:] + l[:-k]
# print(rotate)


""" #3. sets 
    empty set = {}
    #1. values can duplicate in dictionary but not in set 
    #2. sets are unordered or subscriptable 
    #3. hetrogeneous
    #4. mutable """


# s = {1,2,3,4,5}
# print(type(s))


# s = {1,1,2,3,4,5,5}
# print(s) 


# s = {'hello', 1,3.14,True}
# print(s)



""" methods in set """


"""#1. add a new value in set
# item adding"""

# s ={1,1,1,2,2,3,3,4,4,5,5}
# s.add(100)
# print(s)


# s ={1,1,1,2,2,3,3,4,4,5,5}
# s.add(100)
# s.update ([100,200,300,400])        # adding multiple values inside set
# print(s) 


"""#2. removing an element from set
#1 .remove (element)"""

# s ={1,1,1,2,2,3,3,4,4,5,5}
# s.remove(1)
# print(s)


# s ={1,1,1,2,2,3,3,4,4,5,5}
# s.remove(1)
# s.discard(6)                   # agr value exist nhi krti toh it will return you exact set bina kisi error ke.
# print(s) 


"""#3. clear()"""

# s ={1,1,1,2,2,3,3,4,4,5,5}
# s.clear()                        # sab hata dega ye
# print(s)



""" advanced mrthods in sets """

"""#1. .union = sare elements between your sets"""
"""#2. .intersection = dono set ke bech mai jo common values 
   #3. difference
   #4. symmetric difference """


# s1 = {1,2,3,4,5}
# s2 = {1,6,7,8}
# print(s1.union(s2))


# s1 = {1,2,3,4,5}
# s2 = {1,6,7,8}
# print(s1.intersection(s2))


# s1 = {1,2,3,4,5}
# s2 = {1,6,7,8}
# print(f'union of set1 and set2 is {s1.union(s2)}')
# print(f'intersection of set1 and set2 is {s1.intersection(s2)}')





# l=[5,10,15,20]
# for i in range(1,len(l)-1):
#     if l[i]>l[i-1]:
#         print(f"the list is sorted")
#         break
#     else:
#         print(f"the list is not sorted")
#         break