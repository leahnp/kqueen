from .ldap import LDAPAuth


class TestAuthMethod:
    def setup(self):
        self.username = "admin@example.org"
        self.password = "admin"

    def test_login_pass(self):
        auth_class = LDAPAuth()

        assert auth_class.verify(self.username, self.password)

    def test_login_bad_pass(self):
        auth_class = LDAPAuth()

        assert not auth_class.verify(self.username, 'no_password')

    def test_bad_server(self):
        auth_class = LDAPAuth(uri="ldap://127.0.0.1:55555")

        assert not auth_class.verify(self.username, self.password)
