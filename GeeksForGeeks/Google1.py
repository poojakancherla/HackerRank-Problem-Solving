arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 15
curr_total = 0
start = 0
end = 0
for i in range(len(arr)):
    while (curr_total < total):
        curr_total += arr[end]
        end += 1
    while (curr_total > total):
        curr_total -= arr[start]
        start += 1
    if curr_total == total:
        print(start, end+1)
