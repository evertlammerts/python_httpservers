"""
==== 12 threads 1200 connections ====

Running 30s test @ http://127.0.0.1:8889/
  12 threads and 1200 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   166.46ms   75.28ms 379.04ms   56.75%
    Req/Sec   499.58    231.16     1.45k    77.40%
  173354 requests in 30.08s, 26.78MB read
  Socket errors: connect 0, read 1299, write 25, timeout 0
Requests/sec:   5762.80
Transfer/sec:      0.89MB

==== 12 threads 600 connections ====

Running 30s test @ http://127.0.0.1:8889/
  12 threads and 600 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    95.37ms   36.49ms 211.27ms   69.33%
    Req/Sec   486.68    154.29     1.05k    68.51%
  174310 requests in 30.09s, 26.93MB read
  Socket errors: connect 0, read 548, write 0, timeout 0
Requests/sec:   5793.61
Transfer/sec:      0.90MB

==== 12 threads 300 connections ====

Running 30s test @ http://127.0.0.1:8889/
  12 threads and 300 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    48.93ms   17.33ms 151.46ms   63.17%
    Req/Sec   493.12    118.90     1.28k    74.95%
  175910 requests in 30.09s, 27.18MB read
  Socket errors: connect 0, read 295, write 0, timeout 0
Requests/sec:   5845.29
Transfer/sec:      0.90MB

==== 12 threads 120 connections ====

Running 30s test @ http://127.0.0.1:8889/
  12 threads and 120 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    21.14ms    9.38ms 184.59ms   79.84%
    Req/Sec   485.60     96.46     1.19k    76.54%
  174208 requests in 30.07s, 26.91MB read
Requests/sec:   5794.12
Transfer/sec:      0.90MB

==== 12 threads 12 connections ====

Running 30s test @ http://127.0.0.1:8889/
  12 threads and 12 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     2.30ms    1.34ms  49.76ms   95.14%
    Req/Sec   453.26     64.47     0.87k    86.08%
  162688 requests in 30.07s, 25.13MB read
Requests/sec:   5410.63
Transfer/sec:    855.98KB
"""
import asyncio
from aiohttp import web
import uvloop

async def handle(request):
    return web.Response(text="hello world")

if __name__ == '__main__':
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    app = web.Application()
    app.router.add_get('/', handle)
    web.run_app(app, host='127.0.0.1', port=8889)
