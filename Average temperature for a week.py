Days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
Temp = []

for Day in Days:
    temp = float(input(f"Enter the Temperature of {Day}: "))
    Temp.append(temp)
Total_temp = sum(Temp)
Avg_temp = Total_temp / len(Days)

print(f"The avg. temp. for the week is: {Avg_temp:.2f}")