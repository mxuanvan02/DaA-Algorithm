n = int(input("Nhap n: "))


def shortestPath(n):
  A = [[0 for i in range(n)] for j in range(n)]
  F = [[0 for i in range(n)] for j in range(n)]

  for i in range(n):
    for j in range(n):
      a = int(input(f"Nhap phan tu thu ({i+1})({j+1}) cho luoi hinh vuong: "))
      A[i][j] = a
    
  for i in range(n):
    for j in range(n):
      if i == 0 and j > 0:
        F[i][j] = A[0][j] + F[0][j-1]
      elif j == 0 and i > 0:
        F[i][j] = A[i][0] + F[i-1][0]
      else:
        F[i][j] = min(F[i-1][j], F[i][j-1]) + A[i][j]
  print(F)
  return F[i][j]

print(f"Tong cac o di qua la nho nhat la: {shortestPath(n)}")