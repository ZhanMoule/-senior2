#删除k个字符后，构成的最小的字符串，剩余字符相对位置不变
#如'a3b3e4'，删除3个字符后，最小的字符串为'334c'
#PS:可以输出每一步结果，跟踪删除过程

s=input(' input a string（ASCII）:')
k=int(input('删除个数k（小于s长度）:'))
t=k
while t>0:
    
