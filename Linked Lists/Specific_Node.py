def insertNodeAtPosition(llist, data, position):
    if position == 0:
        new_node = SinglyLinkedListNode(data)
        new_node.next = llist
        llist = new_node
    else:
        index = 0
        node = llist
        while node != None:
            if index == position -1:
                new_node = SinglyLinkedListNode(data)
                new_node.next = node.next
                node.next = new_node
                
                break
            index += 1
            node = node.next
    
    return llist
