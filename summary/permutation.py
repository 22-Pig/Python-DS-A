def Solution(L, R):
    if (len(R) == 0):
        for i in L:
            print("%5d" % i, end="")
        print()
        return 0
    for x in R:
        tmp = R + []
        tmp.remove(x)
        Solution(L + [x], tmp)


n = int(input())
Solution([], list(range(1, n + 1)))
