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
                break
        return result

    def entity_exists(self, member):
        result = False
        if member in MemberStore.members:
            result = True
        return result

    def delete(self, id):
        member = self.get_by_id(id)
        MemberStore.members.remove(member)

    def update(self, member):
        all_members = self.get_all()
        for member_in_list in all_members:
            if member_in_list.member_id == member.member_id:
                member_in_list.name = member.name
                member_in_list.age = member.age
                break
        
    def get_by_name(self, member_name):
        member_list = []
        all_members = self.get_all()
        for member in all_members:
            if member.name == member_name:
                member_list.append(member)
        return member_list

    
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
                break
        return result

    def entity_exists(self, post):
        result = False
        if post in PostStore.posts:
            result = True
        return result

    def delete(self, id):
        post = self.get_by_id(id)
        PostStore.posts.remove(post)
