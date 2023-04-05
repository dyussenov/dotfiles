class outer:
    a = 4
    b = 8
    class inner:
        def __init__(self):
            self.a_inner = outer.a


g = outer()
g.a = 228

g1 = g.inner()

print(g1.a_inner)