# 🎉 Hacker_InstaGroupBot 🤖

<p align="center">
  <img src="https://github.com/zynthera/zynthera/raw/master/public/hh.png" alt="Bot Logo" width="200">
</p>

<p align="center">
  <strong>Admin:</strong> <a href="https://instagram.com/xploit.ninja">@xploit.ninja</a>
</p>

---

## 🌟 Features
- **🔒 End-to-End Encrypted Messaging**: Messages are secured using the latest encryption standards.
- **🔄 Dynamic Messages**: Automatically updates messages to keep content fresh.
- **👥 Group Permissions**: Messages are sent only to authorized groups.
- **✅ Task Assignment**: Assign and manage tasks for specific users within groups.
- **🔑 Auto-Generated Encryption Key**: Automatically generates a secure encryption key if not provided.
- **📞 Admin Contact**: Direct admin support for any inquiries or issues.
- **📊 Streamlit Dashboard**: Monitor bot activity and logs in real-time via a web dashboard.

---

## 🚀 Quick Start Guide

### 1️⃣ Clone the Repository
Clone the repository to your local machine:
```bash
git clone https://github.com/zynthera/Hacker_instagrambot.git
cd Hacker_instagrambot
```

### 2️⃣ Install Dependencies
Install the required Python dependencies using `requirements.txt`:
```bash
pip install -r requirements.txt
```

For **non-root users**, create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

For **root users**, ensure proper permissions to avoid conflicts:
```bash
sudo pip install -r requirements.txt
```

### 3️⃣ Set Up Environment Variables
Create a `.env` file in the project directory and populate it with the following variables:
```env
INSTAGRAM_USERNAME=your_instagram_username
INSTAGRAM_PASSWORD=your_instagram_password
GEMINI_API_KEY=your_gemini_ai_api_key
# Optional: Provide your encryption key, or the bot will generate one automatically.
ENCRYPTION_KEY=your_generated_encryption_key
ALLOWED_GROUPS=group_id_1,group_id_2
ADMIN_CONTACT=@xploit.ninja
MESSAGE_UPDATE_INTERVAL=3600
```

### 4️⃣ Generate an Encryption Key (Optional)
If you don’t want the bot to auto-generate an encryption key, you can generate one manually:

#### **Using Python Script**
1. Create the following script in a file named `generate_encryption_key.py`:
    ```python
    from cryptography.fernet import Fernet

    def generate_key(file_name="encryption.key"):
        """
        Generate a secure encryption key and save it to a file.
        """
        key = Fernet.generate_key()
        with open(file_name, "wb") as key_file:
            key_file.write(key)
        print(f"Encryption key successfully generated and saved to '{file_name}'.")

    if __name__ == "__main__":
        generate_key()
    ```
2. Run the script:
    ```bash
    python generate_encryption_key.py
    ```
3. A file named `encryption.key` will be created in your directory. Open the file, copy the key, and paste it into your `.env` file under `ENCRYPTION_KEY`.

### 5️⃣ Run the Bot
Start the bot with:
```bash
python main.py
```

For **non-root users**:
```bash
source venv/bin/activate
python main.py
```

---

## ⚙️ Configuration Options
The bot can be customized using the `.env` file:
- **`INSTAGRAM_USERNAME`**: Your Instagram username.
- **`INSTAGRAM_PASSWORD`**: Your Instagram password.
- **`GEMINI_API_KEY`**: API key for Gemini AI integration.
- **`ENCRYPTION_KEY`**: A secure encryption key (generated automatically if not provided).
- **`ALLOWED_GROUPS`**: Comma-separated list of group IDs authorized to receive messages.
- **`ADMIN_CONTACT`**: Contact information for the bot admin (e.g., Instagram handle).
- **`MESSAGE_UPDATE_INTERVAL`**: Time interval (in seconds) for updating messages.

---

## 🧪 Testing
Run the unit tests to ensure everything is working as expected:
```bash
pytest test_bot.py
```

---

## 📊 Monitoring Dashboard
Launch the Streamlit monitoring dashboard with:
```bash
streamlit run dashboard.py
```
Access it in your browser at `http://localhost:8501`.

---

## 📖 FAQ

### **1. What happens if I don’t provide an encryption key?**
The bot will automatically generate a secure encryption key and save it in a file named `encryption.key`.

### **2. How do I find group IDs for `ALLOWED_GROUPS`?**
You can refer to Instagram's API documentation or use third-party tools to fetch group IDs.

### **3. Can this bot run on Termux?**
Yes! Follow these steps to install the required dependencies on Termux:
```bash
pkg update
pkg upgrade
pkg install python rust cargo
```

```bash
pkg install clang python-dev libffi libffi-dev openssl openssl-dev
pip install cryptography
```

### **4. How to resolve `Permission Denied` errors as root users?**
Ensure you use `sudo` for all commands or switch to a non-root user to avoid file permission conflicts.

---

## 💡 Best Practices
- **Secure Your `.env` File**: Avoid sharing your `.env` file or storing it in public repositories.
- **Use Strong Passwords**: Set a strong password for your Instagram account.
- **Keep Dependencies Updated**: Regularly update your dependencies with:
    ```bash
    pip install --upgrade -r requirements.txt
    ```
- **Monitor Logs**: Use the Streamlit dashboard to monitor bot activity in real-time.

---

## 🛠 Contribution Guidelines
We welcome contributions from the community! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
    ```bash
    git checkout -b feature-name
    ```
3. Commit your changes:
    ```bash
    git commit -m "Add feature-name"
    ```
4. Push to your branch:
    ```bash
    git push origin feature-name
    ```
5. Create a pull request on GitHub.

For major changes, please open an issue first to discuss your approach.

---

## 📜 License
This project is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2025 zynthera

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 📞 Contact
For any questions, feel free to reach out to the admin: [@xploit.ninja](https://instagram.com/xploit.ninja).

---

<div align="center">
  <img src="https://img.shields.io/github/watchers/zynthera/Hacker_instagrambot?color=blue&style=for-the-badge" alt="Watchers Badge">
  <p><strong>Number of Views:</strong> <span style="color: green; font-size: 20px;">❤ {{ NUMBER_OF_VIEWS }} Views</span></p>
</div>