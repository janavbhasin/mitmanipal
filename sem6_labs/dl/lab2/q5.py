import torch
def func(x):
    return 8 * x**4 + 3 * x**3 + 7 * x**2 + 6 * x + 3
x = torch.tensor(1.0, requires_grad=True)
f = func(x)
f.backward()
print(f"x={x.item()}: {x.grad.item()}")
