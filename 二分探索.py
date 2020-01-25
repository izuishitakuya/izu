A,B,X = map(int,input().split())
left = 0
right = 10**9
if A*right +B*10 <= X:
    print(right)
else:
    while left <= right:
        mid = (right+left)//2
        if A*mid + B*len(str(mid)) <= X:
            left = mid
        else:
            right = mid
        if right - left == 1:
            print(left)
            break