class A:
    def a(self):
        print("Parent")


class B(A):
    def b(self):
        print("Child")


d = B()
d.a()
d.b()