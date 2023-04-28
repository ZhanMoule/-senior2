# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 14:14:31 2023
输出字符串中所有子串
@author:Moule


for i in s:
    print(i)
for j in s:
    for q in range(len(s)):
        print(j+s[q])"""
        
s=input("请输入字符串")
for i in range(0,len(s)):
    for j in range(i+1,len(s)+1):
        print(s[i:j])
    
    