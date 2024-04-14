def calculate_result(expression):
    x, y, z = expression.split()

    x = float(x)
    z = float(z)

    if y == "+":
        return x + z
    elif y == "-":
        return x - z
    elif y == "*":
        return x * z
    elif y == "/":
        return x / z

user_expression = input("Enter an arithmetic expression (x y z): ")
result = calculate_result(user_expression)
formatted_result = "{:.1f}".format(result)
print("Result:", formatted_result)