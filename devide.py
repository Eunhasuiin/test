def devide(a,b):
    try:
        a/b
    except ZeroDivisionError as e:
        print('0으로 나누면 에러가 발생합니다.')
    else:
        a/b

