# matrix multiplication using lists

def matrix_add(list1, list2):
    # Check if the dimensions of the lists are the same
    if len(list1) != len(list2) or len(list1[0]) != len(list2[0]):
        return None  # Return None if dimensions don't match
    
    result = []
    
    for i in range(len(list1)):
        row = []

        for j in range(len(list1[0])):
            # Add corresponding elements
            row.append(list1[i][j] + list2[i][j])

        result.append(row)
    return result


# -----------------------------------------------
# main function
result = matrix_add([[2,2],[3,3]], [[4,4],[7,7]])
if result is not None:
    for row in result:
        print(row)
else:
    print("Dimensions of the lists don't match, cannot perform addition.")
