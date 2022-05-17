from page_loader.logger_config import get_logger_config

test_config = {
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
        'file': {
            'class': 'logging.FileHandler',
            'level': 'DEBUG',
            'formatter': 'file_format',
            'filename': 'test/logger.log'
        },
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


def test_get_logger_config():
    assert get_logger_config('test') == test_config
