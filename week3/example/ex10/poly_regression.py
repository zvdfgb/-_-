import torch
import torch.nn as nn
from torch.optim.lr_scheduler import StepLR

torch.manual_seed(20260907)
# 准备二次多项式特征 [x, x^2]
x_raw = torch.linspace(-2, 2, 200).unsqueeze(1)
X = torch.cat([x_raw, x_raw ** 2], dim=1) # 形状 (200, 2)
y = 1.0 - 2.0 * x_raw + 0.5 * (x_raw ** 2)

model = nn.Linear(2, 1)
loss_fn = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.1)
scheduler = StepLR(optimizer, step_size=100, gamma=0.5)

for epoch in range(300):
    pred = model(X)
    loss = loss_fn(pred, y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    scheduler.step()

model.eval()
with torch.no_grad():
    final_loss = loss_fn(model(X), y).item()
    print(f"Poly Fit Final Loss: {final_loss:.6f}")
    assert final_loss < 0.001
    print("[Poly Fit PASSED] Non-linear polynomial regression converged successfully.")
