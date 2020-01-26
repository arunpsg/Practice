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
    elif len(group.get_users()) != 0:
        groupUsers = group.get_users()
        if user in groupUsers:
            return True
    else:
        return False

    for parent_group in given_group:
        if parent_group.get_users():
            groupUsers = parent_group.get_users()
            if user in groupUsers:
                return True
        elif not parent_group.get_groups():
            return False
        else:
            return is_user_in_group(user, parent_group)
    return False

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")
parent.add_group(child)
child.add_group(sub_child)
# sub_child_user = "sub_child_user"
sub_child.add_user("sub_child_user")




 #Test Case 1:
print("is_user_in_group : ", is_user_in_group("sub_child_user", parent))
# Expected output :
# is_user_in_group : True

 #Test Case 2:
print("is_user_in_group : ", is_user_in_group("", parent))
# Expected output :
# Please provide valid inputs
# is_user_in_group : False

 #Test Case 3:
# test_child_user = "test_child_user"
# test_child = Group("testchild")
# test_child.add_user(test_child_user)
# sub_child.add_group(test_child)
# print("is_user_in_group : ", is_user_in_group(test_child_user, sub_child))
# Expected output :
# is_user_in_group :  True

# test case 4 - fairly large amount of people in the group
level_11 = Group('a1')
level_21 = Group('b1')
level_22 = Group('b2')
level_23 = Group('b3')
level_11.add_group(level_22)
# level_21.add_group(level_22)
level_22.add_group(level_23)
level_23.add_user("timi")

print(is_user_in_group('timi', level_11))  # Returns True
print(is_user_in_group("desh", level_11))  # Return False

