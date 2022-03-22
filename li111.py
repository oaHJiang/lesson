'''
f=open('file.txt','r')
print(f.closed)
f.close()
print(f.closed)
'''
'''
with open('file.txt','r') as f:
    print(f.closed)
print(f.closed)
'''
#file.name
#file.mode
#file.encoding
#file.closed
with open('file.txt','r') as f:
    print(f.name)
    print(f.mode)
    print(f.encoding)
    print(f.closed)
print(f.closed)

