class Member():
    def __init__(self, name, age, id):
        self.member_id = id
        self.name = name
        self.age = age
        self.member_posts = []

class Post():
    def __init__(self, title, body, id):
        self.post_id = id
        self.title = title
        self.body = body
