def insertion_sort(arr):
    for i in range(1,len(arr)):
        current = arr[i]
        pre_index = i - 1
        while pre_index >=0 and current<arr[pre_index]:
            arr[pre_index+1] = arr[pre_index]
            pre_index -= 1
        arr[pre_index+1] = current

    return arr


if __name__ == '__main__':
    a = [1, 2, 3, 3, 4, 3, 5, 2, 6, 6, 6, 7, 8, 9, 9, 85]
    b = insertion_sort(a)
    print(b)