from flask import Flask, request, render_template, url_for, redirect
from models import User, generate_random_user
app = Flask(__name__)


USERS = [generate_random_user() for _ in range(5)]

@app.route("/")
def user_list():
    return render_template('users.html', users=USERS)

@app.route('/users/create', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        # Отримуємо дані з форми
        username = request.form.get('username')
        email = request.form.get('email')
        age = request.form.get('age')
        phone = request.form.get('phone')
        user = User(username=username, email=email, age=age, phone=phone)
        USERS.append(user)
        # Створюємо новий об'єкт User (як у вашому коді)
        # new_user = User(username, email, age, phone)
        # database.save(new_user)
        
        return redirect(url_for('user_list')) # Повернення до списку
        
    return render_template('create_user.html')
@app.route('/users/delete/<user_pk>', methods=['GET'])
def delete_user(user_pk):
    for user in USERS:
        if user.pk == user_pk:
            USERS.remove(user)
            break
    return redirect(url_for('user_list'))


if __name__ == "__main__":
    print("Starting Flask app...")
    print("Available users:")
    for user in USERS:
        print(user)
    app.run(debug=True, host="0.0.0.0", port=5001)
