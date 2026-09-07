import torch

# 定义自变量并追踪梯度: z = 2*x^2 + 3*y
x = torch.tensor(3.0, requires_grad=True)
y = torch.tensor(4.0, requires_grad=True)

z = 2 * (x ** 2) + 3 * y
z.backward()

print(f"dz/dx (Theoretical 4*x = 12): {x.grad.item()}")
print(f"dz/dy (Theoretical 3): {y.grad.item()}")

assert x.grad.item() == 12.0 and y.grad.item() == 3.0
print("[Autograd PASSED] Gradients match calculus derivation.")
