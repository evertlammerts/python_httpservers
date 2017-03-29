"""
==== 12 threads 1200 connections ====

Running 30s test @ http://127.0.0.1:8889/
  12 threads and 1200 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   264.01ms   70.18ms 641.05ms   77.77%
    Req/Sec   320.91    225.05     2.00k    74.17%
  113181 requests in 30.09s, 17.49MB read
  Socket errors: connect 0, read 1277, write 0, timeout 0
Requests/sec:   3762.01
Transfer/sec:    595.16KB

==== 12 threads 600 connections ====

Running 30s test @ http://127.0.0.1:8889/
  12 threads and 600 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   144.84ms   25.21ms 333.45ms   82.85%
    Req/Sec   328.42    155.79   818.00     57.95%
  116826 requests in 30.10s, 18.05MB read
  Socket errors: connect 0, read 591, write 0, timeout 0
Requests/sec:   3880.96
Transfer/sec:    613.98KB

==== 12 threads 300 connections ====

Running 30s test @ http://127.0.0.1:8889/
  12 threads and 300 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    73.07ms    9.52ms 171.59ms   92.51%
    Req/Sec   333.03     65.10   710.00     67.71%
  119160 requests in 30.04s, 18.41MB read
  Socket errors: connect 0, read 358, write 0, timeout 0
Requests/sec:   3966.78
Transfer/sec:    627.56KB

==== 12 threads 120 connections ====

Running 30s test @ http://127.0.0.1:8889/
  12 threads and 120 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    30.85ms    4.69ms 107.69ms   91.01%
    Req/Sec   326.42     51.79     0.94k    73.32%
  117114 requests in 30.10s, 18.09MB read
Requests/sec:   3891.07
Transfer/sec:    615.58KB

==== 12 threads 12 connections ====

Running 30s test @ http://127.0.0.1:8889/
  12 threads and 12 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     2.98ms  194.19us   8.90ms   94.80%
    Req/Sec   336.86     10.59   750.00     92.36%
  120881 requests in 30.06s, 18.68MB read
Requests/sec:   4021.32
Transfer/sec:    636.18KB
"""
from aiohttp import web

async def handle(request):
    return web.Response(text="hello world")

if __name__ == '__main__':
    app = web.Application()
    app.router.add_get('/', handle)
    web.run_app(app, host='127.0.0.1', port=8889)
