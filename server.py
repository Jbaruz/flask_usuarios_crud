from flask import Flask, render_template, flash, session, request, redirect
from user import User
app = Flask(__name__)
app.secret_key = 'loquesea'

@app.route('/users')
def all_users():
    all_users = User.get_all()
    print(all_users)
    return render_template('index.html', all_users=all_users)

@app.route('/users/<id>')
def users_to_edit(id):
        return render_template('users_detail.html', user = User.get_by_id(id))

@app.route('/users/edit/<id>')
def users_detail(id):
        return render_template('editUser.html', user = User.get_by_id(id))

@app.route('/users/new', methods=['GET', 'POST'])
def add_new_user():
    print(f'REQUEST TYPE', request.method)
    if request.method == 'GET':
        return render_template('addNewUser.html')

    elif request.method == 'POST':
        print(F'AQUI--->',request.method)
        data = {
            "first_name": request.form['first_name'],
            "last_name": request.form['last_name'],
            "email": request.form['email']
        }
        results=User.insert_user(data)
        print(f'result in route', results)
        if results != False:
            return redirect('/users')
        else:
            flash('There was an error inserting a new user', 'danger')
            return redirect('/users/new')

@app.route('/update/<id>', methods=['GET', 'POST'])
def update_user(id):
    data = {
        'id': id
        }
    User.update(data)
    flash(f"success updating user", 'success')
    return redirect('/users')

@app.route('/delete/<id>', methods=['GET'])   
def delete_user(id):
    
    User.delete(id)
    flash(f"success deleting user {id}", 'success')
    return redirect('/users')

if __name__ == '__main__':
    app.run(debug=True)