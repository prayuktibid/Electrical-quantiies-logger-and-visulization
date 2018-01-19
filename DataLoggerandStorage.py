from struct import pack, unpack
from time import sleep
from datetime import datetime
from pymodbus.client.sync import ModbusSerialClient as MBClient
from pymodbus.pdu import ModbusRequest
from pymodbus.exceptions import ModbusIOException, ParameterException, ConnectionException
from pytz import timezone
from influxdb import InfluxDBClient, SeriesHelper

def dataWrite(file_name, time2, time1, e, p, v, c, cv, c1, c2, c3):
  file = open(file_name, "a")
  file.write(str(time2)+","+str(time1)+","+str(e)+","+str(p)+","+str(v)+","+str(c)+","+str(cv)+","+str(c1)+","+str(c2)+","+str(c3)+"\n")
  return


def decode_32float(response):
  data = pack('>HH',response.registers[1], response.registers[0])
  return unpack('>i', data)[0]


def readData():
  rq = RTUmaster.read_holding_registers(13716, 1, unit=1)
  rq1 = RTUmaster.read_holding_registers(13720, 1, unit=1)
  rq2 = RTUmaster.read_holding_registers(13696, 2, unit=1)
  rq3 = RTUmaster.read_holding_registers(14722, 2, unit=1)
  rq4 = RTUmaster.read_holding_registers(13716, 1, unit=2)
  rq5 = RTUmaster.read_holding_registers(13720, 1, unit=2)
  rq6 = RTUmaster.read_holding_registers(13696, 2, unit=2)
  rq7 = RTUmaster.read_holding_registers(14722, 2, unit=2)
  rq12 = RTUmaster.read_holding_registers(13872, 1, unit=2)
  rq13 = RTUmaster.read_holding_registers(13874, 1, unit=2)
  rq14 = RTUmaster.read_holding_registers(13876, 1, unit=2)

#Variable to store data of Ener Meter 1
  c1 = float(rq1.registers[0]) * 0.01
  p1 = float(decode_32float(rq2)) * -0.001
  v1 = float(rq.registers[0]) * 0.1
  e1 = float(decode_32float(rq3)) * 0.001
  cv1 = c1 * 3.0
  c11 = float(rq8.registers[0]) * 0.01
  c12 = float(rq9.registers[0]) * 0.01
  c13 = float(rq10.registers[0]) * 0.01

#Variable to store data of Ener Meter 10
  c2 = float(rq5.registers[0]) * 0.01
  p2 = float(decode_32float(rq6)) * -0.001
  v2 = float(rq4.registers[0]) * 0.1
  e2 = float(decode_32float(rq7)) * 0.01
  c21 = float(rq12.registers[0]) * 0.01
  c22 = float(rq13.registers[0]) * 0.01
  c23 = float(rq14.registers[0]) * 0.01
  cv2 = c2 * 3.0
  return e1, p1, v1, c1, cv1, c11, c12, c13, e2, p2, v2, c2, cv2, c21, c22, c23

localtime = timezone('Australia/West')
file_name1 = "/home/oztron/Documents/energylogger31.csv"
file_name2 = "/home/oztron/Documents/energylogger32.csv"
RTUmaster = MBClient(method = "rtu", port = "/dev/ttyUSB0", stopbits = 1, bytesize = 8, parity = 'N', baudrate = 19200, timeout = 10)
connection = RTUmaster.connect()
while connection:
while connection:
  try:
    time1 = datetime.now(localtime).strftime("%Y-%m-%d  %H:%M:%S")
    time2 = datetime.now(localtime).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    energy1, power1, voltage1, current1, avgcurrent1, currentl11, currentl12, currentl13, energy2, power2, voltage2, current2, avgcurrent2, currentl21, currentl22, cur$
    dataWrite(file_name1, time2, time1, energy1, power1, voltage1, current1, avgcurrent1, currentl11, currentl12, currentl13)
    dataWrite(file_name2, time2, time1, energy2, power2, voltage2, current2, avgcurrent2, currentl21, currentl22, currentl23)
    sleep(50)

  except(ModbusIOException, ConnectionException,InfluxDBClientError, InfluxDBServerError): pass

