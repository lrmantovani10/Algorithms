def sortedInsert(llist, data):
    node = llist
    
    if data < llist.data:
        new_node = DoublyLinkedListNode(data)
        new_node.prev = None
        new_node.next = llist
        new_node.next.prev = new_node
        llist = new_node
    
    else:  
        while node != None:
            if node.next != None:
                if node.data <= data <= node.next.data:
                    next_node= node.next
                    new_node = DoublyLinkedListNode(data)
                    new_node.next = next_node
                    new_node.prev = node
                    node.next = new_node
                    break
            
            if node.next == None and data >= node.data:
                new_node = DoublyLinkedListNode(data)
                new_node.next = None
                new_node.prev = node
                node.next = new_node
                break
            
            node = node.next
    
    return llist
