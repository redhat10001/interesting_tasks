print('*' * 25)


class User:
    def __init__(self, group: str):
        self.group = group


user = User('admin')
group_to_process_method = {
    'admin': process_admin_request,
    'manager': process_manager_request,
    'client': process_client_request,
    'anon': process_anon_request,
}

print(group_to_process_method[user.group](user, request))
