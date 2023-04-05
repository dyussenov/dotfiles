class A:
    @classmethod
    def foo(self):
        print(1)
    
    @staticmethod
    def boo():
        print(2)

    def coo():
        print(3)

a = A()
a.foo()