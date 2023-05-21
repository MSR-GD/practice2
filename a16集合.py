s = {1,2,3,4,4,5,6,7,7}
print(s)
print(type(s))
s = set(range(6))
print(s)

s = set([1,2,3,4,5,5,6,7,7])
print(s,type(s))

s = set((1,2,3,3,5,66))
print(s)

s = set('Python')
print(s)

s = set({12,4,34,55,66,44,4})
print(s)

s = set()
print(s,type(s))

s1 = {10,20,30,404,51}
'''集合的判断操作'''
print(10 in s1)
print(10 not in s1)
'''集合的增操作'''
s1.add(33)
s1.update({77,23,41})
print(s1)
s1.update([23,21])
s1.update(('qwe'))
print(s1)
'''集合的删操作'''
s1.remove(33)
s1.pop()
s1.discard(21)
print(s1)
s1.clear()
print(s1)

s2 = {10,20,30,40}
s3 = {10,20,30,40}
print(s2 == s3)
print(s2 != s3)
'''是否是子集关系'''
s4 = {10,20,30}
s5 = {10,50}
print(s2.issubset(s4))
print(s2.issubset(s5))
print(s4.issubset(s2))
'''是否是超集关系'''
print(s2.issuperset(s4))
print(s2.issuperset(s5))
'''是否是交集关系'''
print(s2.isdisjoint(s3))
#没有交集为True