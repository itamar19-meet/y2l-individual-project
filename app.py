from flask import Flask ,  render_template, request
app = Flask(__name__)

@app.route('/')
def search():
	if(request.method == 'GET'):
        return render_template("home.html")
    else:

  

@app.route('/add_meme',  methods=['GET', 'POST'])
def add_event_route():
    if(request.method == 'GET'):
        return render_template("add_meme.html")
    else:                                                          
        meme_name = request.form['meme_name']
        meme_img = request.form['meme_img']
        meme_age = request.form['meme_age'] 
        
        add_meme(meme_name , meme_img , meme_age)
        return 
@app.route('/search' , methods=['GET', 'POST'])
def query_memes(key_word):
	if(request.method == 'GET'):
        return render_template("search.html")

 

if __name__ == '__main__':
    app.run(debug=True)

