def create_array():
    n = int(input("How many elements do you want in the array? "))
    arr = []
    for i in range(n):
        value = int(input(f"Enter element {i+1}: "))
        arr.append(value)
    return arr

print("Let's create your first array:")
array1 = create_array()
print("Your array is:", array1)

print("\nLet's create another array:")
array2 = create_array()
print("Your second array is:", array2)

if len(array1) == len(array2):
    result = [array1[i] + array2[i] for i in range(len(array1))]
    print("\nElement-wise addition result:", result)
else:
    print("\nArrays are of different lengths, cannot add element-wise directly.")
