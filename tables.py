from sqlalchemy import MetaData, Table, String, Integer, Column

from database import Base

# metadata = MetaData()
#
# words = Table('words', metadata,
#     Column('id', Integer(), primary_key=True),
#     Column('word', String(), nullable=False),
# )
#
# frequency_words = Table('frequency_words', metadata,
#     Column('id', Integer(), primary_key=True),
#     Column('word', String(), nullable=False),
# )

class Words(Base):
    __tablename__ = 'words'

    id = Column(Integer, primary_key=True, index=True)
    word = Column(String, index=True)

class FrequencyWords(Base):
    __tablename__ = 'frequency_words'

    id = Column(Integer, primary_key=True, index=True)
    word = Column(String, index=True)