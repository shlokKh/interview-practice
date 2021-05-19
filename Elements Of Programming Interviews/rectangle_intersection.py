from collections import namedtuple

Rectangle = namedtuple('Rectangle', ('x', 'y', 'width', 'height'))

'''
Lets think about the case a rectangle cannot intersect another
1. if the r1.x + width < r2.x or vice versa
2. if the r2.x + width < r1.x
'''
def rectangle_intersection(r1: Rectangle, r2: Rectangle) -> Rectangle:
    if r1.x + r1.width <= r2.x and r2.x + r2.width <= r1.x:
        if r1.y + r1.height <= r2.height and r2.y + r2.height <= r1.y:
            return None

    return Rectangle(max(r1.x, r2.x), max(r1.y, r2.y), min(r1.x+r1.width, r2.x+r2.width) - max(r1.x, r2.x), min(r1.y+r1.height, r2.y + r2.height)) - max(r1.y, r2.y)

        # So here we have the x side not intersecting but the y side

