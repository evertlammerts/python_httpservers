"""
==== 12 threads 1200 connections ====

Running 30s test @ http://127.0.0.1:8889/
  12 threads and 1200 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   409.57ms  161.89ms 677.04ms   60.19%
    Req/Sec   188.61    173.54     0.95k    74.11%
  60583 requests in 30.09s, 11.96MB read
  Socket errors: connect 0, read 1523, write 4, timeout 0
Requests/sec:   2013.67
Transfer/sec:    407.06KB

==== 12 threads 600 connections ====

Running 30s test @ http://127.0.0.1:8889/
  12 threads and 600 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   275.88ms   69.84ms 470.53ms   80.32%
    Req/Sec   171.30    130.72   626.00     63.51%
  58617 requests in 30.07s, 11.57MB read
  Socket errors: connect 0, read 773, write 31, timeout 0
Requests/sec:   1949.05
Transfer/sec:    394.00KB

==== 12 threads 300 connections ====

Running 30s test @ http://127.0.0.1:8889/
  12 threads and 300 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   138.92ms   19.81ms 247.67ms   90.61%
    Req/Sec   173.67     65.88   500.00     62.71%
  62142 requests in 30.10s, 12.27MB read
  Socket errors: connect 0, read 286, write 0, timeout 0
Requests/sec:   2064.39
Transfer/sec:    417.31KB

==== 12 threads 120 connections ====

Running 30s test @ http://127.0.0.1:8889/
  12 threads and 120 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    60.74ms    8.64ms 211.09ms   94.20%
    Req/Sec   165.68     40.90   202.00     75.98%
  59439 requests in 30.09s, 11.73MB read
Requests/sec:   1975.49
Transfer/sec:    399.34KB

==== 12 threads 12 connections ====

Running 30s test @ http://127.0.0.1:8889/
  12 threads and 12 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     5.90ms  739.45us  27.60ms   93.74%
    Req/Sec   170.26     10.36   181.00     84.64%
  61240 requests in 30.09s, 12.09MB read
Requests/sec:   2035.43
Transfer/sec:    411.46KB
"""

import asyncio
import uvloop
import tornado.ioloop
from tornado.platform.asyncio import AsyncIOMainLoop
import tornado.web

# set uvloop as the default asyncio event loop
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
# install asyncio's eventloop as the default for tornado
AsyncIOMainLoop().install()


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8889)
    tornado.ioloop.IOLoop.current().start()
