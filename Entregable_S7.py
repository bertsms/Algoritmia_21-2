# Ciclos anidados
for a in range(10):
    for b in range(10):
        print("Ciclo externo:", a, "Ciclo interno", b)

    print()
    ################################
"""
0 x 0 = 0
0 x 1 = 0
...
...
10 x 9 = 90
10 x 10 = 100
"""
for a in range(20): 
     for b in range(8):
         mult = b*a
         print(b,"x", a, "=", mult)
     print() 