#栈
x=[6,8,9]
print(x)
x.append(12)#使用appe添加元素到栈顶端
print(x)
x.pop()#栈顶部取出元素用pop
print(x)
#队列
from collections import deque
x=deque([7,8,9])
print(x)
x.append(54)
print(x)
x.popleft()
print(x)
