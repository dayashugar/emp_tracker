import plotter
import random

tracked_data = {
    "Arnold" : 0,
    "Harry" : 0,
    "Jhon" : 0,
    "Aman" : 0,
    "Karan" : 0,
}

def credit_salary(emp_name,salary):
    tracked_data[emp_name] = tracked_data.get(emp_name, 0) + salary
    print(f"credited : {emp_name} => {salary} salary.")

for i in range(10):
    random_emp_name = random.choice(list(tracked_data.keys()))
    random_salary = random.randint(0,100000)

    credit_salary(emp_name=random_emp_name, salary=random_salary)

print(f"Plotting employee wise salary as Bar-Graph...")
plotter.plot_bar_graph_v2(x_axis=list(tracked_data.keys()),y_axis=list(tracked_data.values()))