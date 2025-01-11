test = int(input())

theta = int(input())

n = []
m = []
output = []
for i in range(test):
    n1 = int(input())
    n.append(n1)
    x = list(map(int, input().split()))
    m.append(x)

for i in range(test):
    xi = m[i]
    n1 = n[i]
    out1 = []
    if n1 >= 3:
        delta_prev = abs(xi[1] - xi[0])
        for j in range(2, n1):
            delta_curr = abs(xi[j] - xi[j-1])
            delta2 = abs(delta_curr - delta_prev)
            if delta2 >= theta:
                out1.append('1')
            else:
                out1.append('0')
            delta_prev = delta_curr
    output.append(' '.join(out1))

for out1 in output:
    print(out1)