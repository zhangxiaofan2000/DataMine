import matplotlib.pyplot as plt

def Judge_diagonal(list):
    t = 1
    for i in range(0, len(list)):
        for j in range(i+1, len(list)):
            if abs(list[i]-list[j]) == j-i:
                t = 0
                break
    return t

def draw_image(list):
    n = len(list)
    image_list = []
    labels = []
    for i in range(0, n):
        image_list.append([1]*n)
        image_list[i][list[i]-1] = 0
        labels.append(i+1)
    plt.imshow(image_list, cmap='gray')
    plt.title("%d-皇后问题的解" % n)
    plt.xticks(range(0, n, 1), labels)
    plt.yticks(range(0, n, 1), labels)
    index = [i-0.5 for i in labels]
    index.pop()
    plt.vlines(index, -0.5, n-0.5)
    plt.hlines(index, -0.5, n-0.5)
    plt.show()

n = 10
c = [0] * n
flag = False
k = 0
while k >= 0:
    while c[k] <= n-1:
        c[k] = c[k] + 1
        if 0 not in c and len(set(c)) == n and Judge_diagonal(c):
            flag = True
            break
        elif len(set(c[0:k+1])) == k+1 and Judge_diagonal(c[0:k+1]):
            k = k + 1
    if flag:
        break
    c[k] = 0
    k = k - 1
if flag:
    print(c)
    draw_image(c)
else:
    print("no solution")
