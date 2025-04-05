x = float(input("give me your first number: "))
y = float(input ("now, your second number: "))

print ("addition yields -           {}" .format(x + y))
print ("subtraction gives -         {}" .format(x - y))
print ("multiplication gets -       {}" .format(x * y))
print ("dividing fetches -          {}" .format(x / y if y != 0 else 'undefined'))
print ("how about some modulus -    {}" .format(x % y if y != 0 else 'undefined'))