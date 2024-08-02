# Factory function || closure in python

def chaiCoder(num):
    def actual(x):
        return (x ** num)
    return actual

f=chaiCoder(2)
g=chaiCoder(3)

print(f(3))
print(g(3))