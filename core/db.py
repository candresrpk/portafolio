from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SQLITE = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }


# YOU WILL NEED TO INSTALL psycopg2 TO USE THIS DB CONFIGURATION
POSTGRES = {
    'ENGINE': 'django.db.backends.posgresql_psycopg2',
    'NAME': 'db',
    'USER':'root',
    'PASSWORD':'root',
    'HOST':'localhost',
    'PORT':'5432',
}