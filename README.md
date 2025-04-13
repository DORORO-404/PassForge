# 🔐 PassForge - Secure Password Generator for Terminal

![Project Status](https://img.shields.io/badge/status-active-brightgreen)  
![License](https://img.shields.io/badge/license-MIT-blue)  
![Python Version](https://img.shields.io/badge/python-3.8+-blue)

**PassForge** is a simple, secure, and customizable password generator for your terminal.  
Built with Python, it's perfect for developers, cybersecurity professionals, and Kali Linux users.

---

## 🚀 About The Project

**PassForge** generates strong and secure passwords directly from the terminal using Python’s `random.SystemRandom()` for cryptographic-level randomness.  

It allows users to:

- ✅ Choose the length (8 to 64+ characters)
- ✅ Choose character types (letters, digits, symbols)
- ✅ Save passwords to a text file
- ✅ Generate multiple passwords at once
- ✅ Optional clipboard copy support *(coming soon)*

---

## 🛠 Technologies Used

| Language   | Type     | Dependencies     |
|------------|----------|------------------|
| Python 3.8+| CLI Tool | `pyfiglet` (for ASCII art)

**Python Modules**:
- `random` – for secure random generation
- `string` – character sets
- `pyfiglet` – for terminal banner art
- `datetime`, `sys`

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
Enter the desired password length: 8
How many passwords would you like to generate?: 5


[1] Numbers only         [4] Uppercase letters
[2] Symbols only         [5] Lowercase letters
[3] Mixed characters     [6] Mixed letters
Select an option: 3

[+] Generating 5 password(s) | Length: 8 | Mode: MIXED
Generated Passwords:
1. Va]MLgT4
2. nAII#x8Y
3. 3lL~b:Y:
4. P2Sc8o&l
5. 2W=LI^vc

Do you want to save the passwords to a file? [Y/n]:
```

## 🤝 Contributing

Contributions are always welcome! Here’s how you can contribute:

1. Fork the repository.
2. Create your branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

Feel free to open issues for any bugs or feature requests.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## 📁 Project Structure
PassForge/
├── passforge.py           # Main Python script for the wordlist generator
├── README.md              # Project documentation
├── LICENSE                # MIT License file
└── requirements.txt       # List of required Python packages