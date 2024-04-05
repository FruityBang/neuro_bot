# News Telegram Bot

This project is a Telegram bot developed using the aiogram library. The bot is designed to fetch news articles from Lenta.ru, provide jokes, and offer various interactive features to users on the Telegram platform.

## Stack
`Python` `aiogram` `asyncio` `bs4`

## Getting Started

To get started with this project, follow these steps:

1. Clone the repository to your local machine:

```bash
git clone https://github.com/FruityBang/neuro_bot.git
```

2. Install the required dependencies with poetry:

```bash
poetry install
```

3. Create a `.env` file in the project directory and add your Telegram bot token as in .env.example:

```
TOKEN=your_telegram_bot_token_here
```

4. Run the `main.py` script to start the bot:

```bash
python main.py
```

## Project Structure

The project consists of several modules:

- `main.py`: Contains the main script to initialize the Telegram bot and start the polling mechanism.
- `handlers.py`: Defines event handlers for various types of messages and callbacks received by the bot.
- `keys.py`: Contains keyboard layouts and utility functions for keyboard management.
- `parser.py`: Provides functions for parsing news articles and fetching data from external sources.
- `trans.py`: Secret one. 

## Usage

Once the bot is running, users can interact with it on Telegram by sending commands, selecting rubrics, ordering random news articles, and accessing secret features.

## Contributing

Contributions to this project are welcome! If you have any improvements, bug fixes, or new features to add, feel free to submit a pull request following the guidelines outlined in the CONTRIBUTING.md file.
