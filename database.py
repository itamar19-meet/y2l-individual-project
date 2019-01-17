from models import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///cats.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def add_meme(meme_id , meme_name, meme_img, meme_age):
	meme_object = meme(
		meme_id =meme_id,
		meme_name = meme_name,
		meme_img= meme_img,
		meme_age = meme_age)
	session.add(meme_object)
	session.commit()
	return meme_object
def query_meme_by_name(meme_name):
	memes = session.query(meme).filter_by(meme_name=meme_name).all()
	return memes
