from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

# Налаштування бази даних (SQLite у пам'яті для тестів або файл linguist.db)
engine = create_engine('sqlite:///linguist.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# --- МОДЕЛІ ---

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    decks = relationship("Deck", back_populates="user", cascade="all, delete-orphan")

class Deck(Base):
    __tablename__ = 'decks'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="decks")

class Card(Base):
    __tablename__ = 'cards'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    word = Column(String)
    translation = Column(String)
    tip = Column(String)

# Створення таблиць
Base.metadata.create_all(engine)

# --- ФУНКЦІЇ USER ---

def user_create(name, email, password) -> User:
    """Створює нового користувача та повертає об'єкт User."""
    new_user = User(name=name, email=email, password=password)
    session.add(new_user)
    session.commit()
    return new_user

def user_get_by_id(user_id) -> User:
    """Отримує користувача за ID."""
    return session.get(User, user_id)

def user_update_name(user_id, name) -> User:
    """Оновлює ім'я користувача."""
    user = user_get_by_id(user_id)
    if user:
        user.name = name
        session.commit()
    return user

def user_change_password(user_id, old_password, new_password) -> bool:
    """Змінює пароль користувача. Повертає True у разі успіху."""
    user = user_get_by_id(user_id)
    if user and user.password == old_password:
        user.password = new_password
        session.commit()
        return True
    return False

def user_delete_by_id(user_id) -> bool:
    """Видаляє користувача за ID."""
    user = user_get_by_id(user_id)
    if user:
        session.delete(user)
        session.commit()
        return True
    return False

# --- ФУНКЦІЇ DECK ---

def deck_create(name, user_id) -> Deck:
    """Створює нову колоду для користувача."""
    new_deck = Deck(name=name, user_id=user_id)
    session.add(new_deck)
    session.commit()
    return new_deck

def deck_get_by_id(deck_id) -> Deck:
    """Отримує колоду за ID."""
    return session.get(Deck, deck_id)

def deck_update(deck_id, name) -> Deck:
    """Оновлює назву колоди."""
    deck = deck_get_by_id(deck_id)
    if deck:
        deck.name = name
        session.commit()
    return deck

def deck_delete_by_id(deck_id) -> bool:
    """Видаляє колоду за ID."""
    deck = deck_get_by_id(deck_id)
    if deck:
        session.delete(deck)
        session.commit()
        return True
    return False

# --- ФУНКЦІЇ CARD ---

def card_create(user_id, word, translation, tip) -> Card:
    """Створює нову картку."""
    new_card = Card(user_id=user_id, word=word, translation=translation, tip=tip)
    session.add(new_card)
    session.commit()
    return new_card

def card_get_by_id(card_id) -> Card:
    """Отримує картку за ID."""
    return session.get(Card, card_id)

def card_filter(sub_word) -> tuple[Card]:
    """Фільтрує картки за підрядком у полях word, translation або tip."""
    cards = session.query(Card).filter(
        Card.word.contains(sub_word) | 
        Card.translation.contains(sub_word) | 
        Card.tip.contains(sub_word)
    ).all()
    return tuple(cards)

def card_update(card_id, word=None, translation=None, tip=None) -> Card:
    """Оновлює поля картки."""
    card = card_get_by_id(card_id)
    if card:
        if word: card.word = word
        if translation: card.translation = translation
        if tip: card.tip = tip
        session.commit()
    return card

def card_delete_by_id(card_id) -> bool:
    """Видаляє картку за ID."""
    card = card_get_by_id(card_id)
    if card:
        session.delete(card)
        session.commit()
        return True
    return False