import torch
import torch.nn as nn
import torch.optim as optim
import torch.utils.data as data
import matplotlib.pyplot as plt
class LinearRegression(nn.Module):
    def __init__(self):
        super(LinearRegression, self).__init__()
        self.w = nn.Parameter(torch.randn(1))
        self.b = nn.Parameter(torch.randn(1))
    def forward(self, x):
        return self.w * x + self.b
class CustomDataset(data.Dataset):
    def __init__(self, x_data, y_data):
        self.x_data = x_data
        self.y_data = y_data
    def __len__(self):
        return len(self.x_data)
    def __getitem__(self, idx):
        return self.x_data[idx], self.y_data[idx]
X = torch.Tensor([5, 7, 12, 16, 20])
y = torch.Tensor([40, 120, 180, 210, 240])
dataset = CustomDataset(X, y)
dataloader = data.DataLoader(dataset, batch_size=1, shuffle=True)
model = LinearRegression()
optimizer = optim.SGD(model.parameters(), lr=0.001)
criterion = nn.MSELoss()
num_epochs = 100
losses = []
for epoch in range(num_epochs):
    epoch_loss = 0
    for x_batch, y_batch in dataloader:
        optimizer.zero_grad()
        predictions = model(x_batch)
        loss = criterion(predictions, y_batch)
        loss.backward()
        optimizer.step()
        epoch_loss += loss.item()
    losses.append(epoch_loss / len(dataloader))
plt.plot(losses)
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.title("Training Loss")
plt.show()
print(f"Learned Parameters: w = {model.w.item()}, b = {model.b.item()}")