# demonstrates what is treated as False

if not None:
    print("None -> False")

if not 0:
    print("0 -> False")

if not '':
    print("'' -> False")

if not []:
    print("[] -> False")

if not {}:
    print("{} -> False")

