
def merge(array1, array2):
    new_array = []
    i, j = 0, 0

    if not isinstance(array1, list) or not isinstance(array2, list):
        raise TypeError("Not array.")

    while i < len(array1) or j < len(array2):
        if i < len(array1):
            new_array.append(array1[i])
            i += 1
        if j < len(array2):
            new_array.append(array2[j])
            j += 1

    print(new_array)

     

array1 = [1,2,3,4]
array2 = [5,6,7,8,9,10,11]

merge(array1, array2)