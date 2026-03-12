class Node:
    def __init__(self,newItem,nextNode):
        self.item = newItem
        self.next = nextNode

class CircularLinkedList:
    def __init__(self):
        self.final = None
        self.count = 0
    
    def AddFirst(self,newItem):
        #cria o novo no para conter o item
        newNode = Node(newItem,None)

        if not self.isEmpty():
            newNode.next = self.final.next
            self.final.next = newNode
        else:
            newNode.next = newNode # 1 elemento
            self.final = newNode
        
        self.count += 1

    def AddLast(self,newItem):
        self.AddFirst(newItem)
        self.final = self.final.next

    def isEmpty(self):
        return self.final == None

    def RemoveFirst(self):
        if self.isEmpty():
            raise Exception('Lista vazia')
        
        if self.count >=2:
            self.final.next = self.final.next.next
        else:
            self.final = None
        
        self.count -= 1

    def RemoveLast(self):
        if self.isEmpty():
            raise Exception("lista vazia")
        
        if self.count == 1:
            self.final = None
        else: 
            #percorre os nos ate atingir o ultimo no
            aux = self.final.next
            for i in range(0,self.count-2):
                aux = aux.next

            aux.next = aux.next.next
            self.final = aux

        self.count -= 1

    def Remove(self,item):
        if self.isEmpty():
            raise Exception("Lista Vazia")
        
        aux = self.final.next
        anterior = self.final
        while (aux != self.final and aux.item != item):
            anterior = aux
            aux = aux.next

        if (aux.item != item):
            return False
        
        if (aux == aux.next):
            self.final = None

        else:
            anterior.next = aux.next
            if aux == self.final:
                self.final = anterior 
        
        self.count -= 1
        return True

    def Get(self,i):
        if(self.isEmpty()):
            raise Exception("lista vazia")
        
        if (i > self.count):
            raise Exception ('posição invalida')
        
        if (i == self.count):
            return self.final.item
        else:
            aux = self.final.next
            pos = 1
            while (pos < i):
                aux = aux.next
                pos = pos + 1
            return aux.item
        
    def Set(self,i, newItem):
        if self.isEmpty():
            raise Exception("Lista vazia")
    
        if i > self.count:
            raise Exception("Posição inválida")

        if i == self.count:
            self.final.item = newItem

        else:
            aux = self.final.next
            pos = 1

            while pos < i:
                aux = aux.next
                pos += 1

            aux.item = newItem


    def Display(self):
        
        aux = self.final.next
        for i in range (self.count):
            print(aux.item, end=' ')
            aux = aux.next
        print('\n')

def main():
        L1 = CircularLinkedList()

        num = int(input('Informe a quantidade incial  de elementos para a fila 1:'))
        print('Informe os elementos')

        for i in range (num):
            L1.AddFirst(int(input()))

        L1.Display()
        print("Elemento na pos.1:", L1.Get(3))

main()

        