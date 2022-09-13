from flask import Blueprint, request, render_template, redirect

from apps.user.module import User


user_blueprint = Blueprint('user', __name__)

users = []

@user_blueprint.route('/')
def user_center():
    return render_template('user/show.html', users=users)

@user_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        print(request.form)
        username = request.form.get('username')
        password = request.form.get('password')
        phone = request.form.get('phone')
        repassword = request.form.get('repassword')
        if password == repassword:
            # judge username unique
            for user in users:
                if user.username == username:
                    return render_template('user/register.html', msg='用户名已存在')
            # create User object
            user = User(username, password, phone)
            # append to users
            users.append(user)
            return redirect('/')
    return render_template('user/register.html')
        
@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    return '用户登录'

@user_blueprint.route('/delete_user')
def delete_user():
    username = request.args.get('username')
    for user in users:
        if user.username == username:
            users.remove(user)
            return redirect('/')
    else:
        return '删除失败'

@user_blueprint.route('/logout', methods=['GET', 'POST'])
def logout():
    return '用户退出'