class Stack():
    def __init__(self):
        self.list_elements = []

    def isEmpty(self): #проверка стека на пустоту. Метод возвращает True или False.
        if len(self.list_elements) == 0:
            return True
        else:
            return False

    def push(self, something): #добавляет новый элемент на вершину стека. Метод ничего не возвращает.
        self.list_elements.append(something)

    def pop(self): #удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
        pop = self.list_elements.pop(-1)
        return pop

    def peek(self): #возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
        return self.list_elements[-1]

    def size(self): #возвращает количество элементов в стеке.
        return len(self.list_elements)

    def allElements(self):
        return self.list_elements

New_Stack = Stack()
New_Stack.push('Бэтмен')
New_Stack.push('Спайдермен')
New_Stack.push('Олень')
New_Stack.push('Черепица')
print(New_Stack.peek())
print(New_Stack.pop())
print(New_Stack.peek())
print(New_Stack.size())
print(New_Stack.isEmpty())
print(New_Stack.allElements())