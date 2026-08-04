
import pyautogui
import time

# 1. Configuration
MESSAGE = "All the best MOHOBBAT VAI.....BYIEEEE"  # Put your message here
COUNT = 10           # Number of times to send it
DELAY = 0.6           # Delay in seconds between messages (do NOT set to 0 or you'll get banned)

# 2. Countdown timer
print("You have 5 seconds to open WhatsApp Web and click on your friend's chat box...")
for i in range(5, 0, -1):
    print(f"Starting in {i}...")
    time.sleep(1)

print("Firing away!")

# 3. The loop
for _ in range(COUNT):
    pyautogui.typewrite(MESSAGE)
    pyautogui.press("enter")
    time.sleep(DELAY)

print("Done! Mission accomplished.")
changed?

