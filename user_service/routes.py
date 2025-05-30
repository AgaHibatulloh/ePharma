from flask import Blueprint, render_template, request, redirect, session, url_for, jsonify
from flask_graphql import GraphQLView
from models import register_user, login_user, get_all_users
from schema import schema

user_bp = Blueprint('user', __name__)

@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nama = request.form['nama']
        no_hp = request.form['no_hp']
        password = request.form['password']
        register_user(nama, no_hp, password)
        return redirect('/login')
    return render_template('register.html')

@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        no_hp = request.form['no_hp']
        password = request.form['password']
        user = login_user(no_hp, password)
        if user:
            # Store user data in session
            session['user_id'] = user['id']
            session['user_name'] = user['nama']
            session['user_role'] = user.get('role', 'user')  # Default role to 'user' if not specified
            
            # Redirect to the dashboard service
            return redirect('http://localhost:5003/')
        else:
            error = "Nomor HP atau password salah"
    
    return render_template('login.html', error=error)

@user_bp.route('/api/users', methods=['GET'])
def api_users():
    users = get_all_users()  # Fungsi ini perlu ditambahkan di models.py
    return jsonify(users)

user_bp.add_url_rule(
    '/graphql', 
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  # untuk interface GraphQL interaktif
    )
)