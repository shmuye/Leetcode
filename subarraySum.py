def subarraySum(arr,k):
    n = len(arr)
    count = 0
    curr_sum = 0
    start = 0
    for end in range(n):
        curr_sum += arr[end]
        while curr_sum >= 