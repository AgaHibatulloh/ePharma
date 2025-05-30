from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from models import get_all_obat, get_kategori, tambah_obat, get_obat_by_id, update_obat, delete_obat
from datetime import datetime
from flask_graphql import GraphQLView
from schema import schema

# Buat blueprint
inventory_bp = Blueprint('inventory', __name__)

@inventory_bp.route('/')
def index():
    return redirect(url_for('inventory.daftar_obat'))

@inventory_bp.route('/obat')
def daftar_obat():
    obat = get_all_obat()
    current_time = datetime.now().strftime("%d %B %Y %H:%M")
    return render_template('daftar_obat.html', obat=obat, current_time=current_time)

@inventory_bp.route('/obat/tambah', methods=['GET', 'POST'])
def form_obat():
    if request.method == 'POST':
        nama_obat = request.form['nama_obat']
        stok = int(request.form['stok'])
        kategori_id = int(request.form['kategori_id'])
        
        tambah_obat(nama_obat, stok, kategori_id)
        return redirect(url_for('inventory.daftar_obat'))
    
    kategori = get_kategori()
    return render_template('tambah_obat.html', kategori=kategori)

@inventory_bp.route('/api/obat', methods=['GET'])
def api_obat():
    obat_list = get_all_obat()
    return jsonify(obat_list)

# Tambahkan di akhir file
inventory_bp.add_url_rule(
    '/graphql', 
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  
    )
)
