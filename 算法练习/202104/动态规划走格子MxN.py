"""
f(i,j) = f(i,j-1)+f(i-1,j)

"""
def walk(m,n):
    """直接递归"""
    if m == 0 and n == 0:
        return 1
    elif m == 0:
        return walk(0, n-1)
    elif n == 0:
        return walk(m-1,0)

    else:
        return walk(m-1, n) + walk(m, n-1)


def walk_cache(m,n):
    """使用缓存"""
    a = []
    for i in range(m+1):
        a.append([])
        for j in range(n+1):
            a[i].append(1)
    # print(a)
    for i in range(1,m+1):
        for j in range(1, n+1):
            a[i][j] = a[i-1][j]+a[i][j-1]
    return a[m][n]


if __name__ == '__main__':
    m = 3
    n = 3
    b = walk_cache(m,n)
    print(b)
    c = walk(m,n)
    print(c)



