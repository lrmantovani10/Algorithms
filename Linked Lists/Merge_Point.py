def findMergeNode(head1, head2):
    heads1 = []
    heads2 = []
    while head1 != None:
        heads1.append(head1)
        head1 = head1.next
    while head2 != None:
        heads2.append(head2)
        head2 = head2.next 
    
    comparator = ()
    for i, a in enumerate(heads1):
        if a in heads2:
            return a.data

