
if __name__ == '__main__':
    f = [0, 1, 2, 0, 0, 0, 0, 0, 0, 0]
    for i in range(3, 8):
        f[i] = 2 * f[i - 1] + ((i - 2) * f[i - 2])
    print(f[6])