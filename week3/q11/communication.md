# 协作材料规范化改进

## 1. 重写 Issue
**Title**: [Bug] 命令行参数 `--name` 为纯空白字符时未进行有效校验

- **运行环境**: Windows 11 / Python 3.13 (其他系统待确认)
- **复现命令**: `sdt-greet --name "   "`
- **期望结果**: 识别非法输入，向 stderr 输出错误并以状态码 2 退出
- **实际结果**: 输出 `Hello,    !` 并以退出码 0 正常退出

## 2. 重写 Commit Message
fix(cli): reject whitespace-only names with exit code 2

Treat names consisting entirely of whitespace characters as invalid input.
Inspect the stripped argument after parsing; if empty, terminate execution
via sys.exit(2) to prevent printing a greeting for blank names.

## 3. 重写 Code Review 意见
**[Blocking]**: 当前实现未对 `a.name` 执行空白字符校验。当用户传入纯空格参数时，仍会输出 `Hello,   !` 并静默返回 0。该行为不符合参数校验规范。建议在 `parse_args()` 后添加 `if not a.name.strip(): sys.exit(2)`，并补充对应的单元测试覆盖纯空白输入场景。
