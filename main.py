from Stack import Stack

str = '(((())))'
str_1 = '(())))'
str_2 = '(((([{}]))))'
str_3 = '{{[(])]}}'

def isbalance(str: str) -> str:
    openstack = Stack()
    closestack = Stack()
    if len(str) % 2 == 0: #Проверка. Если количество элементов строки - нечетное, значит она несбалансирована
        for element in str:
            if element in ['[','{','(']: #Если элемент - открывающая скобка, добавляем её в открывающий стак
                openstack.push(element)
            else: #Если нет, то обрабатываем исключение
                closestack.push(element) #Добавляем элемент во второй стак.
                if openstack.isEmpty() == True: #Проверяем если открывающий стак пуст - возвращаем значение "Несбалансировано"
                    return 'Несбалансировано'
                if openstack.peek() == '(' and closestack.peek() == ')' or openstack.peek() == '[' and closestack.peek() == ']' or openstack.peek() == '{' and closestack.peek() == '}' : #Проверяем, если последние элементы стаков - парные скобки
                    openstack.pop()
                    closestack.pop() #удаляем оба элемента
        if openstack.isEmpty() == True and closestack.isEmpty() == True:
            return 'Сбалансировано'
        else:
            return 'Несбалансировано'
    else:
        return 'Несбалансировано'

if __name__ == '__main__':
    print(isbalance(str))
    print(isbalance(str_1))
    print(isbalance(str_2))
    print(isbalance(str_3))