#归并排序,对列表a的[lt,rt]内的所有数进行归并排序
def reverseNumMerge(a, lt, rt):
    #1.边界条件，只有1个数一定有序
    if lt == rt:
        return 0
    #2.先求中点，二分[lt,mid]和[mid+1,rt]
    mid = (lt + rt) // 2
    #3.左边区间[lt,mid]求逆序对
    x1 = reverseNumMerge(a, lt, mid)
    #4.3.右半区间[mid+1,rt]求逆序对
    x2 = reverseNumMerge(a, mid + 1, rt)
    #4.合并2个有序区间
    return x1 + x2 + merge(a, lt, mid, rt)
    # return merge(a, lt, mid, rt)


#合并2个有序区间[lt,mid]和[mid+1,rt]
def merge(a, lt, mid, rt):
    temp = [0] * (rt - lt + 1)
    x = 0
    i, j, k = lt, mid + 1, 0  #左半区间，右半区间，临时列表
    while i <= mid and j <= rt:
        if a[i] <= a[j]:
            temp[k] = a[i]
            i += 1
        else:
            temp[k] = a[j]
            j += 1
            x += mid - i + 1
        k += 1

    #没取完的数
    while i <= mid:
        temp[k] = a[i]
        i += 1
        k += 1
    while j <= rt:
        temp[k] = a[j]
        j += 1
        k += 1

    #temp复制到源列表
    for i in range(k):
        a[lt + i] = temp[i]
    return x


a = []
n = int(input())
for i in range(n):
    x = int(input())
    a.append(x)
print(reverseNumMerge(a, 0, len(a) - 1))
