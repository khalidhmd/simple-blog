
import models
import stores



def create_members():
    member1 = models.Member('Khalid', 40)
    member2 = models.Member('Safwat', 43)
    return (member1, member2)

def member_store_should_add_models(member_instances, member_store):
    for member in member_instances:
        member_store.add(member)


def member_store_should_add_update(member, member_store):
    member_example = models.Member(member.name, member.age, member.id)
    if member_example is not member:
        print('member and member_example are not the same')
    member_example.name = 'Mohamed'
    member_store.update(member_example)
    


def create_posts():
    post1 = models.Post('Post1', 'This is the first Post model example', 1)
    post2 = models.Post('Post2', 'Another post example. it is getting exciting', 1)
    post3 = models.Post('Post3', 'Third post. Hopfully i got to the end of this task', 2)
    return (post1, post2, post3)

def post_store_should_add_posts(post_instances, post_store):
    for post in post_instances:
        post_store.add(post)


member_store = stores.MemberStore()
post_store = stores.PostStore()

member_store_should_add_models(create_members(),member_store)
post_store_should_add_posts(create_posts(),post_store)

m = member_store.get_by_id(1)


#test get_by_is(id)
p = post_store.get_by_id(1)


#test entit_exists(member)
sample_member = models.Member('Safwat', 43)


#test update(member)
updated_member = models.Member('safwat Aly', 54, 2)
member_store.update(updated_member)
m = member_store.get_by_id(2)


#test get_by_name(name)
members_by_name = member_store.get_by_name('Khalid')

members_with_posts = member_store.get_members_with_posts(post_store)


top_one_member = member_store.get_top(post_store, 1)



