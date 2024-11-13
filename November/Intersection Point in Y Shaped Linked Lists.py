def intersetPoint(head1, head2):
    len1, len2 = 0, 0
    temp1, temp2 = head1, head2
    
    while temp1:
        len1 += 1
        temp1 = temp1.next
    
    while temp2:
        len2 += 1
        temp2 = temp2.next
    
    temp1, temp2 = head1, head2
    if len1 > len2:
        for _ in range(len1 - len2):
            temp1 = temp1.next
    elif len2 > len1:
        for _ in range(len2 - len1):
            temp2 = temp2.next
    
    while temp1 and temp2:
        if temp1 == temp2:
            return temp1.data
        temp1 = temp1.next
        temp2 = temp2.next
    
    return -1
