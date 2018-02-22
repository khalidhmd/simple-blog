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
        mem = self.get_by_id(member.member_id)
        result = False
        if mem is not None:
            result = True
        return result

    def delete(self, id):
        member = self.get_by_id(id)
        MemberStore.members.remove(member)

    def update(self, member):
        all_members = self.get_all()
        for index, member_in_list in enumerate(all_members):
            if member_in_list.member_id == member.member_id:
                all_members[index] = member
                break
        
    def get_by_name(self, member_name):
       return (member for member in self.get_all() if member.name == member_name)
    
    def get_members_with_posts(self, post_store):
        all_members = self.get_all()
        for member in all_members:
            posts = post_store.get_by_member_id(member.member_id)
            member.member_posts = posts
        return all_members

    def get_top(self, post_store, top_number):
        all_members = self.get_members_with_posts(post_store)
        all_members = sorted(all_members, key=lambda member: len(member.member_posts), reverse=True)
        return all_members[:top_number]
    
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

    def get_by_member_id(self, member_id):
        all_posts = self.get_all()
        result = []
        for p in all_posts:
            if p.member_id == member_id:
                result.append(p)
        return result

    def entity_exists(self, post):
        result = False
        if post in PostStore.posts:
            result = True
        return result

    def delete(self, id):
        post = self.get_by_id(id)
        PostStore.posts.remove(post)
