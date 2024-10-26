#!/bin/bash

DOMAIN="hackathon-undefined.ru"
EMAIL="lyhtyrageorgiu@gmail.com"

if ! command -v certbot &> /dev/null; then
    echo "Certbot не найден. Попытка установить..."
    sudo apt-get update
    sudo apt-get install certbot -y
    echo "Установка Certbot завершена."
else
    echo "Certbot уже установлен."
fi

echo "Запуск Certbot для домена $DOMAIN в режиме standalone..."
sudo certbot certonly --standalone -d $DOMAIN --agree-tos -m $EMAIL --non-interactive

echo "Certbot завершил работу. Проверьте сертификаты в /etc/letsencrypt/live/$DOMAIN/"