import models
import stores

def create_members():
    member1 = models.Member('Khalid', 40)
    member2 = models.Member('Safwat', 43)
    print member1
    print member2
    print '=' * 32
    return (member1, member2)

def member_store_should_add_models(member_instances, member_store):
    for member in member_instances:
        member_store.add(member)

def create_posts():
    post1 = models.Post('Post1', 'This is the first Post model example')
    post2 = models.Post('Post2', 'Another post example. it is getting exciting')
    post3 = models.Post('Post3', 'Third post. Hopfully i got to the end of this task')
    print post1
    print post2
    print post3
    print '=' * 32
    return (post1, post2, post3)

def post_store_should_add_posts(post_instances, post_store):
    for post in post_instances:
        post_store.add(post)



member_store = stores.MemberStore()
post_store = stores.PostStore()

member_store_should_add_models(create_members(),member_store)
post_store_should_add_posts(create_posts(),post_store)
#member_store.add(member1)
#member_store.add(member2)

#post_store.add(post1)
#post_store.add(post2)
#post_store.add(post3)

m = member_store.get_by_id(1)
print m.name

p = post_store.get_by_id(1)
print p.title
member2 = models.Member('Safwat', 43)
print member_store.entity_exists(member2)
