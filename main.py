from Stack import Stack

# str = '[([])((([[[]]])))]{()}'
str = '(((())))'
str_1 = '(())))'


# ['[','{','(']
# [']','}',')']

def isbalance(str: str) -> str:
    openstack = Stack()
    closestack = Stack()
    if len(str) % 2 == 0:
        for element in str:
            if element == '(':
                openstack.push(element)
            else:
                closestack.push(element)
                if openstack.peek() == '(' and closestack.peek() == ')':
                    openstack.pop()
                    closestack.pop()
        if openstack.isEmpty() == True and closestack.isEmpty() == True:
            return 'Сбалансировано'
        else:
            return 'Несбалансировано'
    else:
        return 'Несбалансировано'


if __name__ == '__main__':
    print(isbalance(str))
    # print(isbalance(str_1))