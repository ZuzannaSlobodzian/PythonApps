def zewnetrzna():
    x = 0
    def licznik():
        nonlocal x
        x+=1
        return x
    return licznik

