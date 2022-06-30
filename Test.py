a = int(input("Number?"))
flag = False
if a > 1:
    for i in range(2, a):
        if a % i == 0:
            flag = True
            break

if flag:
    print("not a prime")
else:
    print("prime")