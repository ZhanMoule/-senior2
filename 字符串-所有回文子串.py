def is_hw(s):
    if s==s[::-1]:
        return True
    else:
        return False
    
#输出所有回文子串，要求长度不为1
s='afsdfgfdsadasdf' #input(' input a string:')
n=len(s)
hws=[]
for i in range(n):#左边界
    for j in range(i+2,n+1):#右边界
        if is_hw(s[i:j]) :
            hws.append(s[i:j])
print(hws)

for i in range(n): #左边界
    for j in range(2,n+1-i): #取长度
        if ishw(s[i:i+j]):
            print(s[i:i+j])