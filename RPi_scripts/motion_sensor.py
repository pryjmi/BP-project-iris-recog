import RPi.GPIO as GPIO
import time
import subprocess as sp

# Výběr pinu na RPi
SENSOR_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)

def send_signal(channel):
    # Výpis do konzole při detekci pohybu + pořízení snímku
    print('signal')
    sp.run(['libcamera-jpeg', '-o', 'home/pi/Desktop/pic.jpg'])
try:
    # Zaznamenání pohybu přes PIR čidlo
    GPIO.add_event_detect(SENSOR_PIN, GPIO.RISING, callback=send_signal)
    time.sleep(10)
    # Přerušení procesu
except KeyboardInterrupt:
    # Výpis do konzole při ukončení procesu
    print('finish')
GPIO.cleanup()