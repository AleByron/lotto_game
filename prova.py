


targhe_rubate = {'ABC123':3, 'CDE456': 1, 'EFG678': 7, 'POG976': 2, 'AEI098':1}
targhe_buone = ['LKJ908', 'IOU123', 'PIP543', 'QWE345', 'LDF678']
print(targhe_buone, list(targhe_rubate.keys()))
check = input('Inserisci una targa:')

while check != "":
    if check in targhe_rubate:
        print("L' auto {} è stata rubata da {} anni.".format(check, targhe_rubate[check]))
    elif check in targhe_buone:
        print("L' auto {} non è rubata".format(check))
    else:
        print("La targa inserita non fa parte di nessun database")

    check = input('Inserisci una targa:')

