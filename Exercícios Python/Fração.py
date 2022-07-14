from fractions import Fraction
from decimal import Decimal
 
Fraction(11, 35)
# returns Fraction(11, 35)
 
Fraction(10, 18)
# returns Fraction(5, 9)
 
Fraction('8/25')
# returns Fraction(8, 25)
 
Fraction(1.13)
# returns Fraction(1272266894732165, 1125899906842624)
 
Fraction('1.13')
# returns Fraction(113, 100)
 
Fraction(Decimal('1.13'))
# returns Fraction(113, 100)
