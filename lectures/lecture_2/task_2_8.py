
import decimal
import fractions


pi = decimal.Decimal('3.141_592_653_589_793_238_462')
print(pi)
num = decimal.Decimal(1) / decimal.Decimal(3)
print(num)
# задать точность для будущих операций
decimal.getcontext().prec = 120
num = decimal.Decimal(1) / decimal.Decimal(3)
print(num)

f1 = fractions.Fraction(1, 3)
print(f1)
f2 = fractions.Fraction(3, 5)
print(f2)
print(f1 * f2)