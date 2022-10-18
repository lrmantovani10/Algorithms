def lca(root, v1, v2):
  def check(t, n1, n2):
    if n1 < t.info < n2 or n2 < t.info < n1:
        return t 
    elif n1 == t.info or n2 == t.info:
        return t
    elif n1 < t.info and n2 < t.info:
        return check (t.left, n1, n2)
    elif n1 > t.info and n2 > t.info:
        return check(t.right, n1, n2)
    elif t == None:
        return root.info

  return check(root, v1, v2)
