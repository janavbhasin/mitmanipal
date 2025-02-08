import torch
import torch.nn.functional as F
image = torch.rand(1, 1, 6, 6)
kernel = torch.rand(1, 1, 3, 3)
for stride in [1, 2]:
    for padding in [0, 1]:
        outimage = F.conv2d(image, kernel, stride=stride, padding=padding)
        print(f"Stride: {stride}, Padding: {padding}, Output Shape: {outimage.shape}")