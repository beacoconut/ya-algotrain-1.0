a = int(input())
b = int(input())
c = int(input())
if c == 0:
    if a == 0:
        if b == 0:
            print('MANY SOLUTIONS')
        else:
            print('NO SOLUTION')
    else:
        ans = -b//a
        if ans == -b/a:
            print(ans)
        else:
            print('NO SOLUTION')
elif (a + b) == c**2 and (2 * a + b) == c**2:
    print("MANY SOLUTIONS")
elif c > 0:
    if a == 0:
        if b == c**(1/2):
            print('MANY SOLUTIONS')
        else:
            print('NO SOLUTION')
    else:
        ans = (c**2-b)//a
        if ans == (c**2-b)/a:
            print(ans)
        else:
            print('NO SOLUTION')
else:
    print('NO SOLUTION')