try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')

def bool_return():
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")
divide(2, 1)
divide(2, 0)
ivide("2", "1")

