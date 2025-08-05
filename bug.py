import logging
import datetime
import os
import sys
import config

# Custom console formatter simply outputs the level and the message.
class CustomConsoleFormatter(logging.Formatter):
    def format(self, record):
        # Simply return the log level and the message that was already formatted in bug()
        return f"{record.levelname} {record.getMessage()}"

def setup_logging(name, debug, console_output, log_dir):
    """
    Sets up a logger with a timestamped log file and separate formatters for 
    file and console outputs.
    
    Args:
        name (str): The unique name for the logger.
        debug (bool): If True, sets logging level to DEBUG; otherwise INFO.
        console_output (bool): If True, adds a StreamHandler for console output.
        log_dir (str): Directory where the log file will be saved.
    
    Returns:
        logger: A configured logger instance.
    """
    # Ensure the log directory exists.
    if not os.path.isdir(log_dir):
        os.makedirs(log_dir)
    
    # Generate a timestamp string for the log filename (e.g., debug_20251008_153045.log).
    timestamp = datetime.datetime.now().strftime(config.LOG_TIMESTAMP_FORMAT)
    log_file = os.path.join(log_dir, f"{name}_{timestamp}.log")
    
    # Create (or get) the logger.
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG if debug else logging.INFO)
    
    # Clear any existing handlers.
    if logger.hasHandlers():
        logger.handlers.clear()
    
    # Formatter for file output: include timestamp, level, and the plain message.
    file_formatter = logging.Formatter(config.FILE_LOG_FORMAT)
    
    # Custom console formatter: simply shows level and message.
    console_formatter = CustomConsoleFormatter()
    
    # Use sys.stdout for console output.
    if console_output:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(getattr(logging, config.CONSOLE_LOG_LEVEL))
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)
    
    # Always add a FileHandler to write logs to the log file.
    file_handler = logging.FileHandler(log_file, mode=config.LOG_FILE_MODE)
    file_handler.setLevel(getattr(logging, config.FILE_LOG_LEVEL))
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    
    return logger

# Get log directories from config.
log_dir_debug = config.LOG_DIR_DEBUG
log_dir_user_tracking = config.LOG_DIR_USER_TRACKING

# Create two loggers:
logger_debug = setup_logging(config.DEBUG_LOG_NAME, debug=True, console_output=True, log_dir=log_dir_debug)
logger_track = setup_logging(config.TRACKING_LOG_NAME, debug=True, console_output=False, log_dir=log_dir_user_tracking)

def bug(message, debug_level="debug", title=False):
    """
    Logs a message using the specified debug level.
    
    Args:
        message (str): The message to log.
        debug_level (str): One of "error", "warning", "debug", or "track".
        title (bool): If True, indicates a major section title.
    
    Behavior:
        - If title is True, the bug() function wraps the message with "~~~~~" borders.
        - Non-title messages are prefixed with a hyphen.
        - "error" and "warning" messages always show on the console.
        - "debug" messages display on the console only if config.DEBUG_TO_CONSOLE is True.
        - "track" messages are logged only to the tracking log file.
    """
    # Format the message based on the title flag.
    if title:
        border = config.TITLE_BORDER_CHAR * config.TITLE_BORDER_COUNT
        final_message = f"{border} {message} {border}"
    else:
        final_message = f"{config.MESSAGE_PREFIX} {message}"
    
    level = debug_level.lower()
    if level == "error":
        logger_debug.error(final_message)
    elif level == "warning":
        logger_debug.warning(final_message)
    elif level == "debug":
        if config.DEBUG_TO_CONSOLE:
            logger_debug.debug(final_message)
        else:
            # Temporarily suppress console output for debug messages.
            for handler in logger_debug.handlers:
                if isinstance(handler, logging.StreamHandler):
                    old_level = handler.level
                    handler.setLevel(logging.CRITICAL)
            logger_debug.debug(final_message)
            for handler in logger_debug.handlers:
                if isinstance(handler, logging.StreamHandler):
                    handler.setLevel(old_level)
    elif level == "track":
        logger_track.info(final_message)
    else:
        logger_debug.debug(final_message)

if __name__ == "__main__":
    # Demonstrate bug() usage.
    bug("Script started", "debug", title=True)    # Title message, will be wrapped.
    bug("Importing patient and plan data", "debug", title=True)
    bug("Retrieving ROI List", "debug")  # Non-title, so final_message becomes "- Retrieving ROI List"
    bug("This is a warning message", "warning")
    bug("This is an error message", "error")
    bug("This is a user tracking message", "track")
    
    # Direct usage examples.
    logger_debug.info("Direct logger_debug info message.")
    logger_track.info("Direct logger_track info message.")
