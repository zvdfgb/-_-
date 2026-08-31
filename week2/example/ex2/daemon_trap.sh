#!/usr/bin/env bash
log() { echo "$(date '+%H:%M:%S') [$1] $2" | tee -a daemon.log; }

trap 'log "SIGNAL" "Caught SIGHUP: Reloading configuration...";' SIGHUP
trap 'log "SIGNAL" "Caught SIGINT/SIGTERM: Cleaning up temp files..."; rm -f temp.pid; log "EXIT" "Shutdown gracefully."; exit 0' INT TERM

echo $$ > temp.pid
log "START" "Daemon running with PID $$"
while true; do
    sleep 2
done