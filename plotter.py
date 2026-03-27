import matplotlib.pyplot as plt

def plot_bar_graph_v2(x_axis, y_axis):    
    plt.bar(x_axis, y_axis, color="red")
    plt.savefig('./data/employee_salary.png')