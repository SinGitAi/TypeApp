from sqlalchemy.orm import Session

from database import get_db
from tables import FrequencyWords, Words
import random


def choice_words(num_words):
    id_frequency_words = [random.randint(0, 5000) for i in range(num_words // 2)]
    id_words = [random.randint(0, 1532618) for i in range(num_words // 2)]
    print(id_frequency_words)
    print(id_words)
    return id_words, id_frequency_words


def get_words(db: Session, id_frequency_words: list, id_words: list):
    words_obj = db.query(Words).where(Words.id.in_(id_words)).all()
    frequency_words_obj = db.query(FrequencyWords).where(FrequencyWords.id.in_(id_frequency_words)).all()

    words = [obj.word for obj in words_obj]
    frequency_words = [obj.word for obj in frequency_words_obj]

    print(words, frequency_words)

    return words, frequency_words


def gen_text(words: list, frequency_words: list):
    text = list(words + frequency_words)
    random.shuffle(text)

    return " ".join(text)

def main():
    id_words, id_frequency_words = choice_words(100)
    words, frequency_words = get_words(next(get_db()), id_words=id_words, id_frequency_words=id_frequency_words)
    print(gen_text(words, frequency_words))


if __name__ == '__main__':
    main()


