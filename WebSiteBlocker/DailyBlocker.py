import time
from datetime import datetime as dt

#hosts file location
#Mac and Linux /etc/hosts
#Windows C:\Windows\System32\drivers\etc\hosts
hostsTemp = "hosts"
hostPath = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
websiteList = ["www.facebook.com", "facebook.com", "post.sk"]
workingHoursStart = 16
workingHoursEnd = 17

while True:
    #dt(Year, month, day, 8 hours) < actual time < dt(Year, month, day, 16 hours)
    if dt(dt.now().year, dt.now().month, dt.now().day, workingHoursStart) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, workingHoursEnd):
        print("Working hours")
        with open(hostsTemp, 'r+') as f:
            content = f.read()
            for website in websiteList:
                if website in content:
                    pass
                else:
                    f.write(redirect + " " + website + "\n")            
    else:
        print("Not Working hours")
        with open(hostsTemp, 'r+') as f:
            content = f.readlines()
            f.seek(0)
            for line in content:
                if not any(website in line for website in websiteList):
                    f.write(line)
            f.truncate()
    time.sleep(5)