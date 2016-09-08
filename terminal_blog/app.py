from Database import Database
from models.Blog import Blog

Database.initialize()

blog = Blog(author="Jose",
            title="sample title",
            description="Sample description"
            )

blog.new_post()

blog.save_to_mongo()

from_database = Blog.get_from_mongo(blog.id)

print blog.get_posts() # Post.from_blog(id)
