def div():
    try:
        a = int(input("Podaj pierwsza liczbę: "))
        b = int(input("Podaj drugą liczbę: "))
        print(a / b)
    except ValueError:
        print("Only numbers allowed")
    except ZeroDivisionError:
        print("Divider must be different than zero.")
    return


div()
