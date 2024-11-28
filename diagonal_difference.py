def diagonalDifference(arr):
    l = 0
    r = 0

    count = -1

    for i in range(len(arr)):
        l += arr[i][i]
        r += arr[i][count]
        count -= 1
    return(abs(l-r))


print(diagonalDifference([
    [11, 2, 4], 
    [4, 5, 6], 
    [10, 8, -12]
    ]
)) # 15