from typing import Optional

def find_user_age(user_id: int) -> Optional[int]:
    if user_id > 0:
        return 20
    return None

age = find_user_age(-1)
# 静态检查：未解包 None 直接加减运算应被拦截
print(age + 1)
