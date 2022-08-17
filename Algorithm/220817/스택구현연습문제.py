stackSize = 10
stack = [0] * stackSize
top = -1

top += 1         # push(1)
stack[top] = 1

top += 1         # push(2)
stack[top] = 2


top -= 1
temp = stack[top+1]
print(temp)

temp = stack[top]
top = -1
print(temp)

