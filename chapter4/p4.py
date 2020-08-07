def check_balance(n):
    return check_balance_aux(n) != -1000000


def check_balance_aux(n):
    if n == None:
        return -1
    leftHeight = check_balance_aux(n.left)
    if leftHeight == -1000000:
        return -1000000
    rightHeight = check_balance_aux(n.right)
    if rightHeight == -1000000:
        return -1000000
    
    height_dif = abs(leftHeight-rightHeight)
    if height_dif > 1:
        return -1000000
    else:
        return max(leftHeight, rightHeight) + 1

        