class Node:
    def __init__(self, data=None):
        self.data = data
        self.previous = self
        self.next = self


class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0
    
    def add_at_tail(self, data) -> bool:
        # Write code here
        newNode = Node(data)
        temp = self.head
        while(temp.next != None):
            temp = temp.next
        temp.next = newNode
        newNode.previous = temp
        if newNode.previous == temp:
            return True
        else:
            return False
        
    def add_at_head(self, data) -> bool:
        # Write code here
        if self.head == None:
            newNode = Node(data)
            self.head = newNode
        else:
            newNode = Node(data)
            self.head.previous = newNode
            newNode.next = self.head
            self.head = newNode
        if self.head == newNode:
            return True
        else:
            return False
        
    def add_at_index(self, index, data) -> bool:
        # Write code here
        temp=Node()
        temp.data=data
        temp.previous=index
        temp.next=index+1
        index.next=temp
        if index.next==None:
            end=temp
        if end==temp:
            return True
        else:
            return False
        
    def get(self, index) -> int:
        # Write code here
        if index!=None:
            return index.data
        else:
            return -1

    def delete_at_index(self, index) -> bool:
        # Write code here
        if(temp.next != None):
            if(temp == index):
                temp.next.previous = None
                self.head = temp.next
                temp.next = None
                return True
            else:
                while(temp.next != None):
                    if(temp == index):
                        break
                    temp = temp.next
                if(temp.next):
                    temp.previous.next = temp.next
                    temp.next.previous = temp.previous
                    temp.next = None
                    temp.previous = None
                else:
                    temp.previous.next = None
                    temp.previous = None
                return True

         if (temp == None):
            return False
        
    def get_previous_next(self, index) -> list:
        # Write code here
        while(index!=None):
            return index.data
            index=index.next
            
# Do not change the following code
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = []
iteration_count = 0

for item in input_data.split(', '):
    inner_list = []
    if item.isnumeric():
        data.append(int(item))
    elif item.startswith('['):
        item = item[1:-1]
        for letter in item.split(','):
            if letter.isnumeric():
                inner_list.append(int(letter))
        data.append(inner_list)

obj = DoublyCircularLinkedList()
result = []
for i in range(len(operations)):
    if operations[i] == "add_at_head":
        result.append(obj.add_at_head(data[i]))
    elif operations[i] == "add_at_tail":
        result.append(obj.add_at_tail(data[i]))
    elif operations[i] == "add_at_index":
        result.append(obj.add_at_index(int(data[i][0]), data[i][1]))
    elif operations[i] == "get":
        result.append(obj.get(data[i]))
    elif operations[i] == "get_previous_next":
        result.append(obj.get_previous_next(data[i]))
    elif operations[i] == 'delete_at_index':
        result.append(obj.delete_at_index(data[i]))

print(result)
