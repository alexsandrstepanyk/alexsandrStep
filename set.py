my_set = set()
print(my_set)
print(type(my_set))
my_set.add(1)
print(my_set)
my_set.add(2)
print(my_set)
my_set.add(3)
print(my_set)
my_list = [1,1,1,1,2,2,2,2,3,3,3,3,4]
s = set(my_list)
print(s)

print(1 in s)
print(5 in s)
set1 = {1,2,3,4}
set2 = {1,2,3,4,5}
print(set1.issubset(set2))# check for double element
print(set2.issubset(set1))
print(set2.issuperset(set1)) # надмножиство суперсета

set3={1,2,3}
set4={4,5,6}
print(set3.isdisjoint(set4))# перевірка чи  різні елементи в сетах
set5= {1,3,4}
set6= {1,3,4}
print(set5.isdisjoint(set6))# перевірка чи  різні елементи в сетах
a=9-3
c=9-3
d=9-3
set7= {a,c,d}
set8= {a,c,d}
print(set8.isdisjoint(set7))# перевірка чи  різні елементи в сетах
print(set7)
set9 = {1,2,3,4,5}
set10 = {5,6,7,8,9}
set11 = set9.union(set10)# обэднання з двох елементыв в наступне множиство
print(set11)
set11 = set9.intersection(set10)# вивід суміжних елементів сету
print(set11)
set11 = set9.difference(set10)# вивід протележних елементів сету, які відсутні в перщшрму сеті
print(set11)
set11 = set9.symmetric_difference(set10)# вивід протележних елементів сету з двох сетів
print(set11)
print(set9)
set9.update(set10)# обєднати сети без повфторюючих елементів
print(set9)
set9.remove(1)#delete element
print(set9)
set9.discard(2)#delete element
print(set9)
popped_out_element = set9.pop()# delete element vibirkovo
print(popped_out_element)
print(set9)
set15 = set9.copy()
print(set15)
set15.clear()
print(set15)