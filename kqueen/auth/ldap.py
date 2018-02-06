import ldap
import logging

logger = logging.getLogger(__name__)


class LDAPAuth:
    def __init__(self, *args, **kwargs):
        LDAP_URI = kwargs.get('uri', "ldap://127.0.0.1")

        self.connection = ldap.initialize(LDAP_URI)

    def verify(self, username, password):
        dn = "cn=admin,dc=example,dc=org"

        try:
            bind = self.connection.simple_bind_s(dn, password)

            if bind:
                return True
        except ldap.INVALID_CREDENTIALS:
            logger.info("Invalid LDAP credentials for {}".format(dn))

            return False

        except ldap.LDAPError as e:
            logger.error(e)

        finally:
            self.connection.unbind()

        return False
