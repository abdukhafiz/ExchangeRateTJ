server {
    listen ${LISTEN_PORT};

    location /static {
        alias /vol/static;
    }

    location / {
        uwsgi_pass              ${APP_HOST}:${APP_PORT};
        include                 /etc/nginx/uwsgi_params;
        client_max_body_size    10M;
    }

    access_log /var/log/nginx/ExchangerTJ.com-access.log main;
    error_log /var/log/nginx/ExchangerTJ.com-error.log error;
}