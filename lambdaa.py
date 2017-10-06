from functools import reduce
add = lambda x,y: x+y
sub = lambda x,y: x-y

print(str(add(1,10)))



'''
Map function
'''
#new_sequence = map(function, iterables) #iterables meaning lists, dictionaries etc

items = [2,3,4,5,6]
square_list = map(lambda x: x**2,items)
#print(list(square_list))



words = ['Hey', 'Nice meeting you', 'Goodbye']
a = map(lambda x: x + ' Jude', words)
#print(list(a))


'''
filter
'''

# new_sequence = filter(predicate,iterables)
#predicate = function that returns a condition


number_list = [1,-2,3,-4,5]
positive_list = filter(lambda x: x>0, number_list)


names = ['John', 'Jeremy','Mark','Aaron','Jules','James','Kurt']
newList = filter(lambda x: x[0]=='J', names)
newList2 = filter(lambda x: x[0]!='J', names)




#sequence = reduce(function, iterables)


numbers = [1,2,3,4,5,6]
product = 1
for element in numbers:
    product*=element

'''
reduce
'''

mul = reduce(lambda x,y: x*y, numbers)
#what happens is ((((1*2)*3)*4)*5)*6)





a = ['Hello ', 'darkness ', 'my ', 'old ', 'friend']

newList = reduce(lambda x,y: x+y, a)
print(newList)



'''List Comprehensions'''
#Another way to define lists in python
#more elegant(???)
#easier to understand than lambda functions

number_list = [1,-2,3,-4,5]

positive_list = [number for number in number_list if number>0]
#print(positive_list)



items= [2,3,4,5,6]
square_list = [item*item for item in items]
print(square_list)
gluck = "Goodluck "
goodluck_list = [gluck + name for name in names]
print (goodluck_list)

#pwede ring a = [f'Goodluck {name}' for name in names if names[0] =='J']
#etc
