# Piinfo_Backend


# Instalacion (ubuntu)


El primer paso necesario es intalar el entorno virtual
    
    python3 -m venv env

Esto generara el tercer directorio en la carpteta inicial: food_for_me, py_venv_back y venv

posteriormente acceder al entorno virutal generado

    source venv/bin/activate
  
Y finalmente instalar las dependencias

    python -m pip install -U pip
    pip install python-decouple
    pip install dj_rest_auth
    pip install djangorestframework
    python -m pip install django-allauth
    python -m pip install Pillow
    
    
# Ejecución server

Ubicado en el directorio raiz del git, junto a las 3 carpetas, ejecutar:

    python food_for_me/manage.py runserver
    
En caso contrario
    cd food_for_me
    python manage.py runserver


# Informacion extra

El git presenta algunos datos en la base de datos, estos se pueden acceder mediante la ruta

http://127.0.0.1:8000/core/app/propaganda/
http://127.0.0.1:8000/core/app/pymes/

donde todas las rutas configuradas en el documento core/urls.py se le debe anteponer "core/" para su funcionamiento
