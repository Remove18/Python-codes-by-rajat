questions = [
  "Which is the single largest internal organ by mass in the human body?",
  "Which of these is a non-renewable source of energy?",
  "Which of these does the carpenter use to smoothen the surface of a wooden furniture?",
  "A video clip from Manikarnika: The Queen of Jhansi, starring Kangana Ranaut was shown?"
]

optionsofq1 = ["Liver", "Gallbladder", "Kidney", "Stomach"]

optionsofq2 = ["Solar power", "Hydro power", "Wind power", "Natural gas"]

optionsofq3 = ["Butter paper", "Silver paper", "Tissue paper", "Sandpaper"]

optionsofq4 = ["Jhansi", "Gwalior", "Jaipur", "Varanasi"]

money = [
  0,
]
# print(type(totalmoney))

print("\n-:Your question for 10,000rs is:-\n\n", questions[0], "\n")
print("A. " + optionsofq1[0])
print("B. " + optionsofq1[1])
print("C. " + optionsofq1[2])
print("D. " + optionsofq1[3])
answer1 = input("\nAnswer:- ")
if (answer1 == "liver"):
  print("\nyou have given the right answer\n\nYou got 10000rs\n")
  money.append(10000)
else:
  print("\nyour given answer is wrong\n")

print("\n-:Your question for 20,000rs is:-\n\n", questions[1], "\n")
print("A. " + optionsofq2[0])
print("B. " + optionsofq2[1])
print("C. " + optionsofq2[2])
print("D. " + optionsofq2[3])
answer2 = input("\nAnswer:- ")
if (answer2 == "natural gas"):
  print("\nyou have given the right answer\n\nYou got 20000rs\n")
  money.append(20000)
else:
  print("\nyour given answer is wrong\n")

print("\n-:Your question for 50,000rs is:-\n\n", questions[2], "\n")
print("A. " + optionsofq3[0])
print("B. " + optionsofq3[1])
print("C. " + optionsofq3[2])
print("D. " + optionsofq3[3])
answer3 = input("\nAnswer:- ")
if (answer3 == "sandpaper"):
  print("\nyou have given the right answer\n\nYou got 50000rs\n")
  money.append(50000)
else:
  print("\nyour given answer is wrong\n")

print("\n-:Your question for 100,000rs is:-\n\n", questions[3], "\n")
print("A. " + optionsofq4[0])
print("B. " + optionsofq4[1])
print("C. " + optionsofq4[2])
print("D. " + optionsofq4[3])
answer4 = input("\nAnswer:- ")
if (answer4 == "varanasi"):
  print("\nyou have given the right answer\n\nYou got 100000rs\n")
  money.append(100000)
else:
  print("\nyour given answer is wrong\n")

total = 0
for i in money:
  total = total + i
print("Your total winnings are:- ", total)
