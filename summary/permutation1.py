def permute(nums):
    x = len(nums)
    selected = []

    def dfs(nums, selected):
        # 条件
        if len(selected) == x:
            for i in selected:
                print("%5d" % i, end="")
            print()
            return
        # 深度优先递归
        for i in range(x):
            if nums[i] not in selected:
                selected.append(nums[i])
                dfs(nums, selected)
                selected.pop()

    dfs(nums, selected)


n = int(input())
permute(list(range(1, n + 1)))