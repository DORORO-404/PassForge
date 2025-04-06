# PassForge - Secure Password Generator for Terminal

![Project Status](https://img.shields.io/badge/status-active-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python Version](https://img.shields.io/badge/python-3.8+-blue)

PassForge is a command-line password generator tool built with Python's `random` and `string` modules, designed for cybersecurity professionals and Kali Linux users.

## 🚀 Overview

PassForge is an open-source project that:
- Generates cryptographically strong random passwords
- Uses Python's built-in `random` and `string` modules for security
- Provides a simple terminal interface for password generation

## 🛠 Core Implementation

| Module | Purpose | Security Note |
|--------|---------|---------------|
| `random.SystemRandom()` | Cryptographically secure random number generation | Uses OS-provided entropy |
| `string` | Provides character sets (ascii_letters, digits, punctuation) | Predefined safe character sets |

## ✨ Key Features

- 🔒 Secure password generation using `random.SystemRandom()`
- ⚡ Customizable length (8-64 characters)
- 📋 Clipboard copying functionality
- 🎨 Character set options using `string` module:
  - `string.ascii_letters` (uppercase + lowercase)
  - `string.digits` (0-9)
  - `string.punctuation` (special characters)
- 🌐 Simple terminal interface
