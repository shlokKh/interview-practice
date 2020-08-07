def getOrderString(node, l):
    if node == None:
        l.append("X")
        return
    l.append(node.data)
    getOrderString(node.left, l)
    getOrderString(node.rigt, l)

