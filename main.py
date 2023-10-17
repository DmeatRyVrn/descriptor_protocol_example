class UserName:
    def __get__(self, obj, type=None):
        return 'User ' + str(getattr(obj, '_name'))

    def __set__(self, obj, value):
        if len(value) > 8:
            raise ValueError('The username is too long!')
        setattr(obj, '_name', value)


class User:

    name = UserName()

    def __init__(self):
        self._name = ''


if __name__ == '__main__':
    user_1 = User()
    user_1.name = 'Arnold'
    assert user_1.name == 'User Arnold'

    user_2 = User()
    user_2.name = 'Lee'
    assert user_2.name == 'User Lee'

    user_3 = User()
    try:
        user_3.name = 'Harrelson'
    except ValueError as ex:
        assert str(ex) == 'The username is too long!'
