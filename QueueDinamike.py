#SHZ
# Për të ruajtur një hyrje në queue
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
# Një klasë për të përfaqësuar një queue
class Queue:
    def __init__(self):
        self.front = self.rear = None
 
    def isEmpty(self):
        return self.front == None
     
    # Shtimi i nje vlere ne queue
    def EnQueue(self, item):
        temp = Node(item)
         
        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp
        
    # Fshirja e nje vlere nga queue
    def DeQueue(self):
         
        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next
 
        if(self.front == None):
            self.rear = None
    
    # Printimi i queue
    def shfaqQueue(self):
        if self.front is None:
            print("Queue është e zbrazët!")
            return
        else:
            print("Fillimi = " + str(q.front.data)+" Fundi = " + str(q.rear.data)+"\n")
            print("Të dhënat në queue:" ,end=" ")
            n = self.front
            while n != None:
                print(n.data , end=" ")
                n = n.next
    # Kërkimi i vlerave në queue
    def kerko(self,item):
        if self.front is None:
            print("Queue është e zbrazët!")
            return
        else:
            n = self.front
            while n != None:
                if(n.data == item):
                    print(f"Vlera {item} gjindet në queue")
                n = n.next

# Kodi krysesor
if __name__== '__main__':
    q = Queue()
    choice = 0
    print("************** Queue joLinerare ******************\n")
    print("\n1. Inserto\n2. Fshijë\n3. Printoje Queuen\n4. Kerko Vlerën\n5. Mbylle Programin\n") 
    choice = int(input("\nZgjidhni një opsion? "))
    while(choice != 5):  
        if(choice == 1):  
            input1 = int(input("\nVlera: "))
            q.EnQueue(input1)
            choice = int(input("\n>> Për të vazhduar shtypni 1 apo opsion tjetër! "))
        elif(choice == 2):  
            q.DeQueue()
            choice = int(input("\n>> Për të vazhduar shtypni 2 apo opsion tjetër! "))
        elif(choice == 3):  
            q.shfaqQueue()
            choice = int(input("\n>> Për të vazhduar shtypni 3 apo opsion tjetër! "))
        elif(choice == 4):  
            input2 = int(input("\nVlera: "))
            q.kerko(input2)
            choice = int(input("\n>> Për të vazhduar shtypni 4 apo opsion tjetër! "))
        elif(choice >5):
            print("Jepni një opsion të vlefshëm")
            break