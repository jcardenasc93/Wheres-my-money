""" This module handles the app configuration """

import os

from db.mongodb import DBManager

class AppConfig:
    """ Defines the required app configuration """

    def __init__(self):
        """ Class constructor that validates a previous existing
        instance
        """
        self.module_name = "main:app"
        self.host = os.getenv("HOST_IP", "0.0.0.0")
        self.port = int(os.getenv("HOST_PORT", 1906))
        self.db = DBManager()
        self._get_env()

    def _get_env(self):
        """ Defines extra app configuration based
        on the env
        """
        self.environmnet = os.getenv("ENVIRONMENT", "local")
        self.reload = True if self.environmnet == "local" else False

class AppConfigManager:
    """ Defines App configuration manager based on
    singleton pattern
    """
    __app_instance = None

    def __new__(cls):
        if not cls.__app_instance:
            cls.__app_instance = AppConfig()
        return cls.__app_instance

    def __getattr__(self, attr):
        """ Delegate access to config implementation """
        return getattr(AppConfigManager.__app_instance, attr)
