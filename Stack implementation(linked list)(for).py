class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class stack:
    def __init__(self):
        self.head=None
        self.top=None
    def push(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
            newnode.next=self.top
            self.top=newnode
        else:
            newnode.next=self.top
            self.top=newnode
    def pop(self):
        if self.top is None:
            print("Stack Underflow!")
        else:
            print(self.top.data)
            self.top=self.top.next
    def peek(self):
        print(self.top.data)
    def display(self):
        while self.top!=self.head:
            print(self.top.data,end=" ")
            self.top=self.top.next
        print(self.head.data)
    def isempty(self):
        if self.top is None:
            print("True")
        else:
            print("False")
obj=stack()
n=int(input())
for i in range(n):
    s=input().split()
    if s[0]=='push':
        obj.push(s[1])
    elif s[0]=='pop':
        obj.pop()
    elif s[0]=='peek':
        obj.peek()
    elif s[0]=='isEmpty':
        obj.isempty()
    elif s[0]=='size':
        obj.display()

        
