import logging 
# every excecution that probably happen should be able log all those info execution in some file , that will to track if there is some error , we will log that error
import os
from datetime import datetime

LOG_FILE =f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"    # my file name will created whatever daytime will be txt file
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)  #
os.makedirs(logs_path,exist_ok=True)


LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)   #wrt logging where ever i use logging.info probably i write any print message then i am going to use this kind bsicconfig its basically going to keep that format wrt message that we r going to get.

