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
[+] ===== Welcome to PassForge Password Generator ===== [+]
Enter the password length (minimum 8): 10
How many passwords to generate?: 5

[+] Available Password Modes:
[1] Numbers only
[2] Symbols only
[3] Mixed characters
[4] Uppercase only
[5] Lowercase only
[6] Letters (uppercase + lowercase)
Select a mode: 3

[+] Generating 5 passwords | Length: 10 | Mode: MIXED
[✔] Passwords Generated Successfully:

1. O|5tb;eFU#
2. tE4km.nPe9
3. 1QgQtj@q9!
4. s5#o7@eRkH
5. QX4dDSkrO(

[+] What would you like to do next?
[1] Save the passwords to a file
[2] Generate more passwords
[3] Exit PassForge
Select an option: 1
Enter a name for the file: DORORO__404
[✔] Passwords saved to DORORO__404.txt
Select an option: 3

Exiting PassForge... Thank you for using our tool!
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