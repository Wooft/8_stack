class Stack():
    def __init__(self):
        self.list_elements = []
        self.element = {
            "id": 0,
            "Element": None,
            "href_id": 0
        }

    def add(self, something):
        self.element["id"] += 1
        self.element["Element"] = something
        self.element["href_id"] = self.element["id"] - 1
        self.list_elements.append(self.element)

    def isEmpty(self): #проверка стека на пустоту. Метод возвращает True или False.
        pass

    def push(self): #добавляет новый элемент на вершину стека. Метод ничего не возвращает.
        pass

    def pop(self): #удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
        pass

    def peek(self): #возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
        return self.list_elements[-1]

    def size(self): #возвращает количество элементов в стеке.
        pass

New_Stack = Stack()
New_Stack.add('Бэтмен')
New_Stack.add('Спайдермен')
New_Stack.add('Олень')
New_Stack.add('Черепица')

print(New_Stack.peek())
