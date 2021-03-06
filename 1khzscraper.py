#!/usr/bin/python3.7
\
import time
import board
import adafruit_mpu6050
i2c = board.I2C()  # uses board.SCL and board.SDA
mpu = adafruit_mpu6050.MPU6050(i2c)
#fill list with n samples with time counter
def imu_data_scraper():
    n = 1000
    adata_array = [0] * n
    gdata_array = [0] * n
    i = 0
    mpu.sleep= False
    mpu.acceleration
    now1 = time.time_ns()
    while i < 1000:
        time_stamp = ((time.time_ns()) - (now1))
        adata_array[i] = (time_stamp, mpu.acceleration)
        time_stamp = ((time.time_ns()) - (now1))
        gdata_array[i] = (time_stamp, mpu.gyro)
        i += 1
        #1khz
        time.sleep(.00013)
        #200hz
        #time.sleep(.00364)
    now2 = time.time_ns()
    now3 = (now2 - now1)
    #print(adata_array, gdata_array)
    print( now2, “-”, now1,“=”, now3 )
    #return str(data_array)
imu_data_scraper()
