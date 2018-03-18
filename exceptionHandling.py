def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Zero division"

    
print(divide(1, 0))