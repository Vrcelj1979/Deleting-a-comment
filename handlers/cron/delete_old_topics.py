from handlers.base import BaseHandler
import datetime
from models.topic import Topic

class DeleteOldTopicsCron(BaseHandler):
    def get(self):
        topics = Topic.query(Topic.deleted == True,
                             Topic.updated < datetime.datetime.now() -
                             datetime.timedelta(minute=10)).fetch()

        for topic in topics:
            topic.key.delete()