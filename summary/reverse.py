def mergeSort(lst):  #归并排序
    if len(lst) <= 1:
        return lst, 0
    mid = len(lst) // 2  # 将列表分成更小的两个列表
    # 分别对左右两个列表进行处理，分别返回两个排序好的列表
    left, count1 = mergeSort(lst[:mid])
    right, count2 = mergeSort(lst[mid:])
    lst, count = Count(left, right, 0)
    return lst, count1 + count2 + count


def Count(left, right, count):  # 合并两个已排序好的列表，产生一个新的已排序好的列表
    result = []  # 新的已排序好的列表
    i = 0  # left下标
    j = 0  # right下标

    # 对两个列表中的元素 两两对比。
    # 将最小的元素，放到result中，并对当前列表下标加1
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            # 当右半部分的元素先于左半部分元素进入有序列表时，逆序对数量增加左半部分剩余的元素数
            count += len(left) - i
            j += 1
    result += left[i:]
    result += right[j:]
    return result, count


a = []
n = int(input())
for i in range(n):
    x = int(input())
    a.append(x)
mergeSort(a)
print(mergeSort(a)[1])