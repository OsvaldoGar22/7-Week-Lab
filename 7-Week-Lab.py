import random

# Exercise 1 - Total Sales

# sales = []
#
# week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Firday", "Saturday", "Sunday"]
#
# for day in week:
#     daily_sales = float(input(f"What were the sales like on {day}: $"))
#     sales.append(daily_sales)
#
# print(f"Total sales for the week: ${sum(sales):.2f}")


# -------------------------------------------------------

# Exercise 2 - Lottery Number Generator

# MAX_DIGITS = 7
# START = 0
# END = 9
#
# def main():
#     numbers = [0] * 7
#
#     for index in range(MAX_DIGITS):
#         numbers[index] = random.randint(START, END)
#     
#     print("Here are your lottery numbers: ")
#     
#     for index in range(MAX_DIGITS):
#         print(numbers[index], end='')
#     
#     print()
#
# main()


# -------------------------------------------------------

# Exercise 3 - Rainfall Statistics

# rainfall = []
#
# months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
#
# for month in months:
#     monthly_rainfall = float(input(f"What was the rainfall like in {month}: "))
#     rainfall.append(monthly_rainfall)
#
# total_rainfall = sum(rainfall)
#
# avg_rainfall = total_rainfall / len(months)
#
# most_rainfall = max(rainfall)
# least_rainfall = min(rainfall)
#
# print(f"The total rainfall for the year is {total_rainfall:.2f}.")
# print(f"The monthly average rainfall is {avg_rainfall:.2f}.")
# print(f"The month with the most rainfall was {most_rainfall:.2f}.")
# print(f"The month with the least rainfall was {least_rainfall:.2f}.")

# -------------------------------------------------------

# Exercise 4 -  Number Analysis Program

# nums = []
#
# while len(nums) < 20:
#     print("We need 20 numbers")
#     number = int(input("Enter a number: "))
#     nums.append(number)
#
# highest_num = max(nums)
# lowest_num = min(nums)
# num_total = sum(nums)
# avg_num = num_total / len(nums)
#
# print(f"The total of the numbers was {num_total}.")
# print(f"The average of the numbers was {avg_num}.")
# print(f"The highest number was {highest_num}.")
# print(f"The lowest number was {lowest_num}.")


# -------------------------------------------------------

# Exercise 5 - Charge Account Validation

# with open("charge_accounts.txt", "r") as file:
#     account_numbers = [line.strip() for line in file]
#
# user_account = input("Enter a account number: ")
#
# if user_account in account_numbers:
#     print("The account number is valid.")
# else:
#      print("The account number is invalid.")

# -------------------------------------------------------

# Exercise 6 - Larger Than n

# def larger(lst, n):
#     for num in lst:
#         if num > n:
#             print(num)
#
# nums = [1, 20, 5, 10, 15, 3, 45]
# n = 15
#
# larger(nums, n)

# -------------------------------------------------------

# Exercise 7 - Diver's License Exam

# correct_answers = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']
#
# with open("student_answers.txt", "r") as file:
#     answers = [line.strip() for line in file]
#
# right = 0
# wrong = 0
# wrong_questions = []
#
# for i in range(20):
#     if answers[i] == correct_answers[i]:
#         right += 1
#     else:
#         wrong += 1
#         wrong_questions.append(i + 1)
#
# if right >= 15:
#     print("Nice! you passed the exam.")
# else:
#     print("Study harder.")
#
# print(f"Total right answers: {right}")
# print(f"Total wrong answers: {wrong}")
#
# if wrong_questions:
#     print(f"Questions answered wrong: {wrong_questions}")
# else:
#     print("You got a 100%")

# -------------------------------------------------------

# Exercise 8 - Name Search

# with open("popular_names.txt", "r") as file:
#     popular_names = [line.strip() for line in file]
#     
#     name = input("Enter a name: ").strip()
#     
#     if name in popular_names:
#         print("That was a popular name between 2000 and 2009.")
#     else:
#         print("That was not a popular name between 2000 and 2009.")

# -------------------------------------------------------

# Exercise 9 - Population data 

# with open("USPopulation.txt", "r") as file:
#     population_data = [int(line.strip()) for line in file]
#
# population_changes = []
#
# for i in range(1, len(population_data)):
#     change = population_data[i] - population_data[i - 1]
#     population_changes.append(change)
#
# avg_annual_change = sum(population_changes) / len(population_changes)
#
# most_increase = max(population_changes)
# least_increase = min(population_changes)
#
# year_most_increase = 1950 + population_changes.index(most_increase) + 1
# year_least_increase = 1950 + population_changes.index(least_increase) + 1
#
# print(f"Average annual population change was: {avg_annual_change:.2f}")
# print(f"Year with the most population increase: {year_most_increase}")
# print(f"Year with the least population increase: {year_least_increase}")

# -------------------------------------------------------

# Exercise 10 - World Series Championship

with open("WorldSeriesWinners.txt", "r") as file:
    winners = [line.strip() for line in file]

team_name = input("Enter a team name: ")


wins = winners.count(team_name)

if wins > 0:
    print(f"{team_name} has won the World Series {wins} times.")
else:
    print(f"{team_name} has never won the World Series.")






























