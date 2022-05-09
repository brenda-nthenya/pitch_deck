from ensurepip import bootstrap
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config_optons

bootstrap= Bootstrap()
db = SQLAlchemy()

