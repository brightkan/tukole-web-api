def test_users(user_factory):
    user = user_factory()
    assert user.email == "test@tukole.co.ug"
