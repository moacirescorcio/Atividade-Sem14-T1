temperatura1 = float(input())
escala1 = input().upper()
temperatura2 = float(input())
escala2 = input().upper()

t1 = (temperatura1, escala1)
t2 = (temperatura2, escala2)

if escala1 == escala2:
    if temperatura1 > temperatura2:
        print(t1)
    else:
        print(t2)
elif escala1 != escala2:
    if escala1 == 'C':
        t1_em_f = (temperatura1 * (9/5)) + 32
        if t1_em_f > temperatura2:
            print(t1)
        else:
            print(t2)
    if escala1 == 'F':
        t1_em_C = (temperatura1 - 32) * (5/9)
        if t1_em_C > temperatura2:
            print(t1)
        else:
            print(t2)