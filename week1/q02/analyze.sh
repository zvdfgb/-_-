#!/bin/bash

# 1. 检查参数及文件是否存在
if [ $# -eq 0 ] || [ ! -f "$1" ]; then
    echo "Error: File '$1' not found!" >&2
    exit 1
fi

FILE="$1"

# 2. 统计 HTTP 5xx 数量最多的前 2 个 path
echo "Top 2 5xx paths:"
awk -F',' '$4 ~ /^5[0-9]{2}$/ {print $3}' "$FILE" | sort | uniq -c | sort -k1,1nr -k2,2 | head -n 2

# 3. 计算全部数据行的平均 latency_ms
awk -F',' '
    NR > 1 {
        sum += $5
        count++
    }
    END {
        if (count > 0) {
            printf "Average latency: %.2f ms\n", sum / count
        }
    }
' "$FILE"
