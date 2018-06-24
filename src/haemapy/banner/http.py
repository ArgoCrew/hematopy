from apistar import Route, exceptions

routes = [
    ('/', method='GET', handler=list_users),
    ('/{user_id}', method='GET', handler=get_user),
]