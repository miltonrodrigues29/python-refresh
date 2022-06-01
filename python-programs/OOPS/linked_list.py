# class Node:
#     def __init__(self,dataval = None):
#         self.dataval = dataval
#         self.nextval =None

# class SLinkedList:
#     def __init__(self):
#         self.headval = None

# list1 = SLinkedList()
# # |headval = None|
# node1 = Node("Mon")

# list1.headval = node1
# # node1
# node2 = Node("Tue")
# node3 = Node("Weds")
# list1.headval.nextval = node2
# node2.nextval=node3



class Node:
    def __init__(self,data="None"):
        self.data = data
        self.nextVal = None

class SLinkedList:
    def __init__(self):
        self.headval = None

node1 = Node("Monday")
list1 = SLinkedList()
list1.headval = node1
node2 = Node("Tuesday")
node1.nextVal= node2
node3 = Node("Wednesday")
node2.nextVal = node3

#Mon->Tue->Wed->None


# iter = Node()
# iter = list1.headval
# print(iter.data)

# while(iter!=None):
#     print(iter.data,end='->')
#     iter = iter.nextVal
    

if __name__ == "main":
    n = int(input("Enter the number of nodes in linked list"))
    if n==0:
        print("Linked List Should have atleast one element")
    else:

    

  





