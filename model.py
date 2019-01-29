from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Write your classes here :
class comment(Base):
	__tablename__ = 'reviews1'
	comment_id = Column(Integer ,  primary_key = True , autoincrement=True)
	on_post = Column(Integer)
	comment_poster = Column(String)
	comment_content = Column(String)
	comment_rating = Column(Integer)
		
	
class meme(Base):
	__tablename__ = 'memes1'
	meme_id = Column(Integer, primary_key = True, autoincrement=True)
	meme_name = Column(String)
	meme_img = Column(String)
	likes = Column(Integer)
	