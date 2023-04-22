import logging
import sys

def setup_logging():
    log_format = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    logging.basicConfig(
        level=logging.INFO,
        format=log_format,
        handlers=[
            logging.StreamHandler(sys.stdout),
            # Add other handlers like FileHandler, SMTPHandler, etc. as needed.
        ],
    )

    # Silence loggers from libraries if needed.
    logging.getLogger("uvicorn").setLevel(logging.WARNING)
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
