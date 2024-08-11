# Basic Keylogger

This is a basic keylogger written in Python using the `pynput` library. It captures and logs keystrokes, saving them to a file with a unique encoding method for added obfuscation.

## Features

- **Keystroke Logging**: Captures all keystrokes made on the keyboard.
- **Base64 Encoding**: Logs are encoded in base64 to obscure the raw keystroke data.
- **File Storage**: Saves the encoded keystrokes to a file.

## Installation

### Prerequisites

- Python 3.x
- `pynput` library

### Install Dependencies

Install the `pynput` library using pip:

```bash
pip install pynput
```

## Usage

1. **Clone the Repository**

    ```bash
    git clone https://github.com/your-username/SCT_CS_02.git
    cd SCT_CS_02
    ```

2. **Run the Keylogger Script**

    ```bash
    python keylogger.py
    ```

    The script will start logging keystrokes. Press the `Esc` key to stop logging and save the recorded keystrokes to `keystrokes.log`.

3. **Check the Log File**

    The keystrokes are saved in `keystrokes.log` in base64 encoded format. You can decode the file to view the raw keystroke data.

## Key Features

- **Base64 Encoding**: Provides a unique way to save keystrokes, making the data less immediately readable.
- **Stop Logging**: The logging process can be stopped by pressing the `Esc` key.

## Ethical Use

This tool is intended for educational purposes and should be used responsibly. Ensure you have permission before using this keylogger in any environment. Unauthorized use may be illegal and unethical.

## Contributing

If you have suggestions or improvements for this project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or feedback, please contact [Karthik S Sathyan](karthikssathyan1@gmail.com).

