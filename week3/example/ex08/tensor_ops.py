import torch

torch.manual_seed(20260907)
# 广播相加演示
A = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]) # 形状 (2, 3)
B = torch.tensor([10.0, 20.0, 30.0])                  # 形状 (3,)
broadcast_sum = A + B

# 矩阵乘法
C = torch.tensor([[1.0], [2.0], [3.0]])               # 形状 (3, 1)
matmul_res = torch.matmul(A, C)                       # 形状 (2, 1)

print("A + B (Broadcasting):\n", broadcast_sum)
print("A @ C (Matmul Result):\n", matmul_res)
assert matmul_res.shape == (2, 1)
