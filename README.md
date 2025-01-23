# README

## **Description**
This Python script allows you to spam a message repeatedly on WhatsApp Web to a specific contact. This project is designed **only for entertainment purposes** (such as a harmless prank between friends).

### ⚠️ **Important Warnings**
1. **Responsible Use:** This script is for humorous purposes only. You are solely responsible for your actions when using this program.
2. **Risk of Ban:** Abusing this script could violate WhatsApp's terms of service and result in your account being banned. Be cautious.
3. **Headless Mode:** You must disable headless mode during the first use to log in and scan the QR code. After that, your session data will be saved.

---

## **Features**
- Automatically send repeated messages to a specified contact.
- Option to enable or disable "headless" mode (whether or not the browser window is displayed).
- Automatically detect contacts on WhatsApp Web.
- Random pauses between messages to simulate human behavior.
- Periodic reports showing the number of messages sent and elapsed time.

---

## **Requirements**
1. **Python 3.x** installed on your system.
2. The following libraries installed:
   ```bash
   pip install selenium
   ```
3. **Google Chrome** and the corresponding ChromeDriver installed and added to PATH. Ensure the Chrome version matches the driver version.
4. An active WhatsApp account.

---

## **Setup**
1. Download the Python script to your machine.
2. Install the required libraries with:
   ```bash
   pip install selenium
   ```
3. Use the following option to save user sessions:
   - **User Data Directory Path:** `--user-data-dir=C:\Temp\chrome-data` (modifiable in the script).

---

## **How to Use**
1. **Initial Run (without headless mode):**
   - Run the script:
     ```bash
     python script.py
     ```
   - When prompted to enable headless mode, choose "no."
   - Log in to WhatsApp Web by scanning the QR code.
   - Once logged in, press **Enter** to continue.
2. **Configure the Spam:**
   - Enter the contact name.
   - Enter the message you want to send repeatedly.
3. **Start Spamming:**
   - The script will begin sending messages in a loop.
   - A random pause will occur between each message.
   - Periodic updates will be displayed in the console, showing the number of messages sent and the elapsed time.

---

## **Customization**
- **Adjust Message Frequency:** Modify the following line to adjust pauses:
  ```python
  time.sleep(random.uniform(0.1, 0.8))
  ```
- **Change User Data Directory Location:**
  ```python
  options.add_argument("--user-data-dir=C:\\Temp\\chrome-data")
  ```

---

## **Important Notes**
- You must disable headless mode during the first use to save your session data.
- If the script fails to find a contact, check the exact name entered (case-sensitive).

---

## **Legal Disclaimer**
This script is provided "as is" without any warranty. The author is not responsible for any misuse or consequences of using this program, including account bans or violations of WhatsApp's rules.

---

License

Just don't steal my code please...


# vocabulle-autoclick
