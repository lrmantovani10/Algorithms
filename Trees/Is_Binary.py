def checkBST(root):
    def check(t, max_val, min_val):
        if not t:
            return True
        if t.data > max_val or t.data < min_val:
            return False
        return check(t.left, t.data - 1, min_val) and check(t.right, max_val, t.data + 1)
        
    return check(root, (10**4), 0) 