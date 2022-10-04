from Stack import Stack

New_Stack = Stack()
str = '(((([{}]))))'
for symbols in str:
    New_Stack.push(symbols)

for elements in New_Stack:
    print(elements)
