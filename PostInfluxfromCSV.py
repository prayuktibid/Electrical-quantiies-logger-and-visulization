from influxdb import InfluxDBClient, SeriesHelper
from influxdb.exceptions import InfluxDBClientError, InfluxDBServerError
import time
import pandas as pd

host = '35.166.113.128'
port = 8086
user = 'root'
password = 'root'
dbname = 'northam1'
client = InfluxDBClient(host, port, user, password, dbname)
client.create_database(dbname)

def readCsv(file, i):
  data = pd.read_csv(file, header = None)
  t = data.iloc[i,0]
  e = data.iloc[i,2]
  p = data.iloc[i,3]
  v = data.iloc[i,4]
  c = data.iloc[i,5]
  i = i + 1
  return t, e, p, v, c, i


file1 = "/home/oztron/Documents/energylogger31.csv"
file2 = "/home/oztron/Documents/energylogger32.csv"
index1 = 0
index2 = 0
while True:
  try:
    time1, e1, p1, v1, c1, i = readCsv(file1, index1)
    time2, e2, p2, v2, c2, j = readCsv(file2, index2)
    index1 = i
    index2 = j
    client.write_points([{"measurement": "Energy_Meter1", "tags":{"host": "RaspbarryPi", "Region": "Northam"}, "time":time1, "fields":{"Energy": e1, "Power": p1, "Volt$
    client.write_points([{"measurement": "Energy_Meter2", "tags":{"host": "RaspbarryPi", "Region": "Northam"}, "time":time2, "fields":{"Energy": e2, "Power": p2, "Volt$
    time.sleep(60)
  except(InfluxDBClientError, InfluxDBServerError): pass

    
