Instale o python pelo site oficial:
https://www.python.org/ftp/python/3.8.1/python-3.8.1.exe
-No instalador, marque a caixa de adicionar ao PATH no começo do instalador

Caso não tenha a aplicação de criação de ambientes virtuais, execute:
$ pip install virtualenv

Crie um ambiente virtual com o comando:
$ virtualenv env

Acesse a pasta Scripts dentro da pasta env e ative o ambiente:
$ cd env/Scripts
$ activate

Instale os frameworks necessários para a execução do projeto:
$ pip install django
$ pip install django-bootstrap-form

Acesse a pasta do projeto e execute os códigos:
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver