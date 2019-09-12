#！/bin/sh
sudo killall -9 memcached
memcached -d -m 128 -l 127.0.0.1 -p 11211 -u root

