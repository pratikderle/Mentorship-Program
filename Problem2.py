arr = [12, 35, 1, 10, 34, 1]
first_large = None
second_large = None
for num in arr:
    if first_large is None or num > first_large:
            second_large = first_large
            first_large = num
    elif num < first_large:
        if second_large is None or num > second_large:
            second_large = num
    
if second_large is not None:
    print(second_large)
else:
    print("-1")