import torch
def func(x, y, z):
    a = 2 * x
    b = torch.sin(y)
    c = a / b
    d = c * z
    e = torch.log(d + 1)
    f = torch.tanh(e)
    return f, a, b, c, d, e
x = torch.tensor(1.0, requires_grad=True)
y = torch.tensor(1.0, requires_grad=True)
z = torch.tensor(1.0, requires_grad=True)
f, a, b, c, d, e = func(x, y, z)
f.backward()
print(f"a={a},b={b},c={c},d={d},e={e},f={f},y={y.item()}: {y.grad.item()}")
