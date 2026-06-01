from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()

sb = create_client(
    os.getenv('SUPABASE_URL'),
    os.getenv('SUPABASE_KEY')
)

productos = (
    sb.table('productos')
    .select('*')
    .gt('stock', 10)
    .execute()
)

for producto in productos.data:

    nuevo_precio = float(producto['precio']) * 0.90

    sb.table('productos').update({
        'precio': nuevo_precio
    }).eq('id', producto['id']).execute()

print('Descuento aplicado')