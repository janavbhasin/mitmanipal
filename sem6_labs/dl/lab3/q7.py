import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
X = torch.tensor([1, 5, 10, 10, 25, 50, 70, 75, 100], dtype=torch.float32).view(-1, 1)
y = torch.tensor([0, 0, 0, 0, 0, 1, 1, 1, 1], dtype=torch.float32).view(-1, 1)
class LogisticRegressionModel(nn.Module):
    def __init__(self):
        super(LogisticRegressionModel, self).__init__()
        self.linear = nn.Linear(1, 1)
    def forward(self, x):
        return torch.sigmoid(self.linear(x))
model = LogisticRegressionModel()
criterion = nn.BCELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)
num_epochs = 1000
losses = []
for epoch in range(num_epochs):
    predictions = model(X)
    loss = criterion(predictions, y)
    losses.append(loss.item())
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
plt.plot(losses)
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Training Loss Curve')
plt.show()
test_input = torch.tensor([[30.0]])
predicted_y = model(test_input).item()
print(f"Predicted probability for X=30: {predicted_y}")
