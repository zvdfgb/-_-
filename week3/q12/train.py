import torch
from torch import nn

torch.manual_seed(20260907)

x = torch.linspace(-1, 1, 101).reshape(-1, 1)
y = 3 * x - 1

model = nn.Linear(1, 1)
loss_fn = nn.MSELoss()
opt = torch.optim.SGD(model.parameters(), lr=0.1)

for epoch in range(200):
    pred = model(x)
    loss = loss_fn(pred, y)
    
    opt.zero_grad()
    loss.backward()
    opt.step()

model.eval()
with torch.no_grad():
    final_pred = model(x)
    final_loss = loss_fn(final_pred, y).item()
    w = model.weight.item()
    b = model.bias.item()

    print(f"Final Loss: {final_loss:.6f}")
    print(f"Weight: {w:.6f} (Target: 3.0)")
    print(f"Bias: {b:.6f} (Target: -1.0)")

    assert final_loss < 0.001, f"Loss too high: {final_loss}"
    print("Verification PASSED: Final loss is under 0.001.")
