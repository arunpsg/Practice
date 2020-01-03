class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if not user or not group:
        print("Please provide valid inputs")
        return False

    if group.get_groups():
        given_group = group.get_groups()
    elif group.get_users():
        groupUsers = group.get_users()
        for group_user_value in groupUsers:
            if group_user_value is user:
                return True
    else:
        return False

    for parent_group in given_group:
        if parent_group.get_users():
            groupUsers = parent_group.get_users()
            for group_user_value in groupUsers:
                if group_user_value is user:
                    return True

    while given_group:
        for temp_group in given_group:
            if temp_group.get_users():
                temp_users = temp_group.get_users()
                for user_value in temp_users:
                    if user_value is user:
                        return True
            elif temp_group.get_groups():
                given_group = temp_group.get_groups()
    return False


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

 #Test Case 1:
print("is_user_in_group : ", is_user_in_group(sub_child_user, parent))
# Expected output :
# # is_user_in_group : True

 #Test Case 2:
print("is_user_in_group : ", is_user_in_group("", parent))
# Expected output :
# Please provide valid inputs
# is_user_in_group : False

 #Test Case 3:
test_child_user = "test_child_user"
test_child = Group("testchild")
test_child.add_user(test_child_user)
sub_child.add_group(test_child)
print("is_user_in_group : ", is_user_in_group(test_child_user, sub_child))
# Expected output :
# is_user_in_group :  True


