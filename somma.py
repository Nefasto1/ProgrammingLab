def sum(list)
    s = 0;

    a = input("Inserisci il valore (Inserisci un valore non numerico per terminare): ");
    while a.isnumeric():
        list.append(float(a));
        a = input("Inserisci il valore (Inserisci un valore non numerico per terminare): ");

    for item in list:
        s += item;

    print("\nLa somma di {} è: {}" .format(list, s));