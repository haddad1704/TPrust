from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Text, CheckConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .db import Base

class Party(Base):
    __tablename__ = 'parties'

    id = Column(Integer, primary_key=True)
    name = Column(Text)
    started = Column(Boolean, default=False)
    max_players = Column(Integer)
    nb_tours = Column(Integer)
    time_limit = Column(Integer)

    players = relationship("Player", back_populates="party")
    tours = relationship("Tour", back_populates="party")
    cells = relationship("Cell", back_populates="party")


class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    username = Column(Text)
    role = Column(String, CheckConstraint("role IN ('wolf', 'villager')"))
    is_alive = Column(Boolean, default=True)
    party_id = Column(Integer, ForeignKey('parties.id'))

    party = relationship("Party", back_populates="players")
    actions = relationship("Action", back_populates="player")


class Tour(Base):
    __tablename__ = 'tours'

    id = Column(Integer, primary_key=True)
    party_id = Column(Integer, ForeignKey('parties.id'))
    round_number = Column(Integer)
    started_at = Column(DateTime(timezone=True), default=func.now())
    ended_at = Column(DateTime(timezone=True), nullable=True)

    party = relationship("Party", back_populates="tours")
    actions = relationship("Action", back_populates="tour")


class Action(Base):
    __tablename__ = 'actions'

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    tour_id = Column(Integer, ForeignKey('tours.id'))
    direction = Column(String)  # "01", "10", etc.
    decision_time = Column(DateTime(timezone=True), default=func.now())

    player = relationship("Player", back_populates="actions")
    tour = relationship("Tour", back_populates="actions")


class Cell(Base):
    __tablename__ = 'cells'

    id = Column(Integer, primary_key=True)
    party_id = Column(Integer, ForeignKey('parties.id'))
    row = Column(Integer)
    col = Column(Integer)
    content = Column(Integer)  # 0: vide, 1: villageois, 2: loup, 3: obstacle

    party = relationship("Party", back_populates="cells")
