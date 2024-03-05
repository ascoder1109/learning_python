class ComplexNumber:
  def __init__(self, real, imag):
    self.real = real
    self.imag = imag

  # Overload the + operator for adding complex numbers
  def __add__(self, other):
    return ComplexNumber(self.real + other.real, self.imag + other.imag)

# Create complex numbers
c1 = ComplexNumber(2, 3)
c2 = ComplexNumber(4, 1)

# Add them using the + operator (which calls __add__)
c3 = c1 + c2

print(c3.real, c3.imag)  # Output: 6 4
