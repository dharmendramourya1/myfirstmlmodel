import sys
import traceback

def error_message_detail(error, error_detail):
    """Return detailed error message with filename and line number."""
    _, _, exc_tb = sys.exc_info()

    if exc_tb is not None:
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
    else:
        file_name = "Unknown File"
        line_number = "Unknown Line"

    error_message = (
        f"Error occurred in python script name [{file_name}] "
        f"line number [{line_number}] "
        f"error message [{str(error)}]"
    )

    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail=None):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message
