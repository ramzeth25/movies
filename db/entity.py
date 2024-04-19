from datetime import datetime, date
from typing import Optional

from sqlalchemy import String, DateTime, Date, Boolean, Integer, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Movie(Base):
    __tablename__ = "movies"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(128))
    original_title: Mapped[str] = mapped_column(String(128))
    release_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    play_time: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    rating: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    max_rating: Mapped[int] = mapped_column(Integer)
    short_story: Mapped[str] = mapped_column(String(512))
    is_deleted: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    genre: Mapped[Optional[str]] = mapped_column(String(128))

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'original_title': self.original_title,
            'release_date': self.release_date,
            'genre': self.genre,
            'short_story': self.short_story,
            'play_time': self.play_time,
            'rating': self.rating,
            'max_rating': self.max_rating,
        }
