# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 15:38:31 2023
回文字符串中的判断写成自定义函数
1.输出所有的回文子串
2.输出最长的回文子串
3.将s看成循环字符串，在环中查找最长的回文子串
@author: Moule
"""
s=input(' input a string:')
n=len(s)
a=[];b=[];c=[]


def sb(a):
    for i in range(len(s)):
        if a==a[::-1]:
            return True
        else:
            return False
maxlen=0       
for i in range(len(s)): #左边界
    for j in range(2,len(s)+1-i): #取长度
        if sb(s[i:i+j]):
            print(s[i:i+j])
            if len(s[i:i+j])>maxlen:
                maxlen=len(s[i:i+j])
                maxstr=s[i:i+j]
print("最长子串"+s[i:i+j])        
print("最长回文串"+str(maxlen))        
        


        

