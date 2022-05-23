def foo_2(a: int, b: int):
    try:
        c = a / b
    except ZeroDivisionError as p:
        print(f'Not so many have the power to avoid {p}')
    except Exception as e:
        print(f'A mistake {e} were made')

    finally:
        print("I'am happy that you learn python")
    return c


print(foo_2(3, 0))
