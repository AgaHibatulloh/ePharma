import graphene
from models import get_all_obat, get_all_kategori, tambah_obat

class Obat(graphene.ObjectType):
    id = graphene.Int()
    nama_obat = graphene.String()
    stok = graphene.Int()
    nama_kategori = graphene.String()

class Kategori(graphene.ObjectType):
    id = graphene.Int()
    nama_kategori = graphene.String()

class Query(graphene.ObjectType):
    all_obat = graphene.List(Obat)
    all_kategori = graphene.List(Kategori)
    
    def resolve_all_obat(self, info):
        return get_all_obat()
        
    def resolve_all_kategori(self, info):
        return get_all_kategori()

class TambahObatInput(graphene.InputObjectType):
    nama_obat = graphene.String(required=True)
    stok = graphene.Int(required=True)
    kategori_id = graphene.Int(required=True)

class TambahObat(graphene.Mutation):
    class Arguments:
        input = TambahObatInput(required=True)
    
    obat = graphene.Field(lambda: Obat)
    
    def mutate(self, info, input):
        tambah_obat(input.nama_obat, input.stok, input.kategori_id)
        return TambahObat(obat={"nama_obat": input.nama_obat, "stok": input.stok})

class Mutation(graphene.ObjectType):
    tambah_obat = TambahObat.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)