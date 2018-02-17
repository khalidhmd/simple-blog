class MemberStore():
    members = []
    last_id = 1

    def get_all(self):
        return MemberStore.members

    def add(self, member):
        member.member_id = MemberStore.last_id
        MemberStore.members.append(member)
        MemberStore.last_id += 1

    def get_by_id(self, id):
        all_members = self.get_all()
        result = None
        for m in all_members:
            if m.member_id == id:
                result = m
        return result

    def entity_exists(self, member):
        result = False
        if member in MemberStore.members:
            result = True
        return result

    def delete(self, id):
        member = self.get_by_id(id)
        MemberStore.members.remove(member)

    



class PostStore():
    posts = []
    last_id = 1

    def get_all(self):
        return self.posts

    def add(self, post):
        post.post_id = PostStore.last_id
        PostStore.posts.append(post)
        PostStore.last_id += 1

    def get_by_id(self, id):
        all_posts = self.get_all()
        result = None
        for p in all_posts:
            if p.post_id == id:
                result = p
        return result

    def entity_exists(self, post):
        result = False
        if post in PostStore.posts:
            result = True
        return result

    def delete(self, id):
        post = self.get_by_id(id)
        PostStore.posts.remove(post)
