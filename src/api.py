import requests

from os import link
def lookup_product(barcode_number):
    """Fetches product details using a barcode number."""

    BARCODE_API_URL = "https://api.barcodelookup.com/v3/products?barcode="  
    KEY= "&formatted=y&key={your_api_Key}"
    link = f"{BARCODE_API_URL}{barcode_number}{KEY}"

    response = requests.get(link)

    if response.status_code == 200:
        product_data = response.json()
        product_data_one=product_data.get("products", [{}])[0]
        product_name = product_data_one.get("title", "Unknown Product")
        description = product_data_one.get("description", "Unknown Product")
        ingredients = product_data_one.get("ingredients", "Unknown Product")
        return f"🔍 Product Name: {product_name} \n\n📦 Barcode: {barcode_number} \n\n📝 description: {description} \n\n🥗 ingredients: {ingredients} "
    
    return f"⚠️ Product not found for barcode: {barcode_number}"