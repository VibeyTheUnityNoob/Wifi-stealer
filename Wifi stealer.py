import os
import subprocess

output = subprocess.check_output(["netsh", "wlan", "show", "profiles"])

profiles = [line.split(":")[1].strip() for line in output.decode().split("\n") if "All User Profile" in line]

file_path = os.path.join(os.path.dirname(__file__), "wifi_passwords.txt")

with open(file_path, "w") as f:
    for profile in profiles:
        output = subprocess.check_output(["netsh", "wlan", "show", "profile", profile, "key=clear"])
        f.write(output.decode())
        f.write("\n")
