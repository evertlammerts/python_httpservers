"""
==== 12 threads 1200 connections ====

Running 30s test @ http://127.0.0.1:8889/
  12 threads and 1200 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   385.73ms  555.93ms   1.98s    81.17%
    Req/Sec   577.99    805.66     4.13k    87.95%
  111486 requests in 30.10s, 13.82MB read
  Socket errors: connect 0, read 1099, write 61, timeout 3080
Requests/sec:   3703.40
Transfer/sec:    470.16KB

==== 12 threads 600 connections ====

Running 30s test @ http://127.0.0.1:8889/
  12 threads and 600 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   305.63ms  361.14ms   1.72s    78.03%
    Req/Sec   373.76    443.63     4.08k    89.48%
  109611 requests in 30.09s, 13.59MB read
  Socket errors: connect 0, read 410, write 12, timeout 28
Requests/sec:   3642.77
Transfer/sec:    462.47KB

==== 12 threads 300 connections ====

Running 30s test @ http://127.0.0.1:8889/
  12 threads and 300 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   151.60ms  188.23ms   1.88s    79.47%
    Req/Sec   346.66    375.12     3.69k    88.30%
  108347 requests in 30.04s, 13.43MB read
  Socket errors: connect 0, read 310, write 0, timeout 286
Requests/sec:   3607.09
Transfer/sec:    457.94KB

==== 12 threads 120 connections ====

Running 30s test @ http://127.0.0.1:8889/
  12 threads and 120 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   111.92ms  204.36ms   1.89s    94.02%
    Req/Sec   331.67    386.66     3.92k    94.22%
  99130 requests in 30.08s, 12.29MB read
Requests/sec:   3295.06
Transfer/sec:    418.33KB

==== 12 threads 12 connections ====

Running 30s test @ http://127.0.0.1:8889/
  12 threads and 12 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    13.89ms   58.14ms 768.96ms   97.38%
    Req/Sec   299.96    238.92     4.03k    87.27%
  105297 requests in 30.09s, 13.05MB read
Requests/sec:   3499.31
Transfer/sec:    444.26KB
"""
from gevent.pywsgi import WSGIServer


def application(environ, start_response):
    status = '200 OK'

    headers = [
        ('Content-Type', 'text/html')
    ]

    start_response(status, headers)
    yield b'hello world'


if __name__ == '__main__':
    WSGIServer(('', 8889), application, log=None).serve_forever()
