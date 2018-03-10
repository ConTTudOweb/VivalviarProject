# Vivalviar Poker

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.6
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes.

```console
git clone https://github.com/ConTTudOweb/VivalviarProject.git
cd VivalviarProject
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```

## Util

Comando para desabilitar o collectstatic do heroku  
```console
heroku config:set DISABLE_COLLECTSTATIC=1
```

Site para pegar o ID dos videos da play list
[http://www.williamsportwebdeveloper.com/FavBackUp.aspx](http://www.williamsportwebdeveloper.com/FavBackUp.aspx)