
from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    # Add other player-related fields

class RatingHistory(Base):
    __tablename__ = 'rating_history'

    id = Column(Integer, primary_key=True, index=True)
    player_id = Column(Integer, index=True)
    rating_data = Column(JSON)
    # Add other rating history fields
