#! /bin/sh
#
# start.sh
# Copyright (C) 2015 hzwangzhiwei
#
# Distributed under terms of the MIT license.
#


set -eu
python main.py &> /var/log/app.log &
touch /var/log/app.log
echo $! > /var/run/app.pid
tailf /var/log/app.log