import random
import sqlalchemy
from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://daniilnovoselcev:09022004SMASHheart@localhost/typeapp")
engine.connect()
print(engine)




