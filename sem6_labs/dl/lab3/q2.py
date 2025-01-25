import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
x = torch.tensor([2,4])
y = torch.tensor([20,40])
w=torch.tensor(1.0,requires_grad=True)
b=torch.tensor(1.0,requires_grad=True)
al=torch.tensor(0.001)
for i in range(2):
    pred=x*w+b
    err=pred-y
    l=torch.sum(err**2)/(2*len(x))
    l.backward()
    print(f"Computed Gradients: w.grad={w.grad}, b.grad={b.grad}")
    print(f"Analytical Gradients: w.grad={torch.sum(err * x) / len(x)}, b.grad={torch.sum(err) / len(x)}")
    with torch.no_grad():
        w-=al*w.grad
        b-=al*b.grad
    w.grad.zero_()
    b.grad.zero_()