import sys
import pytest
from greetlab.cli import main


def test_normal_name(capsys, monkeypatch):
    """测试正常传入姓名参数时的正确问候输出"""
    monkeypatch.setattr(sys, "argv", ["sdt-greet", "--name", "Alice"])
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, Alice!"


def test_blank_name_exits_with_code_2(monkeypatch):
    """测试纯空白姓名时程序必须以状态码 2 退出"""
    monkeypatch.setattr(sys, "argv", ["sdt-greet", "--name", "   "])
    with pytest.raises(SystemExit) as exc_info:
        main()
    assert exc_info.value.code == 2
