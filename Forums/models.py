class Member():
    def __init__(self, name, age, id = 0):
        self.member_id = id
        self.name = name
        self.age = age
        self.member_posts = []

    def __str__(self):
        return 'Name: {}, Age: {}, Posts: {}'.format(self.name, self.age, len(self.member_posts))

class Post():
    def __init__(self, title, body, member_id, id = 0):
        self.post_id = id
        self.title = title
        self.body = body
        self.member_id = member_id

    def __str__(self):
        return 'Title: {}, Content: {}'.format(self.title, self.body)
