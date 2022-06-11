def divide_array_into_sub_arrays(array):
    count = 0
    for i in range(len(array)):
        count+= array[i]
        for j in range(1, len(array)):
            sum = array[i] + array[j]
            if sum == count//2:
                return f" Sub-arrays are [ {array[i]}, {array[j]} ]"

   
print(divide_array_into_sub_arrays([1, 4, 2, 5]))
s