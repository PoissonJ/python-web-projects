from Database import Database
from models.Post import Post

Database.initialize()

blog = Blog(author="Jose",
            title="sample title",
            description="Sample description"
            )

blog.new_post()

blog.save_to_mongo()

Blog.from_mongo()

blog.get_posts() # Post.from_blog(id)
