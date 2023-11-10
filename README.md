# Computer Engineering Application Project


## Validity identifier system for different identity documents.

### Branch : Main

## APP
> pip install Pillow

> pip install opencv-python

> pip install pytesseract

> pip install python-dotenv

> pip install tensorflow

> pip install pymongo

### Create .env
Create a .envc file with the following variables:
```
uri = "mongo_url"
host = '123.123.123.123'  # Reemplaza con la IP de tu Raspberry Pi
port = '12345'
```
How to run:
From the root directory enter the following line:
```
python .\windows.py
```


## Server

> python3 -m venv .venv

> source .venv/bin/active

> pip3 install opencv-python

> pip3 install requests

How to run:
From the root directory enter the following line:
```
python .\client\server.py
```