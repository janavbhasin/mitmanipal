import torch
def func(x):
    return torch.exp(-x**2 - 2*x - torch.sin(x))
x = torch.tensor(1.0, requires_grad=True)
f = func(x)
f.backward()
print(f"x={x.item()}: {x.grad.item()}")
