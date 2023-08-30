import requests
import threading

ENDPOINT = 'https://sandbox.sistock.org/app/export/?op=delivery1'

h = {
    'Authorization': 'Basic foobar',
    'User-Agent': 'curl/7.77.0'
}

def make_request(url, count):
    response = requests.get(url, headers=h)
    print(f"Response from {url}: {response.status_code} {count}")


threads = []

for count,_ in enumerate(range(0,10)):
    count += 1
    thread = threading.Thread(target=make_request, args=(ENDPOINT,count,))
    thread.start()
    threads.append(thread)


for thread in threads:
    thread.join()
