from Stack import Stack

New_Stack = Stack()
str_0 = '(((([{}]))))'
str_1 = '}{}'
str_2 = '[([])((([[[]]])))]{()}'
str_3 = '{{[(])]}}'

def isbalance(str: str):
    open_stack = Stack()
    close_stack = Stack()
    if len(str) % 2 == 0: #Если количество элементов строки нечетное, значит последовательность несбалансированная
        for symbol in str:
            if symbol in ['(', '[', '{']:
                open_stack.push(symbol)
            else:
                close_stack.push(symbol)
        print(open_stack.allElements())
        print(close_stack.allElements())
    else:
        return 'Несбалансированно'

if __name__ == '__main__':
    print(isbalance(str_2))
    # print(isbalance(str_1))
    # print(isbalance(str_2))
    # print(isbalance(str_3))
