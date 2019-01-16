# We take two index pointers: rd_index to traverse through the same elements and wr_index to write to the array
# rd_index moves forward and increments counter for every iteration. It stops when the next element is different
# wr_index writes the curr element to the array and then increments. Also check if the count is greater than 1
# If the counter is greater than one, add each ele in str(count) to the array while increasing the wr_index
# Start the rd_index again by making counter 0 and repeat until all elemens are exhausted

def compress(arr):
    rd_index = wr_index = 0
    count = 0
    while rd_index < len(arr):
        curr_ele = arr[rd_index]
        count = 0
        while (rd_index < len(arr) and arr[rd_index] == curr_ele):
            rd_index += 1
            count += 1
        arr[wr_index] = curr_ele
        wr_index += 1
        if count > 1:
            for i in str(count):
                arr[wr_index] = i
                wr_index += 1

    return (wr_index, arr[:wr_index])


print(compress(["a","a","b","b","c","c","c","b","b"]))
