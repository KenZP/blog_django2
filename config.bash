killall -9 nginx
/usr/sbin/nginx
killall -9 uwsgi
uwsgi conf/uwsgi.ini -d conf/uwsgi.log
#killall -9 memcached
#memcached -d -m 128 -l 127.0.0.1 -p 11211 -u root
