import matplotlib.pyplot as plt


def plot_salary_and_travel(x_axis, salaries, travel_expenses):
    x = range(len(x_axis))
    width = 0.35

    plt.figure(figsize=(10, 6))
    plt.bar([p - width / 2 for p in x], salaries, width=width, label='Salary', color='tab:blue')
    plt.bar([p + width / 2 for p in x], travel_expenses, width=width, label='Travel Expense', color='tab:orange')

    plt.xticks(x, x_axis)
    plt.xlabel('Employee')
    plt.ylabel('Amount')
    plt.title('Employee Salary vs Travel Expenses')
    plt.legend()
    plt.tight_layout()
    plt.savefig('./data/employee_salary_travel.png')
    plt.close()