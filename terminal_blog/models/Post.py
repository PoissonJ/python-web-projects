class Post(object):

    def __init__(self, blog_id, title, content, author, id, data):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = date
        self.id = id

    def save_to_mongo(self):
        Database.insert(collection='posts', data=self.json())

    def json(self):
        return {
            'id': self.id,
            'blog_id': self.blog_id,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'created_date': self.created_date
        }
