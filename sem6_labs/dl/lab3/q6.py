import torch
import torch.nn as nn
import torch.optim as optim
X = torch.tensor([[2, 3], [4, 5], [3, 7], [4, 3], [5, 6], [3, 5], [2, 5], [4, 2], [1, 3], [3, 1],
                  [2, 2], [3, 4], [1, 5], [2, 4], [3, 6], [4, 7], [5, 5], [4, 3], [2, 6], [5, 3],
                  [3, 4], [1, 2], [3, 3]]).float()
y = torch.tensor([3.7, 2.5, 11.5, 5.7, 4.2, 6.1, 3.4, 4.9, 1.8, 3.0, 5.5, 4.0, 5.3, 2.9, 7.0, 5.1, 6.3,
                  4.7, 4.0, 3.8, 5.6, 3.4, 4.3]).view(-1, 1)
class LinearRegressionModel(nn.Module):
    def __init__(self):
        super(LinearRegressionModel, self).__init__()
        self.linear = nn.Linear(2, 1)
    def forward(self, x):
        return self.linear(x)
model = LinearRegressionModel()
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.001)
num_epochs = 100
for epoch in range(num_epochs):
    predictions = model(X)
    loss = criterion(predictions, y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
print(f"Learned Parameters: Weight = {model.linear.weight.data}, Bias = {model.linear.bias.data}")
test_input = torch.tensor([[3.0, 2.0]])
predicted_y = model(test_input).item()
print(f"Predicted Y for X1=3, X2=2: {predicted_y}")