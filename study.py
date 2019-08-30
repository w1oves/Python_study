def normalize(name):
    x=name[0].upper()+name[1:].lower()
    return x
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)