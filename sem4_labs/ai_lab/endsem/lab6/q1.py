import random
def f(x):
    return -x**2 + 5*x +10
def hill_climbing():
    x=random.randint(-10,10)
    step_size=0.1
    while True:
        fx=f(x)
        new_x_left=x-step_size
        new_x_right=x+step_size
        if f(new_x_left)>fx:
            x=new_x_left
        elif f(new_x_right)>fx:
            x=new_x_right
        else:
            break
    return x,f(x)
x_optimal, fx_optimal = hill_climbing()
print(f'Optimal solution: x = {round(x_optimal, 3)}, f(x) = {round(fx_optimal, 3)}')