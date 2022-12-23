
import requests
# response = requests.get("http://192.168.178.152")
# print(response)
# print(response.text)
import time

max_t=0
min_t=1
avg=0
for i in range(500):

    time_alt=time.time()
    response = requests.get("http://192.168.178.152")
    delta=time.time()-time_alt
    print(delta)
    avg=avg+delta
    if(delta>max_t):
        max_t=delta
    if (delta < min_t):
        min_t = delta
   # print(response.text)
print("-------")
avg=avg/500
print(avg)
print(min_t)
print(max_t)