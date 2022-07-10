import logging

class logrec:

    def __init__(self,filename,level,format):
        self.filename = filename
        self.level = level
        self.format = format
        logging.basicConfig(filename=self.filename,
                            level=self.level,
                            format=self.format)

    def log(self,message,method):
        '''
                    logging the message based on the method
                    passed in this function
                    in the file
        '''
        if method == 'INFO':
            logging.info(message)
        else:
            logging.error(message)

class ineuron:
    def __init__(self):
        self.logger_in = logrec('log_file.txt', 'INFO', '%(levelname)s %(asctime)s %(name)s %(message)s')

    def student_welcome(self):
        '''
        this method prints the welcome
        :return:
        '''