class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def get_post_info(self):
        print(f"Title: {self.title}")
        print(f"Content: {self.content}")
        print(f"Author: {self.author}")
