from sqlalchemy import Column, Integer, DateTime, String, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin

from db.database import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, index=True, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False)
    player = relationship('Score', back_populates='user')


class Score(Base, SerializerMixin):
    __tablename__ = 'score'

    id = Column(Integer, index=True, primary_key=True)
    score = Column(Integer, default=0, nullable=False)
    rank = Column(Integer, default=1, nullable=False)
    date_time = Column(DateTime, nullable=True)
    player_id = Column(Integer, ForeignKey('user.id'))
    records = Column(MutableList.as_mutable(JSONB), nullable=True)
    user = relationship('User', back_populates='player')

    def obj_to_dict(self):  # for build json format
        return {
            'player_id': self.player_id,
            'score': self.score,
            'rank': self.rank,
        }