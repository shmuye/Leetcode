def numberOfApple(weight):
    weight.sort()
    n = len(weight)
    prefix_sum = [0]*n
    prefix_sum[0] = weight[0]
    for i in range(1,n):
        prefix_sum[i] = prefix_sum[i - 1] + weight[i]
    for i in range(n):
        if prefix_sum[i] > 5000:
            return i
    return n
