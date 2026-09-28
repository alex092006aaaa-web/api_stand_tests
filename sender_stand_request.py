import configuration
import requests
import data

#def get_users_table():
    #return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

#response = get_users_table()
#print(response.status_code)
# lo comentado es para solicitudes de respuestas de logs

#t(response.json())
# se coloca "import Data" para la creacion de usuario ,mas la parte de "def post_new_user" el resultado 201
# C:\Users\alex_\PycharmProjects\configuration.py\.venv\Scripts\python.exe C:\Users\alex_\PycharmProjects\configuration.py\sender_stand_request.py
# 201
# {'authToken': '549b6078-c0a0-4e52-8c4b-460a17ae1b2e'}
#
# Process finished with exit code 0
#def post_products_kits(products_ids):
    # Realiza una solicitud POST para buscar kits por productos.
   # return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH, # Concatenación de URL base y ruta.
                        #json=products_ids, # Datos a enviar en la solicitud.
                        # headers=data.headers) # Encabezados de solicitud.


#response = post_products_kits(data.product_ids);
#print(response.status_code)
#print(response.json()) # Muestra del resultado en la consola C:\Users\alex_\PycharmProjects\configuration.py\.venv\Scripts\python.exe C:\Users\alex_\PycharmProjects\configuration.py\sender_stand_request.py
#200
#[{'id': 1, 'name': 'Para pícnics', 'productsList': [{'id': 1, 'quantity': 1}, {'id': 2, 'quantity': 1}, {'id': 3, 'quantity': 1}, {'id': 4, 'quantity': 1}, {'id': 5, 'quantity': 1}, {'id': 6, 'quantity': 1}, {'id': 7, 'quantity': 1}, {'id': 8, 'quantity': 1}, {'id': 9, 'quantity': 1}, {'id': 10, 'quantity': 1}, {'id': 11, 'quantity': 1}, {'id': 12, 'quantity': 1}, {'id': 13, 'quantity': 1}, {'id': 14, 'quantity': 1}, {'id': 15, 'quantity': 1}, {'id': 16, 'quantity': 1}, {'id': 17, 'quantity': 1}, {'id': 18, 'quantity': 1}, {'id': 19, 'quantity': 1}, {'id': 20, 'quantity': 1}, {'id': 21, 'quantity': 1}, {'id': 22, 'quantity': 1}, {'id': 23, 'quantity': 1}, {'id': 24, 'quantity': 1}, {'id': 25, 'quantity': 1}, {'id': 26, 'quantity': 1}, {'id': 27, 'quantity': 1}, {'id': 28, 'quantity': 1}, {'id': 29, 'quantity': 1}, {'id': 30, 'quantity': 1}, {'id': 31, 'quantity': 1}, {'id': 32, 'quantity': 1}, {'id': 33, 'quantity': 1}, {'id': 34, 'quantity': 1}, {'id': 35, 'quantity': 1}, {'id': 36, 'quantity': 1}, {'id': 37, 'quantity': 1}, {'id': 38, 'quantity': 1}, {'id': 39, 'quantity': 1}], 'productsCount': 39}, {'id': 2, 'name': 'Para películas y series', 'productsList': [{'id': 7, 'quantity': 1}, {'id': 8, 'quantity': 1}, {'id': 9, 'quantity': 1}, {'id': 40, 'quantity': 1}, {'id': 41, 'quantity': 1}, {'id': 42, 'quantity': 1}, {'id': 43, 'quantity': 1}, {'id': 44, 'quantity': 1}, {'id': 45, 'quantity': 1}, {'id': 46, 'quantity': 1}, {'id': 47, 'quantity': 1}, {'id': 2, 'quantity': 1}, {'id': 3, 'quantity': 1}, {'id': 4, 'quantity': 1}, {'id': 48, 'quantity': 1}, {'id': 49, 'quantity': 1}, {'id': 50, 'quantity': 1}, {'id': 51, 'quantity': 1}, {'id': 52, 'quantity': 1}, {'id': 53, 'quantity': 1}, {'id': 54, 'quantity': 1}, {'id': 55, 'quantity': 1}, {'id': 56, 'quantity': 1}, {'id': 57, 'quantity': 1}, {'id': 58, 'quantity': 1}, {'id': 59, 'quantity': 1}, {'id': 60, 'quantity': 1}], 'productsCount': 27}]

#Process finished with exit code 0
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

#response = get_users_table(data.user_body);
#print(response.status_code)
#print(response.json())

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH,
                         headers=data.headers)
