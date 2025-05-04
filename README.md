# 🔐 PassForge - Secure Password Generator for Terminal

![Project Status](https://img.shields.io/badge/status-active-brightgreen)  
![License](https://img.shields.io/badge/license-MIT-blue)  
![Python Version](https://img.shields.io/badge/python-3.8+-blue)

**PassForge** is a simple, secure, and customizable password generator for your terminal.  
Built with Python, it's perfect for developers, cybersecurity professionals, and Kali Linux users.

---

## 🚀 About The Project

**PassForge** generates strong and secure passwords directly from the terminal using Python's `random` module, ensuring cryptographic-level randomness.

It allows users to:

- ✅ Choose the length (From 8 to infinity)
- ✅ Choose character types (letters, digits, symbols)
- ✅ Save passwords to a text file
- ✅ Generate multiple passwords at once

---

## 🛠 Technologies Used

| Language   | Type     | Dependencies     |
|------------|----------|------------------|
| Python 3.8+| CLI Tool | `pyfiglet` (for ASCII art)

**Python Modules**:
- `random` – for secure random generation
- `string` – character sets
- `pyfiglet` – for terminal banner art
- `datetime`, `sys`, `colorama`

---

## 📦 Installation

```bash
git clone https://github.com/DORORO-404/PassForge.git
cd PassForge
pip install -r requirements.txt
python passforge.py
```

## 🖥️ Example Usage

```bash
[+] Welcome to PassForge — Create. Secure. Generate.
[i] Advanced password generator for strong and secure credentials.
[i] Let's forge a password that's hard to crack!
[i] Type 'exit', 'quit', 'close', or CTRL + C to exit.
---------------------------------------------------------------------------

[+] What would you like to do?
[1] 🧩 Generate Passwords
[2] 🚪 Exit PassForge
[>] Enter your choice: 1

[>] Enter desired password length (min 8): 10
[>] How many passwords to generate?: 3

[+] Available Password Modes:
[1] 🔢 Numbers only
[2] 🔣 Symbols only
[3] 🧪 Mixed characters
[4] 🔠 Uppercase only
[5] 🔡 Lowercase only
[6] 🔤 Letters (uppercase + lowercase)
[>] Select a mode: 3

[+] Generating 3 password(s) | Length: 10 | Mode: MIXED
[✔] Passwords Generated Successfully:

1. U7ba{Kx6-K
2. 4$':oyzkP9
3. *L!6DKcVRY

[+] What would you like to do next?
[1] 💾 Save to file
[2] 🔁 Generate more
[3] 🚪 Exit PassForge
[>] Select an option: 1

[>] Enter a name for the file: passwords
[✔] Passwords saved to passwords.txt

[+] What would you like to do next?
[1] 💾 Save to file
[2] 🔁 Generate more
[3] 🚪 Exit PassForge
[>] Select an option: 3

[i] Exit command received.

[*] Exiting PassForge...
[!] Thank you for trusting PassForge!
[i] Session ended successfully.
```

## 🤝 Contributing

Contributions are always welcome! Here’s how you can contribute:

1. Fork the repository.
2. Create your branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

Feel free to open issues for any bugs or feature requests.

## ⚖️ License

Distributed under the MIT License. See `LICENSE` for more information.

## 📁 Project Structure
```bash
PassForge/
├── passforge.py           # Main Python script for the wordlist generator
├── README.md              # Project documentation
├── LICENSE                # MIT License file
└── requirements.txt       # List of required Python packages
```