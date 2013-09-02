from sqlalchemy import create_engine
from models import Base, Topic, Post
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:////tmp/talk.db', echo=True)
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

t1 = Topic('topic 1')
t1.posts = [Post('post 1 for topic 1'), Post('post 2 for topic 1')]

t2 = Topic('topic 2')
t2.posts = [Post('post 1 for topic 2'), Post('post 2 for topic 2')]


session.add_all([t1, t2])
session.commit()

print (">>>", session.query(Topic).all())
