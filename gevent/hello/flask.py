"""
==== 12 threads 1200 connections ====

Running 30s test @ http://127.0.0.1:8889/
  12 threads and 1200 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   524.62ms  180.42ms   1.97s    86.40%
    Req/Sec   183.64    119.68     1.77k    72.40%
  64676 requests in 30.10s, 7.90MB read
  Socket errors: connect 0, read 688, write 0, timeout 0
Requests/sec:   2148.45
Transfer/sec:    268.56KB

==== 12 threads 600 connections ====

Running 30s test @ http://127.0.0.1:8889/
  12 threads and 600 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   263.68ms  123.32ms   1.03s    84.06%
    Req/Sec   188.42    140.57     2.57k    77.19%
  64470 requests in 30.06s, 7.87MB read
  Socket errors: connect 0, read 540, write 1, timeout 0
Requests/sec:   2144.65
Transfer/sec:    268.09KB

==== 12 threads 300 connections ====

Running 30s test @ http://127.0.0.1:8889/
  12 threads and 300 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   182.22ms  228.23ms   1.64s    93.19%
    Req/Sec   194.46    179.62     2.60k    96.54%
  64071 requests in 30.09s, 7.82MB read
  Socket errors: connect 0, read 199, write 0, timeout 0
Requests/sec:   2128.97
Transfer/sec:    266.13KB

==== 12 threads 120 connections ====

Running 30s test @ http://127.0.0.1:8889/
  12 threads and 120 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    82.48ms  125.62ms 835.25ms   93.17%
    Req/Sec   196.62    180.21     2.64k    98.11%
  66049 requests in 30.10s, 8.06MB read
Requests/sec:   2194.27
Transfer/sec:    274.29KB

==== 12 threads 12 connections ====

Running 30s test @ http://127.0.0.1:8889/
  12 threads and 12 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     5.51ms    2.65ms  93.23ms   93.92%
    Req/Sec   185.63     24.47     1.10k    93.47%
  66726 requests in 30.08s, 8.15MB read
Requests/sec:   2218.17
Transfer/sec:    277.28KB
"""
from gevent.pywsgi import WSGIServer
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"

if __name__ == '__main__':
    WSGIServer(('', 8889), app, log=None).serve_forever()
