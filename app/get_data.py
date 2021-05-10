import psutil
import MySQLdb as mysql
import time


db = mysql.connect(host="", user="root", passwd="123456", db="devicedata")
db.autocommit(True)
cur = db.cursor()


def getinfo():
    mem = psutil.virtual_memory().percent
    flow = psutil.net_io_counters().packets_sent
    cpu = psutil.cpu_percent(1)
    return cpu,mem,flow


if __name__ == "__main__":
   cpu,mem,flow = getinfo()
   device_id = 1
   time = int(time.time())
   sql = 'insert into device_data(data_cpu,data_memory,data_flow,data_time,device_id) value (%s,%s,%s,%s,%s)' % (cpu, mem, flow, time, device_id)
   cur.execute(sql)


