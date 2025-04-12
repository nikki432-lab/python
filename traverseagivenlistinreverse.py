def Traverse_reverse_with_indices(lst):
    for i in range(len(lst)-1,-1,-1):
        print(f"Index: {i}, Element: {lst[i]}")

original_list = ['red','green','white','black']
print("Traverse the list in reverse order:")
Traverse_reverse_with_indices(original_list)
