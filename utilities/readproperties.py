import configparser

config=configparser.RawConfigParser()
config.read('C:\\Users\\ajayj\\PycharmProjects\\Amazon\\Configuration\\config.ini')

class readconfig():
    @staticmethod
    def geturl():
        url=config.get('common info','url')
        return url

    @staticmethod
    def getemail_or_phone():
        email_or_phone=config.get('common info','email_or_phone')
        return email_or_phone

    @staticmethod
    def getpassword():
        password=config.get('common info','password')
        return password