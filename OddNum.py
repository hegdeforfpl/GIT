class A():
    def __init__(self,lis1):
        self.lis1 = lis1
    def odd(self):
        odd = []
        even = []
        for i in self.lis1:
            if i % 2 == 0:
                even = even + [i]
            else:
                odd = odd + [i]
        return odd
d = A([1,2,3,4,5])
print(d.odd())