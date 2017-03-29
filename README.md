I use [wrk](https://github.com/wg/wrk) for http tests:

```
$ brew install wrk
```


Install requirements as always:

```
$ pip install -r requirements.txt
```


Start one of the servers, e.g.:

```
$ cd aiohttp
$ python -m hello.uvloop
```


In an other shell, run your tests with `wrk`, e.g.:

```
for n in 1200 600 300 120 12; do
    echo -e "\n==== 12 threads $n connections ====\n"
    wrk -t12 -c$n -d30s http://127.0.0.1:8889/
done
```
