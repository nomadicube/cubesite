# python.exe .\app\app.py
from flask import *
import markdown
import os


app = Flask(__name__)


def get_blog_post_content(post_list):
    contents = []
    for filename in post_list:
        with open(filename, 'r') as file:
            post_rendered = markdown.markdown(file.read())
            contents.append(post_rendered)

    return contents


def get_blog_post_paths():
    titles = []
    root_path = os.path.dirname(__file__)
    blog_posts = os.path.join(root_path, 'posts')
    post_list = os.listdir(blog_posts)

    for filename in post_list:
        if not filename.endswith('.md'):
            continue

        file_path = os.path.join(blog_posts, filename)
        titles.append(file_path)

    return sorted(titles, reverse=True)


@app.route("/")
def hello_world():
    blog_posts = get_blog_post_content(get_blog_post_paths())
    #return blog_posts[1]
    return render_template('index.html',
                           blog_posts=blog_posts,
                           )


@app.route("/info")
def info():
    return render_template('info.html')


if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port=36)
    #app.run(debug=True,host="0.0.0.0",port=80)
