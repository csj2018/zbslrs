from perform import *
i = int(input('输入循环次数:'))
result = perform(i)
a = result.count(1)#lang
b = result.count(2)#min
c = result.count(3)#shen
print('游戏共循环%d次，好人胜利%d次，屠民%d次，屠神%d次。'%(i, a, b, c))