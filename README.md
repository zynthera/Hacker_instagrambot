# Instagram Group Bot 🤖

Welcome to the Instagram Group Bot! This bot is designed for secure and dynamic group-based messaging with task management features.

## 🌟 Features
- **End-to-End Encrypted Messaging** 🔒
- **Dynamic Messages**: Messages update automatically to avoid repetition.
- **Group Permissions**: Messages are only sent to allowed groups.
- **Task Assignment**: Assign tasks to specific users within a group.
- **Admin Contact**: Easily contact the admin - [@xploit.ninja](https://instagram.com/xploit.ninja).

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
Update `config.py` or `.env` to add your group IDs and other settings.

## 📜 License
This project is licensed under the MIT License.