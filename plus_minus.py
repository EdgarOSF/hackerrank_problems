def plusMinus(arr):
    p = 0
    n = 0
    z = 0

    ln = len(arr)

    for i in range(len(arr)):
        if arr[i] == 0:
            z += 1
        elif arr[i] < 0:
            n += 1
        else:
            p += 1
    print(f"{p/ln:.6f}\n{n/ln:.6f}\n{z/ln:.6f}")


print(plusMinus([-4, 3, -9, 0, 4, 1]))
print(plusMinus([1, 1, 0, -1, -1]))