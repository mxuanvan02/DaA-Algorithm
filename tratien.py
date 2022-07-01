n = int(input("Nhập số tiền cần trả: "))
m = int(input("Nhập số loại tiền: "))

X = []
S = []
for i in range(m):
  a = int(input("Nhập các mệnh giá các loại tiền: "))
  X.append(a)

for i in range(m-1):
  for j in range(i, m):
    if X[i] < X[j]:
      X[i], X[j] = X[j], X[i]

X1 = n // X[0]
S.append(X1)
remaining1 = n - X1 * X[0]

for i in range(1, m):
  X1 = remaining1 // X[i]
  S.append(X1)
  remaining1 -= X1 * X[i]

print("Các mệnh giá cần trả: ")
for i in range(m):
  print(f"Tiền loại {X[i]} cần {S[i]} tờ.")