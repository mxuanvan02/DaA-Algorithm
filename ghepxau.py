
chars = ['A','B','C','D','E']
n = int(input("Nhap n: "))


def SinhKeTiep(n, A= None, recursive=None):
    if recursive == None:
        recursive = 0
        A = [None]*n
    for char in chars:
        if recursive > 0 and char == A[recursive-1]:
            continue
        A[recursive] = char
        
        if recursive == n-1:
            print(''.join(A))
        else:
            SinhKeTiep(n,A,recursive=recursive+1)
    
SinhKeTiep(n)