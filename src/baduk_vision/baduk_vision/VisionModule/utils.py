def on_left_side(p, a, b):
    return (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0]) > 0

def point_in_quadrilateral(p, quad):
    for i in range(4):
        if not on_left_side(p, quad[i], quad[(i + 1) % 4]):
            return False
    return True