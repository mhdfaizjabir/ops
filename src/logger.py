import logging
import os 
from datetime import datetime


logfile = f"{datetime.now().strftime('%m-%d-%y-%H-%M-%S')}.log"

logs_path = os.path.join(os.getcwd(), "logs", logfile) #this line will create a log file in the logs directory with the current date and time in the filename
os.makedirs(logs_path,exist_ok=True) #this line will create the logs directory if it does not exist
logfile_path = os.path.join(logs_path, logfile) #this line will create the log file in the logs directory


logging.basicConfig(
    filename=logfile_path,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,



)


