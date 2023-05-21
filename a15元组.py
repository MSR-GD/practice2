#元组不能增删改
#元组的创建
t = ('Python','qqq','qwe')
print(t)
print(type(t))

t1 = tuple(('qwe','asd'))
print(t1)
print(type(t1))

t2 = 'qwe','ewq'
print(t2)
print(type(t2))

#如果元组只有一个元素要加逗号

t3 = ("qwe",)
print(t3)
print(type(t3))
print()
t4 = ()
print(t4)

t5 = (10,[20,30],5)
print(t5)
print(type(t5))
for i in range(3):
    print(t5[i],type(t5[i]),id(t5[i]))
t5[1].append(33333)
for i in range(3):
    print(t5[i],type(t5[i]),id(t5[i]))

for i in t5:
    print(i)