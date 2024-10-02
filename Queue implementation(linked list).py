class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class queue:
    def __init__(self):
        self.rear=None
        self.front=None
        self.size=0
    def enqueue(self,data):
        newnode=node(data)
        self.size+=1
        if self.rear==None and self.front==None:
            self.rear=newnode
            self.front=newnode
        else:
            self.rear.next=newnode
            self.rear=newnode
    def dequeue(self):
        if self.rear is None and self.front is None:
            print('Queue is empty')
        else:
            temp=self.front
            print(self.front.data)
            self.front=self.front.next
            del temp
            self.size-=1
            if self.front is None:
                self.rear=None
    def display(self):
        print(self.size)

n=int(input())
obj=queue()
for i in range(n):
    c=input().split()
    if c[0]=='enqueue':
        obj.enqueue(int(c[1]))
    elif c[0]=='dequeue':
        obj.dequeue()
    elif c[0]=='size':
        obj.display()

