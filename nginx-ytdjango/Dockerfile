FROM nginx
WORKDIR /etc/nginx
RUN rm /etc/nginx/conf.d/default.conf
COPY ytdjango.conf /etc/nginx/conf.d/
expose 80