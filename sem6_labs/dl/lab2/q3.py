import torch
def func(w, x, b):
    u = w * x
    v = u + b
    a = torch.sigmoid(v)
    return a
w = torch.tensor(2.0, requires_grad=True)
x = torch.tensor(3.0)
b = torch.tensor(1.0)
a = func(w, x, b)
a.backward()
print(f"w={w.item()}, x={x.item()}, b={b.item()}: {w.grad.item()}")