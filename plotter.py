import matplotlib.pyplot as plt


def plot_salary_and_travel(x_axis, salaries, travel_expenses):
    x = range(len(x_axis))
    width = 0.35

    plt.figure(figsize=(10, 6))
    salary_bars = plt.bar([p - width / 2 for p in x], salaries, width=width, label='Salary', color='tab:blue')
    travel_bars = plt.bar([p + width / 2 for p in x], travel_expenses, width=width, label='Travel Expense', color='tab:orange')

    plt.xticks(x, x_axis)
    plt.xlabel('Employee')
    plt.ylabel('Amount')
    plt.title('Employee Salary vs Travel Expenses')
    plt.legend()

    for bar, salary, travel in zip(travel_bars, salaries, travel_expenses):
        if salary:
            percent = travel / salary * 100
            plt.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + max(salaries + travel_expenses) * 0.01,
                f"{percent:.1f}%",
                ha='center',
                va='bottom',
                fontsize=8,
                color='black',
            )

    plt.tight_layout()
    plt.savefig('./data/employee_salary_travel.png')
    plt.close()