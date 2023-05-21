a = {'name':1,'name2':2}
print(a.keys())#获取键值
print(a.values())#获取值
print(a.items())#俩个都获取

print(type(a.keys()))
print(type(a.values()))
print(type(a.items()))

print(list(a.keys()))#转成列表
print(list(a.values()))
print(list(a.items()))

for i in a:
    print(i,a[i],a.get(i))

print(a)

#键值名不能重复
#键值不能改变
lst = [1,2,3]
lst.insert(1,100)
print(lst)
#d = {lst:100}
#print(d)
#字典生成式
items = ['f1','f2','f3','f4','f5']
prics = [33,22,11,15]

d = {ite:pric for ite,pric in zip(items,prics)}
print(d)