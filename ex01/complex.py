# class是关键字,表示类定义的开始,ComplexNumber是这个类的名字
class ComplexNumber:

    # 类中定义__init__函数,称为初始化方法,用于构造一个该类的新对象
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, another):
        real = self.real + another.real
        imaginary = self.imaginary + another.imaginary
        return ComplexNumber(real, imaginary)

    def __sub__(self, another):
        real = self.real - another.real
        imaginary = self.imaginary - another.imaginary
        return ComplexNumber(real, imaginary)

    def __mul__(self, another):
        real = self.real * another.real - self.imaginary * another.imaginary
        imaginary = self.imaginary * another.real + self.real * another.imaginary
        return ComplexNumber(real, imaginary)

    def __truediv__(self, another):
        real = (self.real * another.real + self.imaginary *
                another.imaginary) / (another.real**2 + another.imaginary**2)
        imaginary = (self.imaginary * another.real -
                     self.real * another.imaginary) / (another.real**2 +
                                                       another.imaginary**2)
        return ComplexNumber(real, imaginary)

    def __str__(self):
        if self.imaginary >= 0:
            return str(self.real) + "+" + str(self.imaginary) + "i"
        if self.imaginary == 0 and self.real == 0:
            return str(0)
        else:
            return str(self.real) + str(self.imaginary) + "i"

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)


c1 = ComplexNumber(2, 3)
c2 = ComplexNumber(3, -5)
print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)
print(c1.conjugate())
