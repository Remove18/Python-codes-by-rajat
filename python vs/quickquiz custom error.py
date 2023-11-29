salary = input("Enter salary amount: ")
if salary == "quit":
  print("you quit the questening.")
  exit()
elif not 2000 < int(salary) < 5000:
    raise ValueError("Not a valid salary")