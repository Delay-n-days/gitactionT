import time
import machine

# 配置 PB8 为输出
led = machine.Pin('PB8', machine.Pin.OUT)

# 循环 10 次
for i in range(10):
    # LED 闪烁
    led.on()
    time.sleep(0.05)
    led.off()
    time.sleep(0.05)
    
    # 打印信息
    print(f"HelloWorld - Loop {i+1}/10 - Time: {time.time()}")
    time.sleep(0.1)

print("Done!")