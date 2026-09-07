1. 核心提示：要求检测到 name 全为空白字符时调用 sys.exit(2) 退出，满足失败测试。
2. 智能体改动：在 parse_args() 后增加 if not a.name.strip(): sys.exit(2) 逻辑分支。
3. 人工审查：审查 diff 确认无多余依赖和修改，保留原有参数解析逻辑。
4. 验证结果：重新执行 pytest，test_blank_name_exits_with_code_2 测试通过。
