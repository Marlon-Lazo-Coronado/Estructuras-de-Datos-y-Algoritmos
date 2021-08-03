A = [-9,-45,0,7,45,-100,89];
s = 0;
_s = 0;

for i in A:
    if i < 0:
        _s += i;
    else:
        s += i;
print("La lista es: ", A)
print("La suma de los positivos es: ", s,"\nLa suma de los negativos es:", _s*(-1))
print("La lista ordenada es: ", sorted(A))
#Ordenamos la lista con un for
tem = 0;
for i in range(len(A)):
    for j in range(len(A)):
        if A[i] < A[j]:
            tem = A[j];
            A[j] = A[i];
            A[i] = tem;
print("\n\nLa lista ordenada con un for es: ", A)