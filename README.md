# PassForge - Secure Password Generator for Terminal

![Project Status](https://img.shields.io/badge/status-active-brightgreen)  
![License](https://img.shields.io/badge/license-MIT-blue)  
![Python Version](https://img.shields.io/badge/python-3.8+-blue)

**PassForge** is a simple, terminal-based password generator written in Python. It focuses on security and usability, making it a great companion for developers, cybersecurity professionals, and Kali Linux users.

## 🚀 About The Project

PassForge is an open-source password generator that provides strong and secure passwords via a clean terminal interface. It uses Python's built-in `random.SystemRandom()` for cryptographically secure randomness, and allows customization of password length and character set.

The tool can:

- Generate random passwords securely using OS entropy
- Offer length customization from 8 to 64 characters
- Include or exclude specific character types (letters, digits, punctuation)
- Copy generated passwords to clipboard (optional)

## 🛠 Technologies Used

| Language   | Type     | Requirements     |
|------------|----------|------------------|
| Python 3.8+| CLI Tool | No external libraries (optional clipboard module) |

**Python Modules**:
- `random.SystemRandom()`: Uses OS-level entropy source for secure generation
- `string`: Built-in character sets like letters, digits, and symbols

## ✨ Features

- ✅ Cryptographically secure password generation
- ✅ Customizable password length (8–64 characters)
- ✅ Choose character types: letters, numbers, punctuation
- ✅ Optional clipboard copy functionality
- ✅ Fast and easy-to-use terminal interface
- ✅ Works offline, no external API needed
