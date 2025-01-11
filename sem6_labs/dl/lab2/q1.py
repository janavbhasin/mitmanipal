import torch
def func(a, b):
    x = 2 * a + 3 * b
    y = 5 * a**2 + 3 * b**3
    z = 2 * x + 3 * y
    return z
a = torch.tensor(1.0, requires_grad=True)
b = torch.tensor(2.0, requires_grad=True)
z = func(a, b)
z.backward()
print(f"a={a.item()}, b={b.item()}: {a.grad.item()}")
