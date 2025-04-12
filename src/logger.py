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

# import logging
# import os
# from datetime import datetime
# import pytz

# class ISTFormatter(logging.Formatter):
#     """
#     Custom formatter to include IST timezone in the asctime.
#     """
#     def formatTime(self, record, datefmt=None):
#         """
#         Override formatTime to use IST.
#         """
#         ist_timezone = pytz.timezone('Asia/Kolkata')
#         dt = datetime.fromtimestamp(record.created, tz=pytz.utc).astimezone(ist_timezone)
#         if datefmt:
#             s = dt.strftime(datefmt)
#         else:
#             s = dt.isoformat()  # Use isoformat for a detailed representation
#         return s

# # Get the IST timezone (defined only once)
# indian_timezone = pytz.timezone('Asia/Kolkata')

# # Get the current IST time
# now_ist = datetime.now(indian_timezone)

# log_file = now_ist.strftime('%d %B %Y at %I:%M %p') + ".log"
# log_dir = os.path.join(os.getcwd(), 'logs')
# os.makedirs(log_dir, exist_ok=True)
# log_file_path = os.path.join(log_dir, log_file)

# # Create a handler and set the formatter
# handler = logging.FileHandler(log_file_path)
# formatter = ISTFormatter(fmt='%(asctime)s - %(lineno)d %(name)s - %(levelname)s - %(message)s',
#                            datefmt='%d %B %Y at %I:%M %p')  
# handler.setFormatter(formatter)

# # Create a logger and add the handler
# # logger = logging.getLogger(__name__) # Or any name you want
# # logger.addHandler(handler)
# # logger.setLevel(logging.INFO)  # Set the logging level

# # logger.info("This is a test log message in IST.")

# # print(f"Log file created at: {log_file_path}")
