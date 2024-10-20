arr = [7,88,41,55,12,35]
largest_num = arr[0]
for i in range(1, len(arr)):
    if arr[i] > largest_num:
        largest_num = arr[i]
print(largest_num)