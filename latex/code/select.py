import math

def split(A,low,high):
    B = A[low:high+1]
    i = 0
    x = B[0]
    for j in range(1, len(B)):
        if B[j] <= x:
            i = i+1
            if i != j:
                t = B[i]
                B[i] = B[j]
                B[j] = t
    tt = B[0]
    B[0] = B[i]
    B[i] = tt
    A[low:high+1] = B
    return i+low

def quicksort(A,low,high):
    if low < high:
        w = split(A, low-1, high-1)
        quicksort(A, low, w)
        quicksort(A, w+2, high)

def select(A,low,high,k):
    if k <= 0:
        print("k不能小于等于0")
        return
    p = high-low+1
    if p < 6:
        quicksort(A, 1, len(A))
        return A[k-1]
    step = 5
    b = [A[i:i+step] for i in range(0, len(A), step)]
    if p % 5 != 0:
        b.pop()
    q = len(b)
    m = []
    for i in b:
        quicksort(i, 1, len(i))
        m.append(i[2])
    mm = select(m, 1, q, math.ceil(q/2))
    a1 = []
    a2 = []
    a3 = []
    for a in A:
        if a < mm:
            a1.append(a)
        elif a == mm:
            a2.append(a)
        else:
            a3.append(a)
    if len(a1) >= k:
        return select(a1, 1, len(a1), k)
    elif len(a1)+len(a2) >= k:
        return mm
    elif len(a1)+len(a2) < k:
        return select(a3, 1, len(a3), k-len(a1)-len(a2))

A = [8,33,17,51,57,49,35,11,25,37,14,3,2,13,52,12,6,29,32,54,5,16,22,23,7]
k = 8
x = select(A, 1, len(A), k)
print('第', k, '小元素为:', x)
k = 13
x = select(A, 1, len(A), k)
print('第', k, '小元素为:', x)
k = 20
x = select(A, 1, len(A), k)
print('第', k, '小元素为:', x)
