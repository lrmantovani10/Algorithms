
def reverse(llist):
    node = llist
    while node != None:
        prev_node = node.next
        node.next = node.prev
        node.prev = prev_node
        if node.prev == None:
            llist = node
            break
        node = node.prev 
            
        
    return llist

