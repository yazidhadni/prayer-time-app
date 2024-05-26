import os


def notification(message, title="Prayer App"):
    os.system(f'osascript -e \'display notification "{message}" with title "{title}"\'')
