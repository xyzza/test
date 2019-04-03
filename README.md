# Задание
- Написать на Python 3 асинхронный HTTP сервер, который считает пришедшие запросы.
- Можно получать запросом текущее значение счетчика сообщений.
- Провести нагрузочное тестирование сервера (можно использовать любые пакеты) и показать кол-во RPS.
- Код предоставить в любом git совместимом репо.


# Запуск в Docker
выполнить из корня проекта:

    docker-compose up


## Benchmarks:

Для замеров использовалась утилита **wrk** https://github.com/giltene/wrk2

```bash
localhost 
osX 10.13.6
mem: 16 GB 2400 MHz DDR4
cpu: 2,2 GHz Intel Core i7

PostgreSQL 9.6 default settings (no tuning)
```


**default asyncio loop**

    2300 RPS
```bash
wrk -t4 -c100 -d30s http://localhost:8080
Running 30s test @ http://localhost:8080
  4 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    42.58ms    4.25ms 151.98ms   96.75%
    Req/Sec   591.21     40.91   710.00     71.91%
  70569 requests in 30.04s, 10.42MB read
Requests/sec:   2349.50
Transfer/sec:    355.28KB

```
**uvloop**
 
    2800 RPS
```bash
wrk -t4 -c100 -d30s http://localhost:8080
Running 30s test @ http://localhost:8080
  4 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    91.17ms  151.67ms   1.70s    88.13%
    Req/Sec   705.70    163.61     1.55k    72.17%
  84380 requests in 30.04s, 12.50MB read
Requests/sec:   2808.89
Transfer/sec:    426.15KB

```

## В default Docker контейнере на localhost

**default asyncio loop:**

    1500 RPS
```bash
wrk -t4 -c100 -d30s http://localhost:8080
Running 30s test @ http://localhost:8080
  4 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    65.78ms    7.22ms 181.00ms   91.29%
    Req/Sec   382.04     40.85   484.00     74.16%
  45610 requests in 30.05s, 6.73MB read
  Socket errors: connect 0, read 85, write 0, timeout 0
Requests/sec:   1518.05
Transfer/sec:    229.42KB

```

**uvloop:**
 
    1600
```bash
wrk -t4 -c100 -d30s http://localhost:8080
Running 30s test @ http://localhost:8080
  4 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   193.20ms  338.51ms   1.99s    86.23%
    Req/Sec   420.37    133.42     0.91k    70.50%
  50256 requests in 30.03s, 7.43MB read
  Socket errors: connect 0, read 80, write 0, timeout 166
Requests/sec:   1673.51
Transfer/sec:    253.31KB
```
