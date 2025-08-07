class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        self.numerator = numerator
        self.denominator = denominator
        self._simplify()  # Simplify the fraction upon initialization
    
    def _find_gcd(self, a, b):
        a, b = abs(a), abs(b)  # Work with absolute values
        while b != 0:
            a, b = b, a % b
        return a
    
    def _simplify(self):
        gcd = self._find_gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator
    
    def add(self, other):
        # Add two fractions: a/b + c/d = (a*d + c*b) / (b*d)
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)
    
    def subtract(self, other):
        # Subtract two fractions: a/b - c/d = (a*d - c*b) / (b*d)
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)
    
    def multiply(self, other):
        # Multiply two fractions: (a/b) * (c/d) = (a*c) / (b*d)
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)
    
    def divide(self, other):
        if other.numerator == 0:
            raise ValueError("Cannot divide by zero fraction")
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)
    
    def __eq__(self, other):
        # Compare two fractions for equality
        if not isinstance(other, Fraction):
            return False
        return (self.numerator == other.numerator and 
                self.denominator == other.denominator)
    
    def __str__(self):
        # String representation of the fraction
        if self.denominator == 1:
            return str(self.numerator)
        return f"{self.numerator}/{self.denominator}"
    
    def __repr__(self):
        # Detailed representation for debugging
        return f"Fraction({self.numerator}, {self.denominator})"
