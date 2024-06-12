def general_arr():
    n = int(input())
    heights = list(map(int, input().split()))

    mh = max(heights)
    mih = min(heights)

    m_in = heights.index(mh)
    mi_in = len(heights) - 1 - heights[::-1].index(mih)

    if m_in > mi_in:
        swaps = m_in + (n - 1 - mi_in) -1
    else:
        swaps = m_in + (n -1 - mi_in)

    return swaps

print(general_arr())