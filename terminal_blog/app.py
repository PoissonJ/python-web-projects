from Database import Database
from models.Post import Post

Database.initialize()

posts = Post.from_blog(id='123')

for post in posts:
    print post
