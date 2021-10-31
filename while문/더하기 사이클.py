a = int(input())
n = a

i = 0

while True:
    if n < 10:
        if 10*n + n == a:
            i += 1
            break
        else:
            i += 1
            n = 10*n + n
    else:
        n_str = str(n)
        n_list = list(n_str)
        m = int(n_list[0]) + int(n_list[1])
        if m < 10:
            if 10*int(n_list[1]) + m == a:
                i += 1
                break
            else:
                i += 1
                n = 10*int(n_list[1]) + m
        else:
            m_str = str(m)
            m_list = list(m_str)
            if 10*int(n_list[1]) + int(m_list[1]) == a:
                i += 1
                break
            else:
                i += 1
                n = 10*int(n_list[1]) + int(m_list[1])

print(i)