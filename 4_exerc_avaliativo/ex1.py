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

    def Get(self, i):
        if self.isEmpty():
            raise Exception("Lista vazia")
        if i < 0 or i > self.count:
            raise Exception('Posição inválida')
        if i == self.count:
            return self.final.item  # último nó é sempre self.final
        else:
            aux = self.final.next   # começa do início
            pos = 0
            while pos < i:          # avança até a posição i
                aux = aux.next
                pos += 1
            return aux.item
        

    def InsertAt(self, p, newItem):
        if p < 1 or p > self.count + 1:
            raise Exception('Posição inválida')

        if p == 1:
            self.AddFirst(newItem)  

        elif p == self.count + 1:
            self.AddLast(newItem)   

        else:
            
            aux = self.final.next
            for i in range(1, p - 1):
                aux = aux.next

            newNode = Node(newItem, aux.next)
            aux.next = newNode
            self.count += 1



    def Display(self):
        
        aux = self.final.next
        for i in range (self.count):
            print(aux.item, end=' ')
            aux = aux.next
        print('\n')


def main():
    
    x = CircularLinkedList()
    opcao = 0

    while opcao != 10:
        print("------ Menu de Opções -----")
        print()
        print("[1] - Adicionar elemento no inicio.")
        print("[2] - Adicionar elemento no final.")
        print("[3] - Inserir elemento em uma posição.")
        print()
        print("[4] - Remover elemento do inicio.")
        print("[5] - Remover elemento do final.")
        print("[6] - Remover elemento por valor.")
        print()
        print("[7] - Consultar elemento por posição (Get).")
        print("[8] - Alterar elemento por posição (Set).")
        print()
        print("[9] - Mostrar a lista.")
        print("[10] - Encerrar.")
        print()

        opcao = int(input("Informe a opção desejada: "))

        if opcao == 1:
            item = int(input("Informe o valor a ser inserido no início: "))
            x.AddFirst(item)
            print(f"Elemento {item} inserido no inicio.")

        elif opcao == 2:
            item = int(input("Informe o valor a ser inserido no final: "))
            x.AddLast(item)
            print(f"Elemento {item} inserido no final")

        elif opcao == 3:
            pos = int(input("Informe a posição de inserção: "))
            item = int(input("Informe o valor a ser inserido: "))
            x.InsertAt(pos, item)
            print(f"Elemento {item} inserido na posicao {pos} ")

        elif opcao == 4:
            x.RemoveFirst()
            print("Primeiro elemento removido")

        elif opcao == 5:
            x.RemoveLast()
            print("Ultimo elemento removido")

        elif opcao == 6:
            item = int(input("Informe o valor a ser removido: "))
            resultado = x.Remove(item)
            if resultado:
                print(f"Elemento {item} removido")
            else:
                print(f"Elemento {item} não encontrado na lista.")

        elif opcao == 7:
            pos = int(input("Informe a posição a ser consultada: "))
            item = x.Get(pos)
            print(f"Elemento na posição {pos}: {item}.")

        elif opcao == 8:
            pos = int(input("Informe a posição a ser alterada: "))
            item = int(input("Informe o novo valor: "))
            x.Set(pos, item)
            print(f"Posição {pos} alterada ")

        elif opcao == 9:
            if x.isEmpty():
                print("Lista vazia")
            else:
                x.Display()

        elif opcao == 10:
            print("Encerrando...")
            break

        else:
            print("Opção inválida!")

main()


