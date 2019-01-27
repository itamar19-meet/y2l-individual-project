from flask import Flask ,  render_template, request
import database
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/add_meme',  methods=['GET','POST'])
def add_meme_route():
    if(request.method == 'GET'):
        return render_template("add_meme.html")
    else:                                                          
        meme_name = request.form['meme_name']
        meme_img = request.form['meme_img']
        database.add_meme(meme_name , meme_img , 0)
        return render_template("home.html")

@app.route('/search' , methods=['GET', 'POST'])
def query_memes():
    if(request.method == 'GET'):
        return render_template("search.html")
    else:
        return render_template("the_meme.html" , memez = database.query_meme_by_name(request.form['meme_name']))
     
@app.route('/the_meme' , methods=['GET', 'POST'])
def add_comment():
    if(request.method == 'GET'):
        return render_template("the_meme.html")
    else:
        comment_poster = request.form['comment_poster']
        comment_rating = request.form['comment_rating']
        comment_content = request.form['comment_content']
        on_post = int(request.form["meme_id"])
        database.add_comment(comment_poster, comment_rating , comment_content,on_post)
        return render_template("the_meme.html" , commentz = database.query_comments_by_post(on_post) , memez = database.query_meme_by_name(request.form['meme_name']))

@app.route('/add_like' , methods=['GET', 'POST'])
def add_like_route():
    if(request.method == 'GET'):
        return render_template("the_meme.html")
    else:
        meme_id= int(request.form["meme_id"])
        database.add_like(meme_id)
        return render_template("the_meme.html" , memez = database.query_meme_by_name(request.form['meme_name']))



if __name__ == '__main__':
    app.run(debug=True)

