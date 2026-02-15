from linguist import *

def run_tests():
    print("Запуск тестів...")

    # Тест User
    u = user_create("Orest", "orest@test.com", "pass123")
    assert u.id is not None
    assert user_get_by_id(u.id).name == "Orest"
    
    user_update_name(u.id, "Orest Updated")
    assert user_get_by_id(u.id).name == "Orest Updated"
    
    assert user_change_password(u.id, "pass123", "new_pass") is True
    assert user_get_by_id(u.id).password == "new_pass"

    # Тест Deck
    d = deck_create("Travel", u.id)
    assert d.name == "Travel"
    assert deck_get_by_id(d.id).user_id == u.id
    
    deck_update(d.id, "Business")
    assert deck_get_by_id(d.id).name == "Business"

    # Тест Card
    c = card_create(u.id, "Apple", "Яблуко", "Fruit")
    assert c.word == "Apple"
    
    found = card_filter("Ябл")
    assert len(found) > 0
    assert found[0].word == "Apple"
    
    card_update(c.id, tip="Green fruit")
    assert card_get_by_id(c.id).tip == "Green fruit"

    # Тест видалення
    assert card_delete_by_id(c.id) is True
    assert deck_delete_by_id(d.id) is True
    assert user_delete_by_id(u.id) is True
    assert user_get_by_id(u.id) is None

    print("Всі тести пройдено успішно! ✅")

if __name__ == "__main__":
    print("Наповнюємо базу даними...")
    
    try:
        # Спробуємо створити користувача
        user = user_create("Орест", "orest@test.com", "pass123")
        print(f"Додано користувача: {user.name}")
        
        # Створюємо колоду та картки тільки якщо користувача щойно створили
        deck = deck_create("Мій перший набір", user.id)
        card1 = card_create(user.id, "Apple", "Яблуко", "Зелений фрукт")
        print(f"Додано картку: {card1.word}")
        
    except Exception as e:
        print(f"Користувач вже існує, пропускаємо створення. (Помилка: {e})")
        # Обов'язково скидаємо невдалу транзакцію!
        session.rollback() 

    # Тепер сесія чиста, і ми можемо читати дані
    print("\n--- Вміст таблиці CARDS ---")
    all_cards = session.query(Card).all()
    
    if not all_cards:
        print("Таблиця карток поки що порожня.")
    else:
        for c in all_cards:
            print(f"ID: {c.id} | {c.word} -> {c.translation}")