import psutil
import os
import fontawesome as fa
import datetime
import time
import pulsectl
#import threading

spacer = '\ \ \|\ \ '
pulse = pulsectl.Pulse()

"""
class VolumeMonitor:
    def __init__(self):
        self.refresh()
    def refresh(self):
        self.volume = int(100*pulse.sink_list()[0].volume.values[0])
        self.do_refresh = True
    def allow_refresh(self):
        self.do_refresh = True
    def start_listen(self):
        while True:
            if self.do_refresh:
                self.refresh()

vm = VolumeMonitor()
"""
print('Starting status bar...')

def refresh(put_col):
    battery = psutil.sensors_battery()
    if(battery.percent >= 85):
        bat_sym = fa.icons['battery-full']
    elif(battery.percent >= 60):
        bat_sym = fa.icons['battery-three-quarters']
    elif(battery.percent >= 35):
        bat_sym = fa.icons['battery-half']
    elif(battery.percent >= 15):
        bat_sym = fa.icons['battery-quarter']
    else:
        bat_sym = fa.icons['battery-empty']
    vol_sym = fa.icons['headphones']
    os.system('xsetroot -name ' + vol_sym + '\ '  + str(int(100*pulse.sink_list()[0].volume.values[0])) + '\%'  + spacer + bat_sym + '\ '  + str(int(battery.percent)) + '\%'  + spacer + datetime.datetime.now().strftime('%I\\' + (':' if put_col else ' ')  + '%M\ %a\ %b\ %d'))

def start_refresh_loop():
    put_col = True
    while True:
        refresh(put_col)
        put_col = not put_col
        time.sleep(0.5)


start_refresh_loop()

"""
vol_loop = threading.Thread(target=vm.start_listen)
vol_loop.start()

refresh_loop = threading.Thread(target=start_refresh_loop)
refresh_loop.start()

def refresh_volume(ev):
    #vm.allow_refresh()
    refresh(True)
pulse.event_mask_set('all')
pulse.event_callback_set(refresh_volume)
pulse.event_listen()
"""
