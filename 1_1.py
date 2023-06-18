troom,tcond = list(map(int,input().split()))
mode = input()
ans = troom
if tcond != troom:
    if mode == 'heat' and tcond > troom or mode == 'auto' and tcond > troom:
        ans = tcond
    if mode == 'freeze' and troom > tcond or mode == 'auto' and troom > tcond:
        ans = tcond
print(ans)