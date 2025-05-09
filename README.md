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
- `datetime`, `sys`

---

## 📦 Installation
To install **PassForge** version 1.5.1, follow the steps below:

1. Clone the repository:

    ```bash
    git clone https://github.com/DORORO-404/PassForge.git
    cd PassForge
    ```

2. **Set Up a Virtual Environment (Recommended)**

    For **Linux** / **macOS**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

    For **Windows**:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:

    ```bash
    python3 passforge.py
    ```

5. Exit anytime by typing `exit`, `quit`, `close`, or pressing `CTRL + C`.

## 🖥️ Example Usage

```bash
[+] Welcome to PassForge — Create. Secure. Generate.
[INFO] An advanced password generator for strong and secure credentials.
[INFO] Type 'exit', 'quit', 'close', or press CTRL + C to exit.
---------------------------------------------------------------------------

[+] What would you like to do?
[1] Generate Passwords
[2] Exit PassForge
[INPUT] Enter your choice: 1

[INPUT] Enter desired password length: 10
[INPUT] Enter number of passwords to generate: 10

[+] Available Password Modes:
[1] Numbers only
[2] Symbols only
[3] Mixed characters
[4] Uppercase letters only
[5] Lowercase letters only
[6] Letters (uppercase + lowercase)
[INPUT] Select a mode: 3

[+] Generating 10 passwords | Length: 10 | Mode: MIXED
[SUCCESS] Passwords generated successfully:

1. (IPp(762)|
2. t{pw3%dIu0
3. %217xBtm_a
4. (_p3XKlX06
5. G[,^3r9m,p
6. RqU(c!n6jY
7. FfsG:6UYJ6
8. :jFxaDO8j]
9. mEP7^7Q2in
10. qE-zLP/7R_

[+] What would you like to do next?
[1] Save to file
[2] Generate more passwords
[3] Exit PassForge
[INPUT] Select an option: 1

[INPUT] Enter file name to save: passwords
[SUCCESS] Passwords saved to passwords.txt

[+] What would you like to do next?
[1] Save to file
[2] Generate more passwords
[3] Exit PassForge
[INPUT] Select an option: 3

[INFO] Exiting PassForge...
[THANK YOU] Thank you for using PassForge!
[INFO] Session ended successfully.
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