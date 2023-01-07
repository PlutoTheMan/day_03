def validate_pesel(pesel):
    waga = list(str(1379137913))
    pesel_lista = list(str(pesel))

    if type(pesel) != int:
        return False
        # raise ValueError
    if len(pesel_lista) != 11:
        print("..")
        return False
        # raise IndexError

    try:
        sum = 0
        for i in range(10):
            sum += int(pesel_lista[i]) * int(waga[i])
        control_number = 10 - sum % 10
        # print(control_number)
        if control_number == int(pesel_lista[10]):
            return True
        return False
    except Exception:
        print("FAIL")
        return


print(validate_pesel(44051401359))
print(validate_pesel("abc"))
