#!/usr/bin/env bash
echo "[$(date +%T)] 主进程启动 (PID: $$)..."

# 启动子任务 1：模拟数据下载（耗时 2 秒）
(
  echo "  -> [Task 1] 正在下载依赖..."
  sleep 2
  echo "  -> [Task 1] 下载完成。"
) &
PID1=$!

# 启动子任务 2：模拟静态扫描（耗时 1 秒）
(
  echo "  -> [Task 2] 正在扫描代码..."
  sleep 1
  echo "  -> [Task 2] 扫描通过。"
) &
PID2=$!

echo "[$(date +%T)] 已并发分发任务: Task1(PID: $PID1), Task2(PID: $PID2)"

# 等待所有后台子进程完成并收集状态
wait $PID1 && echo "[$(date +%T)] Task 1 成功执行完毕"
wait $PID2 && echo "[$(date +%T)] Task 2 成功执行完毕"
echo "[$(date +%T)] 全部并发任务已结束，主进程退出。"
