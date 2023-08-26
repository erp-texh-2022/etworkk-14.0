#!/bin/sh

set -e

etwork_CONFIGURATION_DIR=/etc/etwork
etwork_CONFIGURATION_FILE=$etwork_CONFIGURATION_DIR/etwork.conf
etwork_DATA_DIR=/var/lib/etwork
etwork_GROUP="etwork"
etwork_LOG_DIR=/var/log/etwork
etwork_LOG_FILE=$etwork_LOG_DIR/etwork-server.log
etwork_USER="etwork"
ABI=$(rpm -q --provides python3 | awk '/abi/ {print $NF}')

if ! getent passwd | grep -q "^etwork:"; then
    groupadd $etwork_GROUP
    adduser --system --no-create-home $etwork_USER -g $etwork_GROUP
fi
# Register "$etwork_USER" as a postgres user with "Create DB" role attribute
su - postgres -c "createuser -d -R -S $etwork_USER" 2> /dev/null || true
# Configuration file
mkdir -p $etwork_CONFIGURATION_DIR
# can't copy debian config-file as addons_path is not the same
if [ ! -f $etwork_CONFIGURATION_FILE ]
then
    echo "[options]
; This is the password that allows database operations:
; admin_passwd = admin
db_host = False
db_port = False
db_user = $etwork_USER
db_password = False
addons_path = /usr/lib/python${ABI}/site-packages/etwork/addons
" > $etwork_CONFIGURATION_FILE
    chown $etwork_USER:$etwork_GROUP $etwork_CONFIGURATION_FILE
    chmod 0640 $etwork_CONFIGURATION_FILE
fi
# Log
mkdir -p $etwork_LOG_DIR
chown $etwork_USER:$etwork_GROUP $etwork_LOG_DIR
chmod 0750 $etwork_LOG_DIR
# Data dir
mkdir -p $etwork_DATA_DIR
chown $etwork_USER:$etwork_GROUP $etwork_DATA_DIR

INIT_FILE=/lib/systemd/system/etwork.service
touch $INIT_FILE
chmod 0700 $INIT_FILE
cat << EOF > $INIT_FILE
[Unit]
Description=etwork Open Source ERP and CRM
After=network.target

[Service]
Type=simple
User=etwork
Group=etwork
ExecStart=/usr/bin/etwork --config $etwork_CONFIGURATION_FILE --logfile $etwork_LOG_FILE
KillMode=mixed

[Install]
WantedBy=multi-user.target
EOF
