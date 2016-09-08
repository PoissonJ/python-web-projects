from Database import Database
from models.Blog import Blog

class Menu(object):

    def __init__(self):
        self.user = raw_input("Enter your author name: ")
        self.user_blog = None
        if self._user_has_account():
            print("Welcome back {}".format(self.user))
        else:
            self._prompt_user_for_account()
        pass

    def run_menu(self):
        read_or_write = input("Do you want to (R) or write (W) blogs?")
        if read_or_write == 'R':
            pass
        elif read_or_write == 'W':
            pass
        else:
            print("Thank you for blogging!")

    def _user_has_account(self):
        blog = Database.find_one('blogs', {'author': self.user})
        if blog is not None:
            self.user_blog = blog
            return True
        return False

    def _prompt_user_for_account(self):
        title = raw_input("Enter blog title: ")
        description = raw_input("Enter blog description: ")
        blog = Blog(self.user, self.title, self.description)
        blog.save_to_mongo()
        self.user_blog = blog
