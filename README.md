# Executor SendEmail

The Executor SendEmail is a command-line utility for sending emails from the terminal. It provides a simple interface for configuring email sending parameters.

## Requirements

To use the Executor SendEmail, you need:

- A Unix-like operating system (Linux, macOS, etc.).
- The `sendemail` command-line utility.

## Configuration

To configure the Executor SendEmail, follow these steps:

1. Check if you have the `sendemail` command-line utility installed on your system. If not, you can install it using your system's package manager or by downloading it manually.

   Installation example on Ubuntu:

   ```bash
   sudo apt-get update
   sudo apt-get install sendemail

Replace your_username@gmail.com with your Gmail username, your_password with your Gmail password, smtp.example.com with the SMTP server you wish to use, sender@example.com with the sender's email address, recipient@example.com with the recipient's email address, "Subject" with the subject of the email, and "Message body" with the body of the email.

## Options

Here are some common options you can use with the `sendemail` command:

- `-o tls=no`: Disables TLS encryption.
- `-xu your_username@gmail.com`: Specifies the username for authentication.
- `-xp your_password`: Specifies the password for authentication.
- `-s smtp.example.com:587`: Specifies the SMTP server and port.
- `-f "sender@example.com"`: Specifies the sender's email address.
- `-t "recipient@example.com"`: Specifies the recipient's email address.
- `-u "Subject"`: Specifies the subject of the email.
- `-m "Message body"`: Specifies the body of the email.

## Example
`sendemail -f "sender@example.com" -t "recipient@example.com" -s smtp.example.com:587 -xu your_username@gmail.com -xp your_password -u "Subject" -m "Message body"`

a





