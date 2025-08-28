def add_arrays(*arrays):
    min_length = min(len(arr) for arr in arrays)
    result = [sum(arr[i] for arr in arrays) for i in range(min_length)]
    return result
arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
arr3 = [7, 8, 9]
print("Array 1:", arr1)
print("Array 2:", arr2)
print("Array 3:", arr3)
result = add_arrays(arr1, arr2, arr3)
print("Result (Element-wise Addition):", result)
