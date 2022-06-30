class A:
    def a(self):
        print("Parent class")


class B(A):
    def b(self):
        print("Child class")


d = B()
d.a()
d.b()