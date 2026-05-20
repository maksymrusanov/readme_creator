# Notes TG

A minimalist and efficient Telegram bot designed for capturing, organizing, and retrieving personal notes directly within the Telegram interface.

## Description

**Notes TG** is a Python-based Telegram bot that acts as a personal digital notebook. It allows users to send messages, links, or snippets to a private chat, which are then parsed and stored for future reference. It is designed for users who want a frictionless way to save information without switching to dedicated note-taking apps.

## Features

*   **Quick Capture:** Save text notes instantly via Telegram messages.
*   **Persistent Storage:** Notes are safely stored in a structured database.
*   **Retrieval:** Easily query your saved notes.
*   **Lightweight:** Minimal dependencies and low resource consumption.
*   **Privacy-First:** Designed to run on your own infrastructure.

## Installation

### Prerequisites
*   Python 3.9+
*   A Telegram Bot Token (obtained via [@BotFather](https://t.me/botfather))

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/maksymrusanov/notes_tg.git
   cd notes_tg
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure your environment variables:
   Create a `.env` file in the root directory and add your credentials:
   ```env
   TELEGRAM_TOKEN=your_bot_token_here
   ```

4. Run the bot:
   ```bash
   python main.py
   ```

## Usage

1. Start a conversation with your bot on Telegram.
2. Follow steps  to create a note.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. **Fork** the repository.
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`).
3. **Commit** your changes (`git commit -m 'Add some amazing feature'`).
4. **Push** to the branch (`git push origin feature/amazing-feature`).
5. **Open a Pull Request**.

Please ensure your code follows PEP 8 guidelines and includes tests where applicable.

## License

This project is licensed under the **MIT License**. See the `LICENSE` file for more details.
