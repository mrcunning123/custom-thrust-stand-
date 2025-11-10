from hx711 import HX711
import time

# HX711 wiring:
# DT -> GP2
# SCK -> GP3
hx = HX711(dout=2, pd_sck=3)

print("Remove all weight. Taring...")
time.sleep(2)
hx.tare()
print("Tare complete.")

# You will adjust this value during calibration
hx.scale = 2000   # <-- change this after testing

while True:
    weight = hx.get_units()
    print("Weight:", weight, "kg")
    time.sleep(0.5)
