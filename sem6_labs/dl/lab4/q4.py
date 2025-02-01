import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms as transforms
from torchvision import datasets
from torch.utils.data import DataLoader
from tqdm import tqdm
import matplotlib.pyplot as plt
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])
train_dataset = datasets.MNIST(root='./data', train=True, transform=transform, download=True)
test_dataset = datasets.MNIST(root='./data', train=False, transform=transform, download=True)
train_loader = DataLoader(dataset=train_dataset, batch_size=32, shuffle=True)
test_loader = DataLoader(dataset=test_dataset, batch_size=32, shuffle=False)
class NeuralNetwork(nn.Module):
    def __init__(self, layer_sizes, activation=F.relu):
        super(NeuralNetwork, self).__init__()
        self.linears = nn.ModuleList(
            [nn.Linear(v, layer_sizes[i + 1]) for i, v in enumerate(layer_sizes[:-1])]
        )
        self.activation = activation
    def forward(self, x):
        x = x.view(x.size(0), -1)
        for l in self.linears[:-1]:
            x = self.activation(l(x))
        x = self.linears[-1](x)
        return x
def fit(model, train_data, criterion, optimizer, num_epochs=10):
    losses = []
    for epoch in tqdm(range(num_epochs), desc="Epochs"):
        epoch_loss = 0
        for local_batch, local_labels in tqdm(train_data, desc="Batches", leave=False):
            optimizer.zero_grad()
            loss = criterion(model(local_batch), local_labels.long())
            loss.backward()
            optimizer.step()
            epoch_loss += loss.item()
        losses.append(epoch_loss / len(train_data))
    return losses
def calculate_accuracy(model, data_loader):
    correct = 0
    total = 0
    with torch.no_grad():
        for images, labels in data_loader:
            outputs = model(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    return 100 * correct / total
LEARNING_RATE = 0.003
EPOCHS = 10
model = NeuralNetwork(layer_sizes=[784, 100, 100, 10])
optimizer = torch.optim.Adam(model.parameters(), lr=LEARNING_RATE)
criterion = nn.CrossEntropyLoss()
losses = fit(model, train_loader, criterion, optimizer, num_epochs=EPOCHS)
plt.plot(range(1, len(losses) + 1), losses, marker='o')
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.title("Training Loss vs. Epochs")
plt.grid()
plt.show()
print(f"Train Accuracy: {calculate_accuracy(model, train_loader)}%")
print(f"Test Accuracy: {calculate_accuracy(model, test_loader)}%")
