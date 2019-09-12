#！/bin/sh
sudo killall -9 uwsgi
uwsgi conf/uwsgi.ini -d conf/uwsgi.log
