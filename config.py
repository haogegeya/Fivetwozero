import logging
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='log', level=logging.INFO, format=LOG_FORMAT)
HOST = '47.107.***,***'
PORT = '27017'
DATABASE = '***'
USERNAME = '***'
PASSWORD = '***'

DB_URI = "mongodb://{username}:{password}@{host}:{port}/{db}".format(username=USERNAME,password=PASSWORD, host=HOST,port=PORT, db=DATABASE)




class Config(object):
    JOBS = [
        {
            'id': 'job1',
            'func': 'spider:startScrapy.startOtherProcess',
            'trigger': 'cron',
            'hour':18,
            'minute':25,
            #'second':25
        }
    ]

    SCHEDULER_API_ENABLED = True
