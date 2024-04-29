import torch
import torch.nn as nn
import torch.nn.functional as F

class LeNetGo2(nn.Module):
    def __init__(self):
        super(LeNetGo, self).__init__()
        self.conv1 = nn.Conv2d(1, 6, 5)  # 입력 채널을 이미지 채널 수에 맞춰 변경
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 1)

    def forward(self, x):
        x = self.pool(torch.relu(self.conv1(x)))
        x = self.pool(torch.relu(self.conv2(x)))
        x = x.view(-1, 16 * 5 * 5)
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = torch.sigmoid(self.fc3(x))
        return x
