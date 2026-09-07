# 使用 jq 按部门分组并统计各部门总预算
jq '
  group_by(.dept)
  | map({department: .[0].dept, total_budget: map(.amount) | add})
' transactions.json
