import logging
import os
from datetime import datetime 
import pytz

# Get the IST timezone
indian_timezone = pytz.timezone('Asia/Kolkata')

# Get the current UTC time
now_utc = datetime.utcnow()

# Convert UTC time to IST
now_ist = now_utc.astimezone(indian_timezone)

# You can also get the current IST directly (less recommended for internal logic)
# now_ist_direct = datetime.now(indian_timezone)


log_file = f"{datetime.now(indian_timezone).strftime('%d %B %Y at %I:%M %p')}.log"
log_path = os.path.join(os.getcwd(), 'logs',log_file)
os.makedirs(log_path, exist_ok=True)

log_file_path = os.path.join(log_path, log_file)

logging.basicConfig(
    filename = log_file_path,
    format = '%(asctime)s - %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level = logging.INFO
)

# if __name__ == '__main__':
#   logging.info('Logging has satrted')