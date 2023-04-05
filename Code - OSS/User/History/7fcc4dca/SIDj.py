class outer:
    a = 4
    b = 8
    class inner:
        def __init__(self):
            a_inner = self.a


g = outer()

g1 = g.inner()

print(g1.a_inner)