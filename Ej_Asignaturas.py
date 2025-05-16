curso={'matematicas':6,'fisica':4,'quimica':5}
total_creditos=0
for asignatura, creditos in curso.items():
    print(asignatura, 'tiene', creditos, 'creditos')
    total_creditos+=creditos
print('numero roral de creditos del curso: ', total_creditos)
