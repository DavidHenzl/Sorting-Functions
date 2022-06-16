"""
Sorting functions:
Bubble sort, Selection sort, Insertion sort, Merge sort, Quick sort, Counting sort, Bucket sort
"""


def bubble_sort(lst):
    """Sorts list with "bubble sort" in ascending order"""
    for i in range(len(lst) - 1):
        swapping = False
        for j in range(0, len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapping = True
        if not swapping:
            break


def selection_sort(lst):
    """Sorts list with "selection sort" in ascending order"""
    for x in range(len(lst)):
        min_index = x
        for i in range(x + 1, len(lst)):
            if lst[i] < lst[min_index]:
                min_index = i
        lst[x], lst[min_index] = lst[min_index], lst[x]


def insertion_sort(lst):
    """Sorts list with "insertion sort" in ascending order"""
    for i in range(1, len(lst)):
        sorting = lst[i]
        j = i - 1
        while j >= 0 and sorting < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = sorting
    # return is needed for bucket_sort below
    return lst


def merge_sort(lst):
    """Sorts list with "merge sort" in ascending order"""
    # if the list has 0-1 numbers, this function returns the same list
    # and it will no longer call inside merge_sort()
    if len(lst) > 1:
        # div_point is the point of dividing into sublists
        div_point = len(lst) // 2
        sublist1 = lst[:div_point]
        sublist2 = lst[div_point:]

        # sort the two parts
        merge_sort(sublist1)
        merge_sort(sublist2)

        i = j = k = 0

        # loop until the end of any sublist
        # place elements in correct position
        while i < len(sublist1) and j < len(sublist2):
            if sublist1[i] < sublist2[j]:
                lst[k] = sublist1[i]
                i += 1
            else:
                lst[k] = sublist2[j]
                j += 1
            k += 1

        # when no more elements in any sublist
        # pick up the remaining elements and put in the list
        while i < len(sublist1):
            lst[k] = sublist1[i]
            i += 1
            k += 1

        while j < len(sublist2):
            lst[k] = sublist2[j]
            j += 1
            k += 1

# Quick sort (functions partition and quick_sort)


def partition(lst, low, high):
    """Returns the partition position, low = starting index, high = ending index"""
    key = lst[high]
    # pointer for greater element
    i = low - 1
    # go through all elements and compare them with key
    for j in range(low, high):
        # if element is smaller then key, swap it with greater element pointed by i
        if lst[j] <= key:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    # swap the key with greater element pointed by i
    lst[i + 1], lst[high] = lst[high], lst[i + 1]
    # return the position from where partition is done
    return i + 1


def quick_sort(lst, low, high):
    """Sorts list with "quick sort" in ascending order"""
    if low < high:
        # find key element, that is bigger than all elements on the left
        # and all the greater elements are on the right
        key_index = partition(lst, low, high)
        # recursive call on the left of key
        quick_sort(lst, low, key_index - 1)
        # recursive call on the right of key
        quick_sort(lst, key_index + 1, high)


def counting_sort(lst):
    """Sorts list with "counting sort" in ascending order"""
    maxi = max(lst)
    mini = min(lst)
    size = len(lst)
    elm_range = maxi - mini + 1
    output = [0] * size
    count_list = [0] * (elm_range)
    # store count of each element to count_list
    for i in range(size):
        count_list[lst[i] - mini] += 1
    # and store the cumulative count
    for j in range(1, elm_range):
        count_list[j] += count_list[j - 1]
    # find the index in count_list of each element of the original list
    # place the elemenets in output
    for k in range(size):
        output[count_list[lst[k] - mini] - 1] = lst[k]
        count_list[lst[k] - mini] -= 1
    # replace the elements from original list with output elements
    for l in range(size):
        lst[l] = output[l]


def bucket_sort(lst, num_of_buckets):
    """Sorts list with "bucket sort" in ascending order"""
    arr = []
    max_elm = max(lst)
    min_elm = min(lst)
    # range for buckets
    b_range = (max_elm - min_elm) / num_of_buckets
    # create empty buckets
    for _ in range(num_of_buckets):
        arr.append([])
    # put list elements in different buckets
    for i in range(len(lst)):
        diff = (lst[i] - min_elm) / b_range - int((lst[i] - min_elm) / b_range)
        # append the boundary elements to the lower array
        if (diff == 0 and lst[i] != min_elm):
            arr[int((lst[i] - min_elm) / b_range) - 1].append(lst[i])
        else:
            arr[int((lst[i] - min_elm) / b_range)].append(lst[i])
    # sort individual buckets
    for i in range(len(arr)):
        if len(arr[i]) != 0:
            arr[i] = insertion_sort(arr[i])  # or arr[i].sort()
    # concantenate the result
    k = 0
    for sublist in arr:
        if sublist:
            for num in sublist:
                lst[k] = num
                k += 1
