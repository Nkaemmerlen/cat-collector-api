from datetime import datetime
from api.models.db import db

class Toy(db.Model):
  __tablename__ = 'toys'