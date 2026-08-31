import logging

logger = logging.getLogger("AppModule")
logger.setLevel(logging.DEBUG)

fmt = logging.Formatter("%(asctime)s [%(levelname)s] (%(filename)s:%(lineno)d) - %(message)s")

# 文件输出：记录 DEBUG 及以上所有信息
fh = logging.FileHandler("app.log", mode="w", encoding="utf-8")
fh.setLevel(logging.DEBUG)
fh.setFormatter(fmt)

# 控制台输出：仅显示 WARNING 及以上告警
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)
ch.setFormatter(fmt)

logger.addHandler(fh)
logger.addHandler(ch)

def process_number(n):
    logger.debug(f"Handling input n={n}")
    if n < 0:
        logger.warning(f"Negative value detected: {n}")
    if n == 0:
        logger.error("Zero encountered!")
    return 100 / (n if n != 0 else 1)

process_number(10)
process_number(-5)
process_number(0)
