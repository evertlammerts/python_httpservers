"""
==== 12 threads 1200 connections ====

Running 30s test @ http://127.0.0.1:8889/
  12 threads and 1200 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   463.10ms  261.19ms   1.81s    77.68%
    Req/Sec   183.32    200.26     2.31k    92.90%
  59590 requests in 30.09s, 11.76MB read
  Socket errors: connect 0, read 1492, write 43, timeout 28
Requests/sec:   1980.36
Transfer/sec:    400.33KB

==== 12 threads 600 connections ====

Running 30s test @ http://127.0.0.1:8889/
  12 threads and 600 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   277.61ms  137.85ms   1.14s    79.42%
    Req/Sec   176.49    145.48     2.07k    70.74%
  58239 requests in 30.10s, 11.50MB read
  Socket errors: connect 0, read 713, write 0, timeout 0
Requests/sec:   1935.08
Transfer/sec:    391.17KB

==== 12 threads 300 connections ====

Running 30s test @ http://127.0.0.1:8889/
  12 threads and 300 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   157.22ms  120.92ms 974.68ms   83.99%
    Req/Sec   174.82    132.91     2.30k    94.60%
  58644 requests in 30.09s, 11.58MB read
  Socket errors: connect 0, read 347, write 0, timeout 0
Requests/sec:   1948.68
Transfer/sec:    393.94KB

==== 12 threads 120 connections ====

Running 30s test @ http://127.0.0.1:8889/
  12 threads and 120 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   113.25ms  227.61ms   1.71s    93.84%
    Req/Sec   173.59    124.19     2.16k    97.74%
  57711 requests in 30.10s, 11.39MB read
Requests/sec:   1917.58
Transfer/sec:    387.64KB

==== 12 threads 12 connections ====

Running 30s test @ http://127.0.0.1:8889/
  12 threads and 12 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    18.18ms   70.93ms 744.56ms   96.40%
    Req/Sec   172.19     93.76     2.32k    97.40%
  60749 requests in 30.10s, 11.99MB read
Requests/sec:   2018.02
Transfer/sec:    407.96KB
"""
from gevent.wsgi import WSGIServer
import tornado.wsgi
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


def make_app():
    return tornado.wsgi.WSGIApplication([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    WSGIServer(('', 8889), app, log=None).serve_forever()
