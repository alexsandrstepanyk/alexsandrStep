from typing import List

int_list = [1, 2, 3]
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
names1.append('wolia')  # plus new element for this list
names2.append('mila')
print(names2 + names1)
popped = names1.pop()  # del  first element for this list
print(popped)
print(names1)
names1.pop(1)  # del index element for this list
print(names1)
names1.sort()
print(names1)
names1.append('igor')
print(names1)
letter = ['ac', 'ab', 'aa']  # sort this list
letter.sort()
print(letter)
letters = ['abcd', 'abc', 'ab', 'a']
letters.sort(key=len)
print(letters)
numbers = [3, 2, 8, 9, 0, 5, 4, 3, 2, 1]
numbers.sort()
print(numbers)
yers: list[int] = [2000, 1900, 2001, 1994, 1993, 2021]
yers.sort()
print(yers)
yers.reverse()  # sort revers
print(yers)
yers.sort(reverse=True)  # sort down
print(yers)
yers.insert(3, 1988)  # add new certain element
print(yers)
print(yers.count(2000))
