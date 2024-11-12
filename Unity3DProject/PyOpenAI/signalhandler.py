import signal

# 自定义信号处理函数
def handler(signum, frame):
    global stop
    stop = True
    print("终止")


# 设置相应信号处理的handler
signal.signal(signal.SIGINT, handler)  # 读取Ctrl+c信号
# signal.signal(signal.SIGHUP, my_handler)
# signal.signal(signal.SIGTERM, my_handler)

stop = False

while True:
    try:
        # 读取到Ctrl+c前进行的操作
        if stop:
            # 中断时需要处理的代码
            break  # break只能退出当前循坏
            # 中断程序需要用 raise
    except Exception as e:
        print(str(e))
        break
