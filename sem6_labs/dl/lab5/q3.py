import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms as transforms
from torchvision import datasets
from torch.utils.data import DataLoader
from tqdm import tqdm
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])
train_dataset = datasets.MNIST(root='./data', train=True, transform=transform, download=True)
test_dataset = datasets.MNIST(root='./data', train=False, transform=transform, download=True)
train_loader = DataLoader(dataset=train_dataset, batch_size=32, shuffle=True)
test_loader = DataLoader(dataset=test_dataset, batch_size=32, shuffle=False)
class ConvNN(nn.Module):
    def __init__(self, ch, ker, l):
        super(ConvNN, self).__init__()
        self.conv = nn.ModuleList([
            nn.Conv2d(in_channels=c, out_channels=ch[i + 1], kernel_size=(k, k))
            for (i, c), k in zip(enumerate(ch[:-1]), ker)
        ])
        self.linear = nn.ModuleList([
            nn.Linear(v, l[i + 1]) for i, v in enumerate(l[:-1])
        ])
        self.pool = nn.MaxPool2d(2, 2)
        self.softmax = nn.Softmax(dim=1)
    def forward(self, x):
        for layer in self.conv:
            x = self.pool(F.relu(layer(x)))
        x = torch.flatten(x, 1)
        for layer in self.linear[:-1]:
            x = F.relu(layer(x))
        x = self.softmax(self.linear[-1](x))
        return x
    def parameter_count(self):
        return sum(p.numel() for p in self.parameters())
def fit(model, train_loader, criterion, optimizer, num_epochs=10):
    model.train()
    model.to(device)
    for epoch in tqdm(range(num_epochs), desc="Epochs", leave=False):
        for local_batch, local_labels in tqdm(train_loader, desc="Batches", leave=False):
            local_batch, local_labels = local_batch.to(device), local_labels.to(device).long()
            optimizer.zero_grad()
            outputs = model(local_batch)
            loss = criterion(outputs, local_labels)
            loss.backward()
            optimizer.step()
def get_confusion_matrix(model, data_loader):
    model.eval()
    y_true, y_pred = [], []
    correct, total = 0, 0
    with torch.no_grad():
        for images, labels in tqdm(data_loader, leave=False):
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            _, predicted = torch.max(outputs.data, 1)
            correct += (predicted == labels).sum().item()
            total += len(labels)
            y_true.extend(labels.cpu().numpy())
            y_pred.extend(predicted.cpu().numpy())
    cf_matrix = confusion_matrix(y_true, y_pred)
    acc = 100 * correct / total
    return cf_matrix, acc
models = {
    "Small": ConvNN(ch=[1, 5, 3],ker=[5, 3],l=[75, 25, 10]),
    "Medium": ConvNN(ch=[1, 64, 128, 64], ker=[5, 3, 3], l=[64, 25, 10]),
    "Large": ConvNN(ch=[1, 128, 256, 64],ker=[5, 3, 3],l=[64, 25, 10])
}
results={}
for name,model in models.items():
    model.to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    criterion = nn.CrossEntropyLoss()
    fit(model, train_loader, criterion, optimizer)
    train_cf, train_acc = get_confusion_matrix(model, train_loader)
    test_cf, test_acc = get_confusion_matrix(model, test_loader)
    param_count = model.parameter_count()
    results[name] = (param_count, test_acc)
    print(f"{name} Model Params: {param_count}, Test Accuracy: {test_acc:.2f}%")
plt.figure(figsize=(8, 5))
for name, (param_count, test_acc) in results.items():
    plt.plot(param_count, test_acc, marker='o', linestyle='-', markersize=8, label=name)
plt.xscale("log")
plt.xlabel("Number of Parameters (log scale)")
plt.ylabel("Accuracy (%)")
plt.title("Model Size vs. Accuracy")
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.legend()
plt.show()