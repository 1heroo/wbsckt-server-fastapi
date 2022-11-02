from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Anti Chat"
    admin_email: str = 'iswearican.a@gmail.com'
    # items_per_user: int = 50


settings = Settings()
