from database import get_db_connection

def check_password(input_password, stored_password):
    # Replace this with actual password hashing logic
    return input_password == stored_password

def register_user(nama, no_hp, password, role='user'):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "INSERT INTO users (nama, no_hp, password, role) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (nama, no_hp, password, role))
    conn.commit()
    conn.close()

def login_user(no_hp, password):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM users WHERE no_hp=%s AND password=%s"
    cursor.execute(query, (no_hp, password))
    user = cursor.fetchone()
    conn.close()
    return user

def get_user_by_credentials(username, password):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()
    conn.close()
    
    if user and check_password(password, user['password']):
        return user
    return None

def get_all_users():
    """
    Mengambil daftar semua pengguna dari database
    """
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return users
