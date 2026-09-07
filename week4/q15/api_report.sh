#!/usr/bin/env bash
set -e

API_URL="http://127.0.0.1:8000/packages.json"
OUTPUT_FILE="summary.md"

# 1. 发起 HTTP 请求获取 API 数据
RAW_DATA=$(curl -fsS "$API_URL")

# 2. 写入 Markdown 表头
cat << 'TABLE_HEAD' > "$OUTPUT_FILE"
# Package Summary Report

| Name | Version | Downloads |
| :--- | :--- | :--- |
TABLE_HEAD

# 3. 使用 jq 过滤、排序并格式化输出 Markdown 表格行
echo "$RAW_DATA" | jq -r '
  map(select(.status == "active" and .downloads >= 100))
  | sort_by([-.downloads, .name])[]
  | "| \(.name) | \(.version) | \(.downloads) |"
' >> "$OUTPUT_FILE"

echo ">>> Generated $OUTPUT_FILE successfully: <<<"
cat "$OUTPUT_FILE"
