calc = input()
if '/' in calc:
    print(format(eval(calc), '.2f'))
else:
    print(int(eval(calc)))