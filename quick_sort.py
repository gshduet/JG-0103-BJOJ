def quick_sort_v1(lst: list) -> list:
    if len(lst) <= 1:
        return lst

    pivot = lst[0]
    small_lst, middle_lst, large_lst = [], [], []

    for value in lst:
        if pivot > value:
            small_lst.append(value)
        elif pivot < value:
            large_lst.append(value)
        else:
            middle_lst.append(value)

    return quick_sort_v1(small_lst) + middle_lst + quick_sort_v1(large_lst)

def quick_sort_v2(a:list, first:int, last:int) -> None:
    if first >= last:
        return

    pivot = a[first] # 편의상 first 인덱스에 있는 값을 피봇으로 삼았다. ((first + last) // 2)로 해도 무방하다.
    left = first + 1
    right = last

    while left <= right: 
        while left <= right and pivot > a[left]:
            left += 1

        while pivot < a[right]:
            right -= 1

        if left <= right:
            a[left], a[right] = a[right], a[left]
            left +=1
            right -= 1

    a[first], a[right] = a[right], a[first]

    quick_sort_v2(a, first, right - 1)
    quick_sort_v2(a, right + 1, last)
