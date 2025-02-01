import torch 
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader,Dataset
import matplotlib.pyplot as plt
plt.style.use("seaborn-v0_8")
class NeuralNetwork(nn.Module):
    def __init__(self,layers,active=F.relu):
        super(NeuralNetwork,self).__init__()
        self.linears=nn.ModuleList([nn.Linear(v,layers[i+1])for i,v in enumerate(layers[:-1])])
        self.active=active
    def forward(self,x):
        for l in self.linears[:-1]:
            x=self.active(l(x))
        x=self.linears[-1](x)
        x=torch.sigmoid(x)
        return x    
x = torch.Tensor([[0, 0], [0, 1], [1, 0], [1, 1]])
y = torch.Tensor([0, 1, 1, 0]).reshape(-1, 1)
class xor(Dataset):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __len__(self):
        return len(self.y)
    def __getitem__(self,index):
        return self.x[index],self.y[index]
xo=xor(x,y)
xoo=DataLoader(xo,batch_size=4,shuffle=True)
learn=0.001
epochs=20000
layers=[2,2,1]
xorr=NeuralNetwork(layers,active=F.sigmoid)
crit=nn.BCELoss()
optim=torch.optim.Adam(xorr.parameters(),lr=learn)
losses=[]
for ep in range(epochs):
    ep_loss=0
    for bat_i,bat_l in xoo:
        optim.zero_grad()
        op=xorr(bat_i)
        loss=crit(op,bat_l)
        loss.backward()
        optim.step()
        ep_loss+=loss.item()
    losses.append(ep_loss/len(xoo))
print(f"Final loss = {losses[-1]}")
plt.plot(range(epochs), losses)
plt.show()
preds = xorr(x)
print(preds)
params = dict(xorr.named_parameters())
Xd = x
l1_out = Xd @ params['linears.0.weight'].t() + params['linears.0.bias']
l1_act = F.sigmoid(l1_out)
l2_out = l1_act @ params['linears.1.weight'].t() + params['linears.1.bias']
l2_act = F.sigmoid(l2_out)
print(l2_act)
for k,v  in params.items():
    print(k, v)