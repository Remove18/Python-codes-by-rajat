def fibonacci():
  n = int(input("Enter any number for fibonacci series:- "))
  a = 0
  b = 1
  if (n==1):
    print(a)
  else:
    print(a)
    print(b)
    for i in range(2,n):
      s = a + b
      a = b
      b = s
      print(s)

if __name__ == "__main__":
  fibonacci()