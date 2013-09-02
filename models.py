from json import dumps
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref


Base = declarative_base()


class Topic(Base):
    __tablename__ = 'topic'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    posts = relationship("Post", order_by="Post.id", backref="topic")


    def __init__(self, title):
        self.title = title

    def __repr__(self):
       return "<Topic('%s')>" % self.title


class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    body = Column(String)
    topic_id = Column(Integer, ForeignKey('topic.id'))


    def __init__(self, body):
        self.body = body

    def __repr__(self):
       return "<Post(Topic '%d' | '%s')>" % (self.topic_id, self.body)
