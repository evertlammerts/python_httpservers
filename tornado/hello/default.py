"""
==== 12 threads 1200 connections ====

Running 30s test @ http://127.0.0.1:8889/
  12 threads and 1200 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   466.95ms  185.33ms 865.89ms   73.29%
    Req/Sec   185.02    177.26   800.00     81.22%
  57030 requests in 30.09s, 11.26MB read
  Socket errors: connect 0, read 1402, write 8, timeout 0
Requests/sec:   1895.03
Transfer/sec:    383.08KB

==== 12 threads 600 connections ====

Running 30s test @ http://127.0.0.1:8889/
  12 threads and 600 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   285.93ms   60.41ms 619.85ms   82.37%
    Req/Sec   162.37    109.98   570.00     61.21%
  56305 requests in 30.10s, 11.12MB read
  Socket errors: connect 0, read 694, write 0, timeout 0
Requests/sec:   1870.51
Transfer/sec:    378.12KB

==== 12 threads 300 connections ====

Running 30s test @ http://127.0.0.1:8889/
  12 threads and 300 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   148.09ms   36.42ms 347.05ms   87.22%
    Req/Sec   163.17     67.68   505.00     67.23%
  57645 requests in 30.09s, 11.38MB read
  Socket errors: connect 0, read 365, write 0, timeout 0
Requests/sec:   1915.78
Transfer/sec:    387.27KB

==== 12 threads 120 connections ====

Running 30s test @ http://127.0.0.1:8889/
  12 threads and 120 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    58.75ms    4.68ms 158.51ms   95.94%
    Req/Sec   171.24     38.54   202.00     77.23%
  61369 requests in 30.08s, 12.11MB read
Requests/sec:   2040.36
Transfer/sec:    412.46KB

==== 12 threads 12 connections ====

Running 30s test @ http://127.0.0.1:8889/
  12 threads and 12 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     6.09ms    1.55ms  53.57ms   93.87%
    Req/Sec   165.82     20.03   313.00     85.83%
  59637 requests in 30.09s, 11.77MB read
Requests/sec:   1981.76
Transfer/sec:    400.61KB
"""

import tornado.ioloop
import tornado.web


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
