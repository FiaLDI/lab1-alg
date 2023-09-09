
if __name__ == '__main__':
    a = '''28	96	26	1	58	19	16	29	58	76
    35	33	11	88	92	31	15	5	39	21
    83	82	8	20	20	95	33	89	96	21
    61	11	95	70	8	91	41	64	46	50
    95	68	20	30	87	31	11	60	47	68
    28	48	40	46	6	28	74	7	100	55
    60	68	80	86	94	14	90	65	53	96
    89	15	37	8	34	94	99	51	1	76
    29	57	86	73	79	65	93	55	91	95
    68	40	86	47	39	4	62	23	33	15
    '''
    m = 10
    n = 10
    c = 0
    mas = [int(i) for i in a.split()]
    mas2 = [[0] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            mas2[i][j] = mas[c]
            c += 1
    for i in range(0, m):
        for j in range(0, n):
            if i == 0 and j == 0:
                pass
            if i == 0 and j != 0:
                mas2[i][j] += mas2[i][j - 1]
            if i != 0 and j == 0:
                mas2[i][j] += mas2[i - 1][j]
            if i != 0 and j != 0:
                mas2[i][j] += min(mas2[i-1][j], mas2[i][j-1])
    print(mas2[n - 1][m - 1])
