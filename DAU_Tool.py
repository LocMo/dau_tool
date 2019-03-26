#encoding=utf-8  
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#自定义函数 e指数形式
def func(x, a, b):
    return a*pow(x,b)

#输入二维数组的行数
print("待输入的数据行数:")
n = int(input())        
#初始化二维数组
line = [[0]*2]*n  
print("留存天数 n日留存率（直接复制excel）")      
for i in range(n):
	#输入二维数组，同行数字用空格分隔，不同行则用回车换行

    line[i] = input().split("\t")

#数组类型转换
for j in range(len(line)):
	line[j] = list(map(float,line[j]))


#定义x、y散点坐标
data =  np.array(line)
x = np.array(data[:,0])
y = np.array(data[:,1])



#非线性最小二乘法拟合
popt, pcov = curve_fit(func, x, y)
#获取popt里面是拟合系数
a = popt[0] 
b = popt[1]
print(a)
print(b)

#计算DAU
print("请输入累计天数：")
day = int(input())
print("请输入预计每日新增(W)")
new_user = float(input())
r = 0
print("----------这里是分割线----------")
print("0\t%f" % (new_user))
for d in range(1,day):
	r = r + a * pow(d,b)
	n_dau = (1 + r) * new_user
	print("%d,%f" % (d,n_dau))
'''
dau = (1 + r) * new_user
print("预期DAU(W)")
print(round(dau,2))


#计算第n天留存率（校验数据）--2018.9.25
print("请输入留存天数：(1=次日)")
check = int(input())
check_result = a * pow(check,b)
check_print = "第(%d)日留存率预估值为(%f)" % (check,check_result)
print(check_print)
'''



