from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///cats.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def add_meme(meme_name, meme_img):
	meme_object = meme(
		meme_name = meme_name,
		meme_img= meme_img)
	session.add(meme_object)
	session.commit()
	return meme_object


def add_comment(comment_poster, comment_rating , comment_content,on_post):
	comment_object = comment(
		comment_poster = comment_poster,
		comment_rating = comment_rating,
		comment_content = comment_content,
		on_post = on_post)
	session.add(comment_object)
	session.commit()
	return comment_object

def query_meme_by_name(meme_name):
	memes = session.query(meme).filter_by(meme_name=meme_name).all()
	return memes
def query_comments_by_post(on_post):
	comments = session.query(comment).filter_by(on_post = on_post).all()
	return comments
	



