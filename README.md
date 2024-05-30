# Email to Telegram Forwarder

This Python script forwards emails from a specified sender to a Telegram channel as screenshots. It is particularly useful for individuals managing multiple accounts or subscriptions, such as those using catchall domains or the Gmail "+" trick. The script connects to a Gmail IMAP server, searches for unread emails from the specified sender, extracts the email content (text or HTML), converts it to a screenshot, and sends it to a Telegram channel using a bot.

## Use Case

This script was originally designed to forward promotional emails & Connexion Codes from Uber Eats to a Telegram channel, allowing users to view and act upon the promotions quickly & Login. However, it can be easily modified to forward emails from any sender to any destination, making it a versatile tool for automating email-based tasks.

## Usage

1. **Set Up Gmail Credentials**: Replace the `username` and `password` variables with your Gmail credentials. Also, replace the `target_sender` variable with the email address of the sender whose emails you want to forward.

2. **Set Up Telegram Bot**: Create a new Telegram bot and obtain its token. Replace the `bot_token` variable with your bot's token. Also, replace the `channel_id` variable with the ID of the Telegram channel where you want to send the screenshots.

3. **Run the Script**: Execute the script using a Python interpreter. Ensure that you have the necessary dependencies installed (e.g., `imaplib`, `email`, `requests`, `imgkit`).

4. **Review Output**: Once the script starts running, it will continuously monitor your Gmail inbox for new emails from the specified sender. It will forward the email content as screenshots to the specified Telegram channel.

## Dependencies

- Python 3.x
- `imaplib`: The IMAP client library for accessing and manipulating email messages on an IMAP server.
- `email`: Module for parsing email messages.
- `requests`: Library for making HTTP requests.
- `time`: Module for time-related functions.
- `imgkit`: Library for converting HTML to images.

## Contributing

Feel free to contribute to this project by submitting bug reports, feature requests, or pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
