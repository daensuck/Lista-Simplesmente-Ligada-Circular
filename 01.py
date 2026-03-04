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

            
        