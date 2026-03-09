import tkinter as tk
from tkinter import messagebox
import random
import time
import threading
import requests

# ThingSpeak API details (replace with your own channel & API keys)
THINGSPEAK_WRITE_API = "YOUR_WRITE_API_KEY"
THINGSPEAK_READ_API = "YOUR_READ_API_KEY"
CHANNEL_ID = "YOUR_CHANNEL_ID"
THINGSPEAK_WRITE_URL = "https://api.thingspeak.com/update"
THINGSPEAK_READ_URL = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json"

# Thresholds
TEMP_HIGH = 30   # Fan turns on above this
TEMP_LOW = 18    # Heater turns on below this

class HomeAutomationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Home Automation System")

        # System states
        self.temperature = 25
        self.smoke_detected = False
        self.fan_on = False
        self.heater_on = False
        self.alarm_on = False

        # UI Labels
        self.temp_label = tk.Label(root, text=f"Temperature: {self.temperature} °C", font=("Arial", 14))
        self.temp_label.pack(pady=10)

        self.fan_label = tk.Label(root, text="Fan: OFF", font=("Arial", 14))
        self.fan_label.pack(pady=5)

        self.heater_label = tk.Label(root, text="Heater: OFF", font=("Arial", 14))
        self.heater_label.pack(pady=5)

        self.smoke_label = tk.Label(root, text="Smoke Detector: CLEAR", font=("Arial", 14))
        self.smoke_label.pack(pady=5)

        self.alarm_label = tk.Label(root, text="Alarm: OFF", font=("Arial", 14))
        self.alarm_label.pack(pady=5)

        self.cloud_label = tk.Label(root, text="Cloud Data: Waiting...", font=("Arial", 12), fg="blue")
        self.cloud_label.pack(pady=10)

        # Buttons
        tk.Button(root, text="Simulate Smoke", command=self.trigger_smoke).pack(pady=10)
        tk.Button(root, text="Reset Alarm", command=self.reset_alarm).pack(pady=10)
        tk.Button(root, text="Fetch Cloud Data", command=self.fetch_from_thingspeak).pack(pady=10)

        # Start background monitoring
        self.running = True
        threading.Thread(target=self.monitor_system, daemon=True).start()

    def monitor_system(self):
        while self.running:
            # Simulate temperature changes
            self.temperature = random.randint(15, 35)
            self.update_system()
            self.send_to_thingspeak()
            time.sleep(5)

    def update_system(self):
        self.temp_label.config(text=f"Temperature: {self.temperature} °C")

        # Fan control
        if self.temperature > TEMP_HIGH:
            self.fan_on = True
            self.fan_label.config(text="Fan: ON")
        else:
            self.fan_on = False
            self.fan_label.config(text="Fan: OFF")

        # Heater control
        if self.temperature < TEMP_LOW:
            self.heater_on = True
            self.heater_label.config(text="Heater: ON")
        else:
            self.heater_on = False
            self.heater_label.config(text="Heater: OFF")

        # Smoke detector
        if self.smoke_detected:
            self.smoke_label.config(text="Smoke Detector: SMOKE!")
            self.activate_alarm()
        else:
            self.smoke_label.config(text="Smoke Detector: CLEAR")

    def trigger_smoke(self):
        self.smoke_detected = True
        self.update_system()

    def activate_alarm(self):
        self.alarm_on = True
        self.alarm_label.config(text="Alarm: ON")
        messagebox.showwarning("ALERT", "Smoke detected! Alarm triggered!")
        print("📱 Phone Notification: Smoke detected at home!")

    def reset_alarm(self):
        self.smoke_detected = False
        self.alarm_on = False
        self.alarm_label.config(text="Alarm: OFF")
        self.update_system()

    def send_to_thingspeak(self):
        try:
            payload = {
                "api_key": THINGSPEAK_WRITE_API,
                "field1": self.temperature,
                "field2": int(self.fan_on),
                "field3": int(self.heater_on),
                "field4": int(self.smoke_detected),
                "field5": int(self.alarm_on)
            }
            requests.post(THINGSPEAK_WRITE_URL, data=payload)
        except Exception as e:
            print("Error sending to ThingSpeak:", e)

    def fetch_from_thingspeak(self):
        try:
            params = {"api_key": THINGSPEAK_READ_API, "results": 1}
            response = requests.get(THINGSPEAK_READ_URL, params=params)
            data = response.json()
            if "feeds" in data and len(data["feeds"]) > 0:
                latest = data["feeds"][0]
                cloud_temp = latest.get("field1", "N/A")
                cloud_fan = "ON" if latest.get("field2") == "1" else "OFF"
                cloud_heater = "ON" if latest.get("field3") == "1" else "OFF"
                cloud_smoke = "SMOKE!" if latest.get("field4") == "1" else "CLEAR"
                cloud_alarm = "ON" if latest.get("field5") == "1" else "OFF"

                self.cloud_label.config(
                    text=f"Cloud Data → Temp: {cloud_temp}°C | Fan: {cloud_fan} | Heater: {cloud_heater} | Smoke: {cloud_smoke} | Alarm: {cloud_alarm}"
                )
        except Exception as e:
            self.cloud_label.config(text=f"Error fetching cloud data: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = HomeAutomationApp(root)
    root.mainloop()