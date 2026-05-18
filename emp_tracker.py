import plotter
import random

tracked_data = {
    "Arnold": {"salary": 0, "travel": 0},
    "Harry": {"salary": 0, "travel": 0},
    "Jhon": {"salary": 0, "travel": 0},
    "Aman": {"salary": 0, "travel": 0},
    "Karan": {"salary": 0, "travel": 0},
}

def credit_salary(emp_name, salary):
    tracked_data[emp_name]["salary"] += salary
    print(f"credited : {emp_name} => {salary} salary.")


def credit_travel_expense(emp_name, expense):
    tracked_data[emp_name]["travel"] += expense
    print(f"recorded : {emp_name} => {expense} travel expense.")

for i in range(10):
    random_emp_name = random.choice(list(tracked_data.keys()))
    random_salary = random.randint(0, 100000)
    random_travel = random.randint(0, 20000)

    credit_salary(emp_name=random_emp_name, salary=random_salary)
    credit_travel_expense(emp_name=random_emp_name, expense=random_travel)

print("\nExpense as percentage of salary:")
for emp_name, values in tracked_data.items():
    salary = values["salary"]
    travel = values["travel"]
    if salary:
        percent = travel / salary * 100
        print(f"  {emp_name}: {percent:.2f}% of salary spent on travel")
    else:
        print(f"  {emp_name}: salary is 0, cannot compute percentage")

print("\nPlotting employee salary and travel expenses as grouped Bar-Graph...")
plotter.plot_salary_and_travel(
    x_axis=list(tracked_data.keys()),
    salaries=[tracked_data[name]["salary"] for name in tracked_data],
    travel_expenses=[tracked_data[name]["travel"] for name in tracked_data],
)