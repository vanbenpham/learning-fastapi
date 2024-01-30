from pydantic import BaseSettings
import os

class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_username: str
    database_name: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        if os.environ.get("USE_DOTENV", "false").lower() == "true":
            env_file = '.env'
        else:
            env_file = None


settings = Settings(database_hostname=os.environ['DATABASE_HOST'])

# from pydantic import BaseSettings, PostgresDsn
# from typing import Optional
# import os
# import urllib.parse

# class Settings(BaseSettings):
#     database_url: Optional[PostgresDsn] = None
#     secret_key: str
#     algorithm: str
#     access_token_expire_minutes: int

#     @property
#     def database_hostname(self) -> str:
#         return self._get_db_component("hostname")

#     @property
#     def database_port(self) -> str:
#         return self._get_db_component("port")

#     @property
#     def database_username(self) -> str:
#         return self._get_db_component("username")

#     @property
#     def database_password(self) -> str:
#         return self._get_db_component("password")

#     @property
#     def database_name(self) -> str:
#         return self._get_db_component("path")[1:]  # Remove leading '/'

#     def _get_db_component(self, component: str) -> str:
#         if self.database_url:
#             result = urllib.parse.urlparse(self.database_url)
#             return getattr(result, component)
#         return ""

#     class Config:
#         env_file = '.env'
#         env_file_encoding = 'utf-8'
#         case_sensitive = True
#         fields = {
#             'database_url': {'env': 'DATABASE_URL'},
#         }

# # Load settings from the environment variable if available, otherwise from .env
# settings = Settings(_env_file=os.environ.get('ENV_PATH', '.env'))

