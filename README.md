# Instagram Group Bot 🤖

Welcome to the Instagram Group Bot! This bot is designed for secure and dynamic group-based messaging with task management features.

## 🌟 Features
- **End-to-End Encrypted Messaging** 🔒 using the latest encryption standards.
- **Dynamic Messages**: Messages update automatically to avoid repetition.
- **Group Permissions**: Messages are only sent to allowed groups.
- **Task Assignment**: Assign tasks to specific users within a group.
- **Admin Contact**: Easily contact the admin - [@xploit.ninja](https://instagram.com/xploit.ninja).
- **Auto-generated Encryption Key**: If no encryption key is provided via environment variables, the bot will automatically generate one and store it securely.

## 🚀 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/zynthera/Hacker_instagrambot.git
   cd Hacker_instagrambot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables in a `.env` file:
   ```env
   INSTAGRAM_USERNAME=your_instagram_username
   INSTAGRAM_PASSWORD=your_instagram_password
   # Optional: provide your encryption key, otherwise one will be auto-generated.
   ENCRYPTION_KEY=your_generated_encryption_key
   ALLOWED_GROUPS=group_id_1,group_id_2
   ADMIN_CONTACT=@xploit.ninja
   MESSAGE_UPDATE_INTERVAL=3600
   ```

4. Run the bot:
   ```bash
   python main.py
   ```

## 🛠️ Configuration
- Updating the `.env` file allows you to configure group IDs, API credentials, and other settings.
- The encryption key will be auto-generated and saved to `encryption.key` if not provided.

## 🧪 Testing
- Add unit tests for each feature to ensure reliability.
- Run tests using `unittest`:
  ```bash
  python -m unittest discover
  ```

## 📜 License
This project is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2025 zynthera

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
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

Let me know if you need help with anything else!