class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


node1 = Node(20)
node2 = Node(34)
node3 = Node(45)
node4 = Node(50)
node5 = Node(60)

node1.next = node2
node2.next = node3 
node3.next = node4
node4.next = node5
# node5.next = node1 # if you want create singli linkedlist


currant = node1
while currant is not None:
    print(currant.data, end = "->")
    currant= currant.next

