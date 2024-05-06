# TeleShell-Executor

This is a Telegram bot written in Python that allows you to execute PowerShell commands, list running sessions, and run sessions in the background.

## Features

- **Send PowerShell Command**: Use the `/send_ps` command followed by the desired PowerShell command to execute it and receive the output in the Telegram chat.

- **List Running Sessions**: With the `/list` command, you can list all the sessions currently running in the bot.

- **Run Sessions in the Background**: Use the `/background` command followed by the PowerShell command to run a session in the background. This allows you to perform time-consuming tasks without blocking the bot.

- **Menu of Options**: The `/menu` command displays a menu with all available options.

## Configuration

Before using the bot, you need to configure the following variables in the code:

- `TOKEN`: Telegram bot token.
- `GROUP_CHAT_ID`: ID of the chat group where the bot will be active.

## Requirements

Make sure you have Python installed on your system. Additionally, you need to install the following dependencies:

- `python-telegram-bot`: To interact with the Telegram API.
- `subprocess`: To execute PowerShell commands.

You can install the dependencies using the following command:


## Usage

After configuring the bot and installing the dependencies, run the Python script. The bot will be active and respond to commands from the specified Telegram chat.

### Supported Commands

- `/send_ps <command>`: Executes the specified PowerShell command.
- `/list`: Lists all running sessions.
- `/background <command>`: Executes a PowerShell command in the background.
- `/menu`: Displays a menu with all available options.

## Contributions

Contributions are welcome! Feel free to open issues to report problems or suggest improvements. If you'd like to contribute directly, you can open pull requests with your changes.


