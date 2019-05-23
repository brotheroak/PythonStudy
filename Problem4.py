def get_span(P):
    # Input: N일 동안 판매액을 저장한 List P
    # Output: 각 날짜에 대한 span값을 저장한 배열 S
    S = []
    idx = 1
    for val in P:
        if P.index(val) > 0 and P[P.index(val) -1] < val :
            idx += 1
        else :
            idx = 1
        S.append(idx)
    return S


P = [5800, 6000, 6100, 5900, 6050, 4900]

print(get_span(P))
