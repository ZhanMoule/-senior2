# -*- coding: utf-8 -*-
"""
Spyder Editor
created 2023/3/17
字符串qiuzhen

This is a temporary script file.
"""
s=input("请输入字符串")
s1=input("请输入子串")
a=len(s1)
for i in range(len(s)):
    if s1[0]==s[i]:
        b=s[i:i+a]
        if b==s1:
            print(s1,"为的子串")
    else:
        print("不是子串哦")
        
