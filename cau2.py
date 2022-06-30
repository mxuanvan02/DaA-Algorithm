class Tho:
  def __init__(self, ten, chiphi):
    self.ten = ten
    self.chiphi = chiphi

def sapXep(arr, n, index):
  for i in range(n-1):
    for j in range(i, n):
      if arr[i].chiphi[index] < arr[j].chiphi[index]:
        arr[i], arr[j] = arr[j], arr[i]

def get(arr, n, index):
  get = arr[n - 1].chiphi[index]
  return get

def greedy(arr, n):
  F = []
  for i in range(n):
    if n == 0:
      break

    sapXep(arr, n, i)
    F.append(get(arr, n, i))
    n -= 1

  return sum(F)

def nhap(n):
  arr = []
  for i in range(n):
    chiphi = []
    for j in range(n):
      x = int(input(f"Nhap chi phi cong viec {j+1} cho tho {i+1}: "))
      chiphi.append(x)
    arr.append(Tho(i, chiphi))

  return arr


if __name__ == "__main__":
  n = int(input("Nhap n: "))
  arr = nhap(n)
  print(greedy(arr, n))
  