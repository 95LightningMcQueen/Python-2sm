import pandas as pd
import os
from datetime import datetime


def log_decorator(func):
    def wrapper(*args, **kwargs):
        filename = 'logs.csv'
        user = os.getlogin()
        now = datetime.now()
        d = now.strftime('%d.%m.%Y')
        t = now.strftime('%H:%M:%S')
        if os.path.exists(filename) and os.path.getsize(filename) > 0:
            old_data = pd.read_csv(filename)
            new_id = len(old_data) + 1
        else:
            new_id = 1
        row = [[new_id, user, func.__name__, d, t]]
        headers = ['id', 'pc_username', 'function_name', 'Date', 'Time']
        df_row = pd.DataFrame(row, columns=headers)
        if not os.path.exists(filename):
            df_row.to_csv(filename, index=False)
        else:
            df_row.to_csv(filename, mode='a', index=False, header=False)
        return func(*args, **kwargs)
    return wrapper
