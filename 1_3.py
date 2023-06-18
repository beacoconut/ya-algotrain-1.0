num1 = str(input())
num2 = str(input())
num3 = str(input())
num4 = str(input())
nonnumbers = "-()"
listofnumbers = [num1,num2,num3,num4]
rightans = ''
for i in range(len(listofnumbers)):
    final_i = listofnumbers[i].translate({ord(c): None for c in "-()"})
    if final_i.startswith('+7'):
        final_i = final_i.replace('+7','8')
    if not final_i.startswith('8'):
        final_i = '8495'+final_i
    if i == 0:
        rightans = final_i
    else:
        if final_i == rightans:
            print("YES")
        else:
            print('NO')