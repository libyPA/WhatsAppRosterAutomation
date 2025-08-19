import pandas as pd
import pywhatkit as kit
import time

# Load roster from Excel
df = pd.read_excel("Roster.xlsx")

# Days of the week
days = ["Monday", "Tuesday", "Wednesday"]

for i, row in df.iterrows():
    name = row["Name"]
    phone = str(row["Phone"]).strip()

    # Auto-add country code if missing
    if not phone.startswith("+"):
    	phone = "+353" + phone.lstrip("0")   # removes leading 0 and adds +353

    print(f"phonenumber is {phone}")

    # Build weekly schedule
    schedule = "\n".join([f"{day}: {row[day]}" for day in days])

    # Message text
    message = f"Hello {name}, here is your weekly roster:\n\n{schedule}"

    # Send WhatsApp message (set 2 minutes ahead of current time)
    now = time.localtime()
    hour = now.tm_hour
    minute = now.tm_min + 2

    print(f"Sending message to {name} ({phone})...")
    kit.sendwhatmsg_instantly(phone, message, wait_time=20, tab_close=True)
    #kit.sendwhatmsg(phone, message, hour, minute, wait_time=20, tab_close=True)
    time.sleep(15)  # pause to avoid overlap
