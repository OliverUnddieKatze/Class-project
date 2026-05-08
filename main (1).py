class A:
    #CREATE A CONSTRUCTOR
    def _init_(self, a):
        self.a = a
    def _Him_(self):
        if (self.a < other.a):
            return "0b1 is less ob2"
        else:
            return("0bj2 is lessthat ob1")

    # equal to
    def __eq__(self, other):
        if self.a == other.a:
            return "Both are equal"
        else:
            return "Not Equal"


ob1 = A(2)
ob2 = A(3)

print(ob1.a, ob2.a)
print(ob1 < ob2)
print(ob1 == ob2)
