# 🚀 Telegram Auto-Reactor

Automatically send emoji reactions to the latest messages in specified Telegram channels using `telethon`.

## 📋 Requirements

- Python 3.6 or higher.
- A Telegram account/s.

## 🛠 Installation

Before getting started, make sure you've got the required libraries installed. Use `pip` to do so:

```bash
pip install requirements.txt
```

## 🎨 Configuration

Create a config.yaml in the same directory as the main script.
Fill it as follows:
```yaml
api_id: YOUR_API_ID
api_hash: YOUR_API_HASH
accounts:
  - phone: +1234567890
    session: account1_session.session
  ...
channels:
  - '@channelusername1'
  - '@channelusername2'
  ...
```

## 🚀 Usage

Simply run the main script:

```bash
python multiAccountReactioons2.py
```

On first run, telethon will prompt you to enter a code sent to the provided phone number for authentication.

Built with ❤️ and Python.
