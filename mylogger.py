# Includes
import sys
import logging

def main(arguments):
        # import the first three arguments and prep them for use
        inputSCRIPT = arguments[0]                                                      # pulls the script name from the array ** Also used for problematic breakout**
        MyLEVEL = int(arguments[1])                                                     # turns the second argument into an integer to be used for the level
        inputMESSAGE = arguments[2]                                                     # pulls the third argument from the array **Also used for problematic breakout**
        MyMESSAGE = inputSCRIPT + ": " + inputMESSAGE           # concantinates the first and third arguments into a string to pass to the log file
        #print(MyMessage)

        # Prepar the Log Format, log file, and logger object
        LOG_FORMAT = "%(asctime)s - %(levelname)s -- %(message)s"
        logging.basicConfig(filename = "log.log", level = logging.DEBUG, format = LOG_FORMAT)
        logger = logging.getLogger()

        # Writes to the log based on severity
        if MyLEVEL == 1:                                                                        # This is the Debug level
                logger.debug(MyMESSAGE)
        elif MyLEVEL == 2:                                                                      # This is the Informational level
                logger.info(MyMESSAGE)
        elif MyLEVEL == 3:                                                                      # This is the Warning level
                logger.warning(MyMESSAGE)
        elif MyLEVEL == 4:                                                                      # This is the Error level
                logger.error(MyMESSAGE)
        elif MyLEVEL == 5:                                                                      # This is the Critical level
                logger.critical(MyMESSAGE)
        else:                                                                                           # This creates a log entry should the provided arguments not match one of the 5 log conditions
                LOG_FORMAT = "%(levelname)s %(asctime)s --- %(message)s"
                logger.critical("Logging system failure!!! Details to follow.")
                logger.info('%%%%%%%%%% Start of error paramiters %%%%%%%%%%')
                logger.critical(inputSCRIPT)
                logger.critical(MyLEVEL)
                logger.critical(inputMESSAGE)
                logger.info('%%%%%%%%%% End of error paramiters %%%%%%%%%%')

if __name__ == '__main__':
        main()


                                                                                                                                                                                   
