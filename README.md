# Password Manager

A simple Python application using Tkinter to manage passwords securely. It allows you to generate strong passwords, save them along with website details, and search for saved passwords.

## Features

- Generate strong passwords with random letters, numbers, and symbols.
- Save passwords securely in a JSON file (`passwords.json`).
- Search for saved passwords by website name.
- Basic error handling for empty fields and missing JSON file.

## Requirements

- Python 3.x
- Tkinter (typically included with Python installations)
- pyperclip library (`pip install pyperclip`)

## Installation and Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/Cpoooo/password-manager.git
   cd password-manager
   ```

2. Ensure you have the required dependencies installed:
   ```bash
   pip install pyperclip
   ```

3. Run the application:
   ```bash
   python password_manager.py
   ```

4. Use the interface to add, generate, and manage passwords.

## Usage

- **Generate Password**: Click "Generate Password" to create a new strong password and copy it to your clipboard.
- **Save Password**: Enter website details (Website, Email/Username, Password) and click "Add" to save them securely.
- **Search Password**: Enter a website name in the "Website" field and click "Search" to retrieve saved credentials.
