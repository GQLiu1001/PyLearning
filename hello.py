# 列表 List [] 可变序列
a =[1,3,5,2]
b = sorted(a)
print('b:', b )
# a[0] a[1]...
# 序号从2到4 左闭右开 [2,4)
c =a[2:4]
print('c:',c)
# list[start:end:step] step绝对值大小为步长 正负号决定方向
print('len(a):',len(a))
print('len(c)',len(c))
# 元组：只读数组 不可变序列
tup = (1 , 2 , 3)
print('tup:', tup)
# 字典 字符串 一个存Map集合的List集合
dic = {'a':'b','c':3}
print('dic的a对应的值:',dic['a'])
# 函数 def
def return_max(num1,num2):
    if num1 > num2:
        return num1
    else:
        return num2

d=5
f=9
c=return_max(d,f)
print(c)

