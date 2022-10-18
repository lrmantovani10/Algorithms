def has_cycle(head):
    heads = []
    while head != None:
        if head.next in heads:
            return True
        else:
            heads.append(head.next)
        head = head.next
    return False