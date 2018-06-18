from movies.models import *
from api.general import generate_hash


class APIClient(models.Model):

    # Token related fields
    access_token = models.CharField(max_length=255, blank=True)
    expires_on = models.DateTimeField(null=True)
    expired = models.BooleanField(default=False)

    # Client related fields
    name = models.CharField(max_length=255)
    key = models.CharField(max_length=255)
    secret = models.CharField(max_length=255)

    @staticmethod
    def generate_key_and_secret():
        """
        Generates a random key and secret combo.
        """
        key = generate_hash()
        secret = generate_hash()

        return key, secret

    def set_key_and_secret(self, key=None, sec=None):
        """
        Associates the given key and secret to the
        instance of self. If no key and secret was
        passed, they will be automatically generated.
        """

        nkey, nsec = self.generate_key_and_secret()
        key = key if key else nkey
        sec = sec if sec else nsec

        # Associate key and secret with self.
        self.key = key
        self.secret = sec
        self.save()

    def save(self, *args, **kwargs):
        super(APIClient, self).save(*args, **kwargs)
        if not (self.key or self.secret):
            self.set_key_and_secret()
