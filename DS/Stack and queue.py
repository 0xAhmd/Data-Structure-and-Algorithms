# implement stack in pyhton "LIFO"

web_history = []
web_history.append(1)
web_history.append(2)
web_history.append(3)
print(web_history)
web_history.pop()
print(web_history)
web_history.pop()
print(web_history)
web_history.pop()
if not web_history:
    print("web history is empty")

########################################################################################################################################

# implement queue in pyhton "FIFO"
from collections import deque
maque  = deque([])
maque.append(1)
maque.append(2)
maque.append(3)
maque.append(4)
maque.popleft()
maque.popleft()
maque.popleft()
maque.popleft()
#if not maque:
   # print("the queue is finished!")




