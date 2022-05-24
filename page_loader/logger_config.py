# import os


def get_logger_config() -> dict:
    """Gets logger config with path to save .log file"""
    # file_name = 'logger.log'
    # full_path = os.path.join(path_to_log, file_name)

    logger_config = {
        'version': 1,
        'disable_existing_loggers': True,

        'formatters': {
            'file_format': {
                'format': '{asctime} | [{levelname}]  - {message}',
                'style': '{'
            },
            'console_format': {
                'format': '[{levelname}] {message}',
                'style': '{'
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'level': 'WARNING',
                'formatter': 'console_format'
            }
        },
        'loggers': {
            'best_logger': {
                'level': 'DEBUG',
                'handlers': ['file', 'console'],
                'propagate': False
            }
        }
    }
    return logger_config
