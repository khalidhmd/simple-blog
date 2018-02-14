import models
import stores

member1 = models.Member('Khalid', 40, 1)
member2 = models.Member('Safwat', 43, 2)
post1 = models.Post('Post1', 'This is the first Post model example', 1)
post2 = models.Post('Post2', 'Another post example. it is getting exciting', 2)
post3 = models.Post('Post3', 'Third post. Hopfully i got to the end of this task', 3)

member_store = stores.MemberStore()
post_store = stores.PostStore()

member_store.add(member1)
member_store.add(member2)

post_store.add(post1)
post_store.add(post2)
post_store.add(post3)