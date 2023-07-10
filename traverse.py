def traverse(arr, i):
    if i == len(arr):
        return
    # 前序位置
    print(arr[i])
    traverse(arr, i + 1)
    # 后序位置


traverse([1, 3, 4, 7, 99], 0)
