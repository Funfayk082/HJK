def input_R():
     while True:
        x = int(input('Введите начальное значение = '))
        if x > 0:
            break
        print('Недопустимое значение')
    return x

def x2(x):
     return collatz(x // 2)


def x3_1(x):
    return collatz( x*3+1 )


def collatz(x):
      result = [x]
    if x == 1:
        pass
    elif x % 2 == 0:
        result.extend(x2(x))
    else:
        result.extend(x3_1(x))
    return result

n = input_R()
    print(collatz(n))

