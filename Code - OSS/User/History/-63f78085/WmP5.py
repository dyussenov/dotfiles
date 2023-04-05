class A:
    @classmethod
    def foo(cls):
        print(1)
    
    @staticmethod
    def boo():
        print(2)

    def coo(self):
        print(3)

a = A()
a.foo()
