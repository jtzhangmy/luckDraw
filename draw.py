import os
import sys
import tty, termios

os.system('python3 ./loop.py &')
pid = os.popen('pgrep -f loop.py').read()
# 监听按键
while True:
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

# 当按键为Enter时
    if ord(ch) == 13:
        os.system('kill %s' % pid)
        break
