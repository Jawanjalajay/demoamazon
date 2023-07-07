import logging
import inspect

class LogJenerator():
    @staticmethod
    def loggen():
        name=inspect.stack()[1][3]
        logger=logging.getLogger(name)
        logfile=logging.FileHandler("C:\\Users\\ajayj\\PycharmProjects\\Amazon\\logs\\amazon_automation.log")
        format=logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)d : %(message)s")
        logfile.setFormatter(format)
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        return logger









