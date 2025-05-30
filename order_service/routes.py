import requests
from flask import Blueprint, render_template, request, redirect, session, jsonify
from models import simpan_pesanan, get_all_pesanan
from ai_gemini import konsultasi_ai_gemini
import json
from datetime import datetime
from flask_graphql import GraphQLView
from schema import schema


order_bp = Blueprint('order', __name__)

@order_bp.route('/pesan', methods=['GET', 'POST'])
def buat_pesanan():
    # Ambil data obat dari Inventory Service
    res = requests.get('http://localhost:5002/api/obat')
    daftar_obat = res.json() if res.status_code == 200 else []

    if request.method == 'POST':
        nama = request.form['nama']
        id_obat = request.form['id_obat']
        jumlah = request.form['jumlah']
        kategori = request.form['kategori']
        simpan_pesanan(nama, id_obat, jumlah, kategori)
        return redirect('/pesanan')

    return render_template('buat_pesanan.html', daftar_obat=daftar_obat)

@order_bp.route('/pesanan')
def lihat_pesanan():
    semua = get_all_pesanan()
    current_time = datetime.now().strftime("%d %B %Y %H:%M")
    return render_template('daftar_pesanan.html', pesanan=semua, current_time=current_time)



@order_bp.route('/konsultasi', methods=['GET', 'POST'])
def konsultasi_obat():
    if request.method == 'POST':
        keluhan = request.form['keluhan']
        hasil_raw = konsultasi_ai_gemini(keluhan)
        return render_template("hasil_konsultasi.html", hasil=hasil_raw, keluhan=keluhan)

    return render_template("form_konsultasi.html")

@order_bp.route('/')
def dashboard():
    # Check if user is logged in
    if 'user_id' not in session:
        # User is not logged in, show general dashboard
        return render_template('dashboard.html', is_logged_in=False)
    
    # User is logged in, check role
    user_role = session.get('user_role', 'user')
    user_name = session.get('user_name', 'User')
    
    if user_role == 'admin':
        # Admin dashboard
        return render_template('dashboard.html', 
                              is_logged_in=True,
                              is_admin=True,
                              user_name=user_name)
    else:
        # Regular user dashboard
        return render_template('dashboard.html', 
                              is_logged_in=True, 
                              is_admin=False,
                              user_name=user_name)

@order_bp.route('/api/orders', methods=['GET'])
def api_orders():
    pesanan = get_all_pesanan()
    return jsonify(pesanan)

order_bp.add_url_rule(
    '/graphql', 
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  # untuk interface GraphQL interaktif
    )
)





