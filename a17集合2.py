s1 = {10,20,30,40}
s2 = {20,30,40,50,60}
#交集
print(s1.intersection(s2))
print(s1 & s2)
#并集
print(s1.union(s2))
print(s1 | s2)
#差集
print(s1.difference(s2))
print(s1 - s2)
#对称差集
print(s1.symmetric_difference(s2))
print(s1^s2)

#集合生成式

s = {i * i for i in range(10)}
print(s)