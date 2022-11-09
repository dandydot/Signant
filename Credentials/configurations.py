import configparser


def getConfig():
    config = configparser.ConfigParser()
    config.read('Credentials/properties.ini')
    return config


def password():
    return "Tester@@2022"


token = 'NTkxNTk5MTA5MjQ5MzQ5NDEwMTg1NTIxNDg0NDI5MjgwOTMyNjM='

