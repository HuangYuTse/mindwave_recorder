import datetime
from NeuroPy import NeuroPy
import time
import csv
import serial.tools.list_ports
import keyboard


# from matplotlib import pyplot as plt


class TimeFunction:
    def __init__(self):
        self.dtime = datetime.datetime.now()
        self.ans_time = time.mktime(self.dtime.timetuple())

    def get_unix_time(self):
        self.dtime = datetime.datetime.now()
        self.ans_time = time.mktime(self.dtime.timetuple())
        return self.ans_time

    def get_unix_time_int(self):
        self.dtime = datetime.datetime.now()
        self.ans_time = int(time.mktime(self.dtime.timetuple()))
        return self.ans_time

    def get_unix_time_str(self):
        self.dtime = datetime.datetime.now()
        self.ans_time = str(int(time.mktime(self.dtime.timetuple())))
        return self.ans_time


def attention_callback(attention_value):
    """this function will be called everytime NeuroPy has a new value for attention"""
    global attention_no_data
    global attention_file_name

    print("Value of attention is: ", attention_value)

    if attention_value != 0:
        attention_no_data = True
    else:
        pass
    if attention_no_data:
        with open(attention_file_name, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([TimeFunction().get_unix_time_str(),attention_value])
            csvfile.close()
    else:
        pass
    return None


def meditation_callback(meditation_value):
    """this function will be called everytime NeuroPy has a new value for meditation"""
    global meditation_no_data
    global meditation_file_name

    print("Value of meditation is: ", meditation_value)

    if meditation_value != 0:
        meditation_no_data = True
    else:
        pass
    if meditation_no_data:
        with open(meditation_file_name, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([TimeFunction().get_unix_time_str(),meditation_value])
            csvfile.close()
    else:
        pass
    return None


def rawValue_callback(rawValue_value):
    """this function will be called everytime NeuroPy has a new value for rawValue"""
    global rawValue_no_data
    global rawValue_file_name

    # print("Value of rawValue is: ", rawValue_value)

    if rawValue_value != 0:
        rawValue_no_data = True
    else:
        pass
    if rawValue_no_data:
        with open(rawValue_file_name, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([TimeFunction().get_unix_time_str(),rawValue_value])
            csvfile.close()
    else:
        pass
    return None


def delta_callback(delta_value):
    """this function will be called everytime NeuroPy has a new value for delta"""
    global delta_no_data
    global delta_file_name

    print("Value of delta is: ", delta_value)

    if delta_value != 0:
        delta_no_data = True
    else:
        pass
    if delta_no_data:
        with open(delta_file_name, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([TimeFunction().get_unix_time_str(),delta_value])
            csvfile.close()
    else:
        pass
    return None


def theta_callback(theta_value):
    """this function will be called everytime NeuroPy has a new value for theta"""
    global theta_no_data
    global theta_file_name

    print("Value of theta is: ", theta_value)

    if theta_value != 0:
        theta_no_data = True
    else:
        pass
    if theta_no_data:
        with open(theta_file_name, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([TimeFunction().get_unix_time_str(),theta_value])
            csvfile.close()
    else:
        pass
    return None


def lowAlpha_callback(lowAlpha_value):
    """this function will be called everytime NeuroPy has a new value for lowAlpha"""
    global lowAlpha_no_data
    global lowAlpha_file_name

    print("Value of lowAlpha is: ", lowAlpha_value)

    if lowAlpha_value != 0:
        lowAlpha_no_data = True
    else:
        pass
    if lowAlpha_no_data:
        with open(lowAlpha_file_name, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([TimeFunction().get_unix_time_str(),lowAlpha_value])
            csvfile.close()
    else:
        pass
    return None


def highAlpha_callback(highAlpha_value):
    """this function will be called everytime NeuroPy has a new value for highAlpha"""
    global highAlpha_no_data
    global highAlpha_file_name

    print("Value of highAlpha is: ", highAlpha_value)

    if highAlpha_value != 0:
        highAlpha_no_data = True
    else:
        pass
    if highAlpha_no_data:
        with open(highAlpha_file_name, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([TimeFunction().get_unix_time_str(),highAlpha_value])
            csvfile.close()
    else:
        pass
    return None


def lowBeta_callback(lowBeta_value):
    """this function will be called everytime NeuroPy has a new value for lowBeta"""
    global lowBeta_no_data
    global lowBeta_file_name

    print("Value of lowBeta is: ", lowBeta_value)

    if lowBeta_value != 0:
        lowBeta_no_data = True
    else:
        pass
    if lowBeta_no_data:
        with open(lowBeta_file_name, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([TimeFunction().get_unix_time_str(),lowBeta_value])
            csvfile.close()
    else:
        pass
    return None


def highBeta_callback(highBeta_value):
    """this function will be called everytime NeuroPy has a new value for highBeta"""
    global highBeta_no_data
    global highBeta_file_name

    print("Value of highBeta is: ", highBeta_value)

    if highBeta_value != 0:
        highBeta_no_data = True
    else:
        pass
    if highBeta_no_data:
        with open(highBeta_file_name, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([TimeFunction().get_unix_time_str(),highBeta_value])
            csvfile.close()
    else:
        pass
    return None


def lowGamma_callback(lowGamma_value):
    """this function will be called everytime NeuroPy has a new value for lowGamma"""
    global lowGamma_no_data
    global lowGamma_file_name

    print("Value of lowGamma is: ", lowGamma_value)

    if lowGamma_value != 0:
        lowGamma_no_data = True
    else:
        pass
    if lowGamma_no_data:
        with open(lowGamma_file_name, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([TimeFunction().get_unix_time_str(),lowGamma_value])
            csvfile.close()
    else:
        pass
    return None


def midGamma_callback(midGamma_value):
    """this function will be called everytime NeuroPy has a new value for midGamma"""
    global midGamma_no_data
    global midGamma_file_name

    print("Value of midGamma is: ", midGamma_value)

    if midGamma_value != 0:
        midGamma_no_data = True
    else:
        pass
    if midGamma_no_data:
        with open(midGamma_file_name, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([TimeFunction().get_unix_time_str(),midGamma_value])
            csvfile.close()
    else:
        pass
    return None


if __name__ == '__main__':

    """列出 COM port"""
    ports = serial.tools.list_ports.comports()
    for port, desc, hwid in sorted(ports):
        print("{}: {} {}".format(port, desc, hwid))

    """取得當前 unix_time"""
    unix_time = TimeFunction().get_unix_time_str()

    """設定記錄檔名稱"""
    attention_file_name = 'data/attention{}.csv'.format(unix_time)
    meditation_file_name = 'data/meditation{}.csv'.format(unix_time)
    rawValue_file_name = 'data/rawValue{}.csv'.format(unix_time)
    delta_file_name = 'data/delta{}.csv'.format(unix_time)
    theta_file_name = 'data/theta{}.csv'.format(unix_time)
    lowAlpha_file_name = 'data/lowAlpha{}.csv'.format(unix_time)
    highAlpha_file_name = 'data/highAlpha{}.csv'.format(unix_time)
    lowBeta_file_name = 'data/lowBeta{}.csv'.format(unix_time)
    highBeta_file_name = 'data/highBeta{}.csv'.format(unix_time)
    lowGamma_file_name = 'data/lowGamma{}.csv'.format(unix_time)
    midGamma_file_name = 'data/midGamma{}.csv'.format(unix_time)
    blinkStrength_file_name = 'data/blinkStrength{}.csv'.format(unix_time)

    """設定腦波帽 COM port"""
    mind_wave_port = str(input("COM port? ex:COM3 =>"))

    """建立腦波帽 neuropy物件"""
    neuropy = NeuroPy(mind_wave_port)

    """初始化無資料 旗標"""
    attention_no_data = False
    meditation_no_data = False
    rawValue_no_data = False
    delta_no_data = False
    theta_no_data = False
    lowAlpha_no_data = False
    highAlpha_no_data = False
    lowBeta_no_data = False
    highBeta_no_data = False
    lowGamma_no_data = False
    midGamma_no_data = False

    """設定監聽函數"""
    neuropy.setCallBack("attention", attention_callback)
    neuropy.setCallBack("meditation", meditation_callback)
    neuropy.setCallBack("rawValue", rawValue_callback)
    neuropy.setCallBack("delta", delta_callback)
    neuropy.setCallBack("theta", theta_callback)
    neuropy.setCallBack("lowAlpha", lowAlpha_callback)
    neuropy.setCallBack("highAlpha", highAlpha_callback)
    neuropy.setCallBack("lowBeta", lowBeta_callback)
    neuropy.setCallBack("highBeta", highBeta_callback)
    neuropy.setCallBack("lowGamma", lowGamma_callback)
    neuropy.setCallBack("midGamma", midGamma_callback)

    """新增並創建紀錄用CSV 檔"""
    with open(attention_file_name, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["unix_time", "attention_value"])
        csvfile.close()

    with open(meditation_file_name, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["unix_time", "meditation_value"])
        csvfile.close()

    with open(rawValue_file_name, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["unix_time", "rawValue"])
        csvfile.close()

    with open(delta_file_name, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["unix_time", "delta_value"])
        csvfile.close()

    with open(theta_file_name, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["unix_time", "theta_value"])
        csvfile.close()

    with open(highAlpha_file_name, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["unix_time", "highAlpha_value"])
        csvfile.close()

    with open(lowAlpha_file_name, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["unix_time", "lowAlpha_value"])
        csvfile.close()

    with open(highBeta_file_name, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["unix_time", "highBeta_value"])
        csvfile.close()

    with open(lowBeta_file_name, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["unix_time", "lowBeta_value"])
        csvfile.close()

    with open(lowGamma_file_name, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["unix_time", "lowGamma_value"])
        csvfile.close()

    with open(midGamma_file_name, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["unix_time", "midGamma_value"])
        csvfile.close()

    """啟動腦波帽"""
    neuropy.start()
    print("press q to exit")

    try:
        while True:
            if keyboard.is_pressed('q'):
                break
            time.sleep(0.2)
    finally:
        neuropy.stop()
