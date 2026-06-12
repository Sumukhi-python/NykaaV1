import logging

class LogGen():
    @staticmethod
    def loggen():
        logging.basicConfig(filename="C:\\Users\\sumuk\\PycharmProjects\\logs\\automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        return logger
