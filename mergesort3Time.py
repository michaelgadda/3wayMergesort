import numpy as np
import time as time


def merge3(left, middle, right):
    combined = []
    i = j = k = 0
    while i < len(left) and j < len(right) and k < len(middle):
        if left[i] < right[j]:
            if left[i] < middle[k]:
                combined.append(left[i])
                i += 1
            else:
                combined.append(middle[k])
                k += 1
        elif right[j] < middle[k]:
            combined.append(right[j])
            j+=1
        else:
            combined.append(middle[k])
            k += 1

    while j < len(right) and k < len(middle):
        if right[j] < middle[k]:
            combined.append(right[j])

            j+=1
        else:
            combined.append(middle[k])

            k+=1

    while i < len(left) and k < len(middle):
        if left[i] < middle[k]:
            combined.append(left[i])

            i+=1
        else:
            combined.append(middle[k])

            k+=1

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            combined.append(left[i])

            i+=1
        else:
            combined.append(right[j])

            j+=1

    while i < len(left):
        combined.append(left[i])

        i+=1

    while j < len(right):
        combined.append(right[j])

        j+=1

    while k < len(middle):
        combined.append(middle[k])

        k+=1


    return combined


def merge_sort3(array):
    if len(array) < 2:
        return array

    if len(array) == 2:

        if(array[0] > array[1]):
            temp = array[0]
            array[0] = array[1]
            array[1] = temp
        return array


    qq = len(array) // 3
    zz = len(array) % 3
    qz = len(array)



    left = merge_sort3(array [:qq])

    middle = merge_sort3(array[(qq):((2*qq+1))])

    right = merge_sort3(array[((2*qq+1)):((3*qq)+zz)])

    return merge3(left, middle, right)



def run_mergesort():
    from random import randint
    x = 10000
    for i in range(1,20):

        numbers = np.random.randint(1, 10000, x)
        t1 = time.time()
        merge_sort3(numbers)
        t2 = time.time()
        t3 = t2 - t1
        print(str(x) + " : " + str(t3))
        x += 10000
    return numbers


run_mergesort()
