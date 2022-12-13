from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, email, password, **kwargs):

        if not username:
            raise ValueError("The Username Must be Set")

        if not email:
            raise ValueError("The Email Must be Set")

        if not password:
            raise ValueError("The Password Must be Set")

        user = self.model(
            username=username, email=self.normalize_email(email), **kwargs
        )

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password, **kwargs):

        if not username:
            raise ValueError("The Username Must be Set")

        if not email:
            raise ValueError("The Email Must be Set")

        if not password:
            raise ValueError("The Password Must be Set")

        user = self.model(
            username=username, email=self.normalize_email(email), **kwargs
        )
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True

        user.set_password(password)
        user.save()

        return user
