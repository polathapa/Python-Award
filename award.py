#Welcome message
print("Welcome to the triathalon award calculator!")
#User input: minutes per activity saved as int
cycling = int(input("How many minutes did it take you to cycle?🚴\n"))
running = int(input("How many minutes did it take you to run?🏃\n"))
swimming = int(input("How many minutes did it take you to swim?🏊‍♀️\n"))
#Total time calculated and printed using funciton
total_time = cycling + swimming + running
print(f"Your total time was {total_time} minutes. Congratulations!")
#Award calculated based on time
if total_time <= 100:
  print("Your award is: Provincial Colours! 🥇")
elif total_time <= 105:
  print("Your award is: Provincial Half Colours! 🥈")
elif total_time <= 110:
  print("Your award is: a Provincial Scroll! 🥉")
elif total_time >= 111:
  print("No award but thanks for participating! 🏅")
