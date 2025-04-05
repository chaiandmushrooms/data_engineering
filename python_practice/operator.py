def operate (x, op, y):
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/' and y == 0:
        return 'undefined'
    elif op == '/':
        return x / y
    elif op == '%' and y == 0:
        return 'undefined'
    elif op == '%':
        return x % y
    else:
        return 'invalid operation'
    
x = float(input("enter first number: "))
y = float(input("enter second number: "))
op = input("enter your operator: ").strip()

print("{} {} {} = {}".format(x, op, y, operate(x, op, y)))