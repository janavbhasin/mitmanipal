import torch
import torch.nn.functional as F
import torch.nn as nn
image = torch.rand(1, 1, 6, 6)
print(image)
print(image.shape)
m = nn.Conv2d(1, 3, 3, stride=1, padding=0, bias=False)
outimage_nn = m(image)
k = [n.data for n in m.parameters()][0]
outimage_F = F.conv2d(image, k, stride=1, padding=0)
print('using nn.Conv2D')
print(outimage_nn)
print(outimage_nn.size())
print('using F.Conv2D')
print(outimage_F)
print(outimage_F.size())