server {
    listen ${LISTEN_PORT};

    location /media/ {
        alias /home/app/mediafiles/;
    }

    location /static/ {
        alias /home/app/staticfiles/;
    }

    location / {
        uwsgi_pass              ${APP_HOST}:${APP_PORT};
        include                 /etc/nginx/uwsgi_params;
        client_max_body_size    10M;
    }
}