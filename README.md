# PC Creator

## Creación del Backend con Django
 Creación del **entorno virtual** en Cmd de Windows: 

    python -m venv myvenv
Activación del **virtualenv**:

    myvenv\Scripts\activate
Verificar que aparece el (myvenv) en linea de terminal

**Instalación de Django:**

    py -m pip install Django
Para comprobar que se instalo correctamente:

    py -m pip freeze
**Creación del proyecto:**

    django-admin startproject nombre
**Correr el servidor de Django**
Ingresamos a la carpeta del proyecto desde la terminal:

    py manage.py runserver

## Creación del Frontend con Angular
Creación del proyecto en terminal:

    ng new nombre
**Correr el servidor de Angular**
Ingresamos a la carpeta del proyecto desde la terminal:

    ng s -o

## En Back-end
En Terminal con el *virtualenv* activado instalamos:

    py -m pip install djangorestframework

Consultar la documentación [aqui](https://www.django-rest-framework.org/tutorial/quickstart/)

Ahora hacemos la primera migración a la base de datos:

    python manage.py migrate
Creamos un super usuario para el administrador:

    python manage.py createsuperuser
Creación de la aplicación **API**:

    django-admin startapp api
 Ahora en **settings. py** agregamos la aplicación **api**:

     INSTALLED_APPS = [ 'api' ]
**Instalación de django-cors-headers**:

    py -m pip install django-cors-headers
Consultar documentación [aqui](https://github.com/adamchainz/django-cors-headers)

En archivo **settings** agregar lo siguiente:

    INSTALLED_APPS = [ 'corsheaders', ]
    MIDDLEWARE = [ 
    	'corsheaders.middleware.CorsMiddleware',
        'django.middleware.common.CommonMiddleware',
     ]
**Para Probar que todo este funcionando**
Instalamos la **httpie**:

    py -m pip install httpie
Ahora teniendo el servidor de django corriendo ejecutamos:

    http -a admin:password123 http://127.0.0.1:8000/pcs/

**Autenticación con JWT (JSON Web Token)** 
Instalación de djangorestframework-simplejwt:

    py -m pip install djangorestframework-simplejwt

Consultar documentación [aqui](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html) 

## En Front-end
Autenticación de angular con JWT [Consultar](https://bezkoder.com/angular-jwt-authentication/#Login_Component)
