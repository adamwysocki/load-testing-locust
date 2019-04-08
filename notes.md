
# Setup master
locust -f locustfile.py --master --expect-slaves=10

# Setup slave(s)
locust -f locustfile.py --slave --master-host=xxx.xxx.xx.xx

