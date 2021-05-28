from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask (__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'

db = SQLAlchemy(app)

class blogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(20), nullable=False, default='N/A')
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self) -> str:
        return 'Blog post ' + str(self.id)




all_posts = [
    {
        'title': 'Post 1',
        'content': 'this is the content of post 1',
        'author': 'Lucky Yoila'
    },

    {
        'title': 'Post 2',
        'content': 'this is the content of post 2',
    },

]

@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route('/posts')
def posts():
    return render_template('posts.html', posts = all_posts)





if __name__ == '__main__':
    app.run(debug=True)