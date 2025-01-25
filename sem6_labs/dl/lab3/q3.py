import torch
import matplotlib.pyplot as plt
class linear:
    def __init__(self, lr=0.001):
        self.w = torch.randn([1]).requires_grad_(True)
        self.b = torch.randn([1]).requires_grad_(True)
        self.lr = lr
    def forward(self, x):
        return self.w * x + self.b
    def update(self):
        with torch.no_grad():
            self.w -= self.w.grad * self.lr
            self.b -= self.b.grad * self.lr
    def reset_grad(self):
        self.w.grad.zero_()
        self.b.grad.zero_()
    def criteria(self, pred, lab, x):
        err = pred - lab
        print(err)
        print(f"Analytical Gradients: w.grad={torch.sum(err * x) / len(x)}, b.grad={torch.sum(err) / len(x)}")
        return torch.sum((pred - lab) ** 2 / len(lab))
    def fit(self, x, y, ep):
        loss = []
        for i in range(ep):
            pred = self.forward(x)
            l = self.criteria(pred, y, x)
            loss.append(l.item())
            l.backward()
            self.update()
            self.reset_grad()
        return loss
X = torch.Tensor([5, 7, 12, 16, 20])
y = torch.Tensor([40, 120, 180, 210, 240])
m = linear()
z= m.fit(X, y,100)
plt.plot(z)
plt.show()