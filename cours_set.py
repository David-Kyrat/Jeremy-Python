def intro():
    listdbl = [2, 2, 3]
    l = ["2", "3", "4"]
    s = set()

    for el in listdbl:
        print(f"adding {el} to set: {s}")
        s.add(el)
        print(f"set={s}\n")

    print(",".join(l))  # pas faire ",".join(listdbl) car c'est pas une liste de string (str) !


