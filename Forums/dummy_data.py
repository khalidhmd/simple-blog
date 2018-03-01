import models
import stores


def create_members():
    member1 = models.Member('Khalid', 40)
    member2 = models.Member('Safwat', 43)
    return (member1, member2)


def create_posts():
    post1 = models.Post('Post1', 'This is the first Post model example', 1)
    post2 = models.Post(
        'Post2', 'Another post example. it is getting exciting', 1)
    post3 = models.Post(
        'Post3', 'Third post. Hopfully i got to the end of this task', 2)
    return (post1, post2, post3)
