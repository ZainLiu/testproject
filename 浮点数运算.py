from decimal import Decimal
class FractionCalculation(object):
    """
    浮点数运算类

    """
    @staticmethod
    def add_2(a, b):
        return Decimal(str(a))+Decimal(str(b))

    @staticmethod
    def sub_2(a, b):
        return Decimal(str(a))-Decimal(str(b))

a = FractionCalculation.add_2(0.6,0.2)
b = FractionCalculation.sub_2(0.6,0.2)
print(a,b)


