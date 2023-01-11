# Multi-Logger

A Python package for creating a mixed and flexible logger with different outputs (console, file, Telegram, ELK, etc.).

## Usage

The package includes multiple options for logging, implemented in different classes, as seen below. Also, there is an example of usage in `usage_example.py`.

### BasicLogger

This logger is based on the `logging` package, and includes optional handlers for **rotating file** logger, **console** and also a **Logstash** handler.

### TelegramLogger

This logger sends the messages to a **Telegram bot** (that we must create previously, since we need the token). It also has an optional file logging for backup of messages.

### MultiLogger

Once we have created the different loggers, we can **add them to the MultiLogger** object, and use that as the main logger for the application, having different outputs in a single logging object.

## Preconfiguration

For using the **Telegram logger**, you must modify the file `multi_logger/telegram_logger.py` and include the bot ID and the chat IDs where the messages will be sent to.

For using the **ELK logger**, you need to specify the ELK host and port when adding the Logstash handler to the logger.

## Logging level

When creating a new logger object (like BasicLogger or TelegramLogger), you can specify the logging level for that logger. The logging level is a number between 0 and 3, where:

 * 0: Only show **error** and **exception** messages.
 * 1: Same as level 0 and also **warning** messages.
 * 2: Same as level 1 and also **information** messages.
 * 3: Show all messages (same as level 2 and also **debug** messages).

For example, you may want to log every message to the console or to a file, but only receive the error messages in your Telegram.
