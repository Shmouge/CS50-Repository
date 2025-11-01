#User inputs expression
expr = input("Expression: ").strip()
x, op, z = expr.split()

x, z = float(x), float(z)

#Match user input to result
if op == "+":
    result = x + z
elif op == "-":
    result = x - z
elif op == "*":
    result = x * z
elif op == "/":
    result = x / z
else:
    result = 0
#Built with failsafe  

print(f"{result:.1f}")