import ast

code_snippet = """
import os
def execute_payload(cmd):
    eval("2 + 2")
    os.system(cmd)
"""

class SecurityVisitor(ast.NodeVisitor):
    def visit_Call(self, node):
        if isinstance(node.func, ast.Name) and node.func.id in ("eval", "exec"):
            print(f"[SECURITY ALERT] 发现高危内置函数调用: {node.func.id} (行号: {node.lineno})")
        self.generic_visit(node)

tree = ast.parse(code_snippet)
SecurityVisitor().visit(tree)
