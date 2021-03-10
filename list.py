int_list = [1,2,3]
print(int_list)
len(int_list)
print(int_list[0])
var = int_list[1:]
print(int_list)
names1 = ['djon', 'bob', 'igor']
names2 = ['racy', 'joly', 'iren']
print(names2 + names1)
names1[0] = 'liam'
print(names1)
names1. append('wolia')# plus new element for this list
names2.append('mila')
print(names2 + names1)
popped = names1.pop()# del  first element for this list
print(popped)
print(names1)
names1. pop(1)# del index element for this list
print(names1)
names1.sort()
print(names1)
names1.append('igor')
print(names1)
letter = ['ac', 'ab', 'aa']#sort this list
letter.sort()
print(letter)
letters = ['abcd', 'abc', 'ab', 'a']
letters.sort(key=len)
print(letters)