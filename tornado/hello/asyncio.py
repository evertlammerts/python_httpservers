"""
==== 12 threads 1200 connections ====

Running 30s test @ http://127.0.0.1:8889/
  12 threads and 1200 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   510.32ms  136.03ms   1.13s    81.16%
    Req/Sec   171.06    134.53   700.00     73.07%
  58348 requests in 30.09s, 11.52MB read
  Socket errors: connect 0, read 1246, write 0, timeout 0
Requests/sec:   1938.95
Transfer/sec:    391.95KB

==== 12 threads 600 connections ====

Running 30s test @ http://127.0.0.1:8889/
  12 threads and 600 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   292.69ms   41.76ms 816.66ms   94.38%
    Req/Sec   166.42     51.02   320.00     68.05%
  58236 requests in 30.10s, 11.50MB read
  Socket errors: connect 0, read 507, write 11, timeout 0
Requests/sec:   1934.76
Transfer/sec:    391.11KB

==== 12 threads 300 connections ====

Running 30s test @ http://127.0.0.1:8889/
  12 threads and 300 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   156.21ms   32.94ms 378.88ms   83.13%
    Req/Sec   155.26     72.51   505.00     64.92%
  54707 requests in 30.09s, 10.80MB read
  Socket errors: connect 0, read 324, write 0, timeout 0
Requests/sec:   1818.06
Transfer/sec:    367.52KB

==== 12 threads 120 connections ====

Running 30s test @ http://127.0.0.1:8889/
  12 threads and 120 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    65.03ms   17.47ms 316.74ms   92.72%
    Req/Sec   157.29     45.21   202.00     69.31%
  56035 requests in 30.09s, 11.06MB read
Requests/sec:   1862.34
Transfer/sec:    376.47KB

==== 12 threads 12 connections ====

Running 30s test @ http://127.0.0.1:8889/
  12 threads and 12 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     6.22ms    1.80ms  56.69ms   97.09%
    Req/Sec   163.36     16.56   292.00     91.39%
  58747 requests in 30.10s, 11.60MB read
Requests/sec:   1951.74
Transfer/sec:    394.54KB
"""

import tornado.ioloop
from tornado.platform.asyncio import AsyncIOMainLoop
import tornado.web

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
