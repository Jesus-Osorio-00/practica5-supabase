from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()

sb = create_client(
    os.getenv('SUPABASE_URL'),
    os.getenv('SUPABASE_KEY')
)

nuevo = sb.table('productos').insert({
    'nombre': 'Laptop Gamer X500',
    'precio': 18999.99,
    'categoria': 'Electronica',
    'stock': 15
}).execute()

print('INSERT:', nuevo.data)

res = (
    sb.table('productos')
    .select('id, nombre, precio, stock')
    .eq('categoria', 'Electronica')
    .gt('stock', 0)
    .order('precio', desc=True)
    .execute()
)

print('Productos:', res.data)

sb.table('productos').update({
    'precio': 17499.99,
    'stock': 20
}).eq('nombre', 'Laptop Gamer X500').execute()

print('Producto actualizado')