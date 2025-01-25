import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import matplotlib.pyplot as plt
x = torch.tensor( [12.4, 14.3, 14.5, 14.9, 16.1, 16.9, 16.5, 15.4, 17.0, 17.9, 18.8, 20.3, 22.4,
19.4, 15.5, 16.7, 17.3, 18.4, 19.2, 17.4, 19.5, 19.7, 21.2])
y = torch.tensor( [11.2, 12.5, 12.7, 13.1, 14.1, 14.8, 14.4, 13.4, 14.9, 15.6, 16.4, 17.7, 19.6,
16.9, 14.0, 14.6, 15.1, 16.1, 16.8, 15.2, 17.0, 17.2, 18.6])
w=torch.tensor(1.0,requires_grad=True)
b=torch.tensor(1.0,requires_grad=True)
al=torch.tensor(0.001)
loss=[]
for i in range(10):
    pred=x*w+b
    err=pred-y
    l=torch.sum(err**2)/len(x)
    loss.append(l.item())
    l.backward()
    print(f"Analytical Gradients: w.grad={torch.sum(err * x) / len(x)}, b.grad={torch.sum(err) / len(x)}")
    with torch.no_grad():
        w-=al*w.grad
        b-=al*b.grad
    w.grad.zero_()
    b.grad.zero_()
plt.plot(loss)
plt.show()