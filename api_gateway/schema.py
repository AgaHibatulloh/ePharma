import graphene
import requests

class User(graphene.ObjectType):
    id = graphene.Int()
    username = graphene.String()
    nama = graphene.String()
    email = graphene.String()
    no_hp = graphene.String()

class Obat(graphene.ObjectType):
    id = graphene.Int()
    nama_obat = graphene.String()
    stok = graphene.Int()
    nama_kategori = graphene.String()

class Pesanan(graphene.ObjectType):
    id = graphene.Int()
    nama_pemesan = graphene.String()
    jumlah = graphene.Int()
    kategori = graphene.String()
    status = graphene.String()

class Query(graphene.ObjectType):
    obat = graphene.List(Obat)
    pesanan = graphene.List(Pesanan)
    users = graphene.List(User)
    
    def resolve_obat(self, info):
        try:
            result = requests.get('http://inventory-service:5002/api/obat')
            return result.json()
        except Exception as e:
            return []
    
    def resolve_pesanan(self, info):
        try:
            result = requests.get('http://order-service:5003/api/orders')
            return result.json()
        except Exception as e:
            return []
    
    def resolve_users(self, info):
        try:
            result = requests.get('http://user-service:5001/api/users')
            return result.json()
        except Exception as e:
            return []

schema = graphene.Schema(query=Query)