### 介绍

用tornado实现的高性能代理服务器，涵盖了基本的method , 性能方面经过我的测试，他每秒平均在300个访问,如果在tornado加入threadpool逻辑，并发估计会破1k 。

对于https的支持会有些问题，我后期会增强tornado httpclient对于ssl的支持，另外对于高性能方面会加入gevent。

[toproxy 更多介绍](http://xiaorui.cc  "xiaorui.cc")

### 原理
你通过http client附加proxy地址访问页面，我通常会解析你的访问，然后我自己再去访问你刚才提交的页面，然后返回你结果。
当然在协议上来说，这虽然不是最高性能的方法，但是最简单有效的方法....  如果是底层的socket来写，我首先需要解析你的各种各样的header请求，然后还要考虑多任务的模块，或 prefork 或 异步模式， 这都是开发的成本。    我这里是用tornado这异步框架，本身解决了各个流程的堵塞问题，然又用异步的 httpclient,避免了我请求url时的堵塞。 

New Future

1. 加入了白名单功能

2. 当访问的地址连接失败的时候，会做重试机制

更多的httpclient文档，[httpclient 更多文档](http://tornado.readthedocs.org/en/latest/httpclient.html  "tornado httpclient") 

### 安装 

    方法1:
    pip install toproxy

    方法2:
    依赖tornado 
    python setup.py install

### 直接使用
    第一个参数是端口，第二个参数是白名单ip地址。 
    方法1:
    python  -m toproxy/proxy 8888
    python  -m toproxy/proxy 8888 8.8.8.8,114.114.114.114
    ::::Starting HTTP proxy on port 8888

    方法2:
    python toproxy 8888


### 模块的调用

    from toproxy import run_proxy
    run_proxy(port, start_ioloop=False)
    ...
    tornado.ioloop.IOLoop.instance().start()


### test

    curl -vvv -x xiaorui.cc:8888 http://www.google.com

    ab -X xiaorui.cc:8888 -c 200 -n 1000 http://www.hao123.com/ 
    
    ```
    his is ApacheBench, Version 2.3 <$Revision: 655654 $>
    Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
    Licensed to The Apache Software Foundation, http://www.apache.org/
    
    Benchmarking www.hao123.com (be patient)
    Completed 100 requests
    Completed 200 requests
    Completed 300 requests
    Completed 400 requests
    Completed 500 requests
    Completed 600 requests
    Completed 700 requests
    Completed 800 requests
    Completed 900 requests
    Completed 1000 requests
    Finished 1000 requests
    
    
    Server Software:        BWS/1.0
    Server Hostname:        www.hao123.com
    Server Port:            80
    
    Document Path:          /
    Document Length:        750380 bytes
    
    Concurrency Level:      200
    Time taken for tests:   7.967 seconds
    Complete requests:      1000
    Failed requests:        10
       (Connect: 0, Receive: 0, Length: 10, Exceptions: 0)
    Write errors:           0
    Total transferred:      752184936 bytes
    HTML transferred:       751671400 bytes
    Requests per second:    125.52 [#/sec] (mean)
    Time per request:       1593.406 [ms] (mean)
    Time per request:       7.967 [ms] (mean, across all concurrent requests)
    Transfer rate:          92199.44 [Kbytes/sec] received
    
    Connection Times (ms)
                  min  mean[+/-sd] median   max
    Connect:       24   40  94.6     31    1034
    Processing:   289 1371 786.8   1223    4028
    Waiting:       46   57  27.8     55     663
    Total:        317 1411 791.2   1276    4059
    
    Percentage of the requests served within a certain time (ms)
      50%   1276
      66%   1751
      75%   2030
      80%   2208
      90%   2510
      95%   2768
      98%   3187
      99%   3389
     100%   4059 (longest request)
    ```

### todo

1.  提高toproxy的性能
2.  加入重试机制
3.  加入异步回调通知模式
4.  批量传送

