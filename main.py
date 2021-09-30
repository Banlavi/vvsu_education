a = 1
print(type(a))
b=1.1
print(type(b))

c='c'
print(type(c))

o, p="hi", "g"
f=False
print(type(f))

g = a+b
print(type(g)) 

print(ord("/"))

s = input()
sl=len(s)
if sl == 1: 
    if ord(s[0]) == 47:
        print("command list")
    else: print('inc_code')
else: print('tadjik')