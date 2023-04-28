# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 09:27:23 2023
将一行字符串中元素进行压缩  例：>>>1110011000
                            >>>3 1 2 0 2 1 3 0
@author: Moule
"""
s=input("请输入想要压缩的字符串")
c=1
res=""
i=1
while i<len(s):
    if s[i-1]==s[i]:
        c+=1      
    else:
        res+=str(c)+" "+s[i-1]+" "
        c=1
    i+=1
res+=str(c)+" "+s[len(s)-1]
print(res)
 
