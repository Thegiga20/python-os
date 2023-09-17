def callapp():
    userinput = input('do you what to add, sub, times, dived? ')
    if userinput == 'add':
        addnumber1 = input('put in 1th number: ')
        addnumber2 = input('put 2th number:  ')
        add = float(addnumber1) + float(addnumber2)
        print(add)
    if userinput == 'sub':
        number1 = input('put in 1th number: ')
        number2 = input('put 2th number:  ')
        sub = float(number1) - float(number2)
        print(sub)
    if userinput == 'times':
        number1 = input('put in 1th number: ')
        number2 = input('put 2th number:  ')
        times = float(number1) * float(number2)
        print(times)
    if userinput == 'dived':
        number1 = input('put in 1th number: ')
        number2 = input('put 2th number:  ')
        dievd = float(number1) / float(number2)
        print(dievd)