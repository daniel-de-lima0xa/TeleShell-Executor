# TeleShell Executor

This is a Telegram bot that executes PowerShell commands sent by users and provides a simple interface for managing background sessions.

## Requirements

- Python 3.x
- Python Libraries: `python-telegram-bot`

## Configuration

1. Clone this repository:

    ```
    git clone https://github.com/your-username/teleshell-executor.git
    ```

2. Install the dependencies:

    ```
    pip install python-telegram-bot
    ```

3. Configure the following variables in the `config.py` file:

    - `TOKEN`: Telegram bot token.
    - `GROUP_CHAT_ID`: ID of the chat/group where the bot will operate.

## Usage

Run the `main.py` file to start the bot:


The bot will start and wait for commands sent by users. Additionally, it offers the following functionalities:

- `/send_ps`: Send a PowerShell command for execution.
- `/list`: List running sessions.
- `/background`: Leave a command in the background for continuous execution.
- `/menu`: Display the menu of options.

## Notes

- Make sure the bot has permission to read and send messages in the specified chat/group.

## Contribution

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

