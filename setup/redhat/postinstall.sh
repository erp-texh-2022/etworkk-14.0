#!/bin/sh

set -e

DOSYT_CONFIGURATION_DIR=/etc/etwork
DOSYT_CONFIGURATION_FILE=$DOSYT_CONFIGURATION_DIR/etwork.conf
DOSYT_DATA_DIR=/var/lib/etwork
DOSYT_GROUP="etwork"
DOSYT_LOG_DIR=/var/log/etwork
DOSYT_LOG_FILE=$DOSYT_LOG_DIR/etwork-server.log
DOSYT_USER="etwork"
ABI=$(rpm -q --provides python3 | awk '/abi/ {print $NF}')

if ! getent passwd | grep -q "^etwork:"; then
    groupadd $DOSYT_GROUP
    adduser --system --no-create-home $DOSYT_USER -g $DOSYT_GROUP
fi
# Register "$DOSYT_USER" as a postgres user with "Create DB" role attribute
su - postgres -c "createuser -d -R -S $DOSYT_USER" 2> /dev/null || true
# Configuration file
mkdir -p $DOSYT_CONFIGURATION_DIR
# can't copy debian config-file as addons_path is not the same
if [ ! -f $DOSYT_CONFIGURATION_FILE ]
then
    echo "[options]
; This is the password that allows database operations:
; admin_passwd = admin
db_host = False
db_port = False
db_user = $DOSYT_USER
db_password = False
addons_path = /usr/lib/python${ABI}/site-packages/etwork/addons
" > $DOSYT_CONFIGURATION_FILE
    chown $DOSYT_USER:$DOSYT_GROUP $DOSYT_CONFIGURATION_FILE
    chmod 0640 $DOSYT_CONFIGURATION_FILE
fi
# Log
mkdir -p $DOSYT_LOG_DIR
chown $DOSYT_USER:$DOSYT_GROUP $DOSYT_LOG_DIR
chmod 0750 $DOSYT_LOG_DIR
# Data dir
mkdir -p $DOSYT_DATA_DIR
chown $DOSYT_USER:$DOSYT_GROUP $DOSYT_DATA_DIR

INIT_FILE=/lib/systemd/system/etwork.service
touch $INIT_FILE
chmod 0700 $INIT_FILE
cat << EOF > $INIT_FILE
[Unit]
Description=Dosyt Open Source ERP and CRM
After=network.target

[Service]
Type=simple
User=etwork
Group=etwork
ExecStart=/usr/bin/etwork --config $DOSYT_CONFIGURATION_FILE --logfile $DOSYT_LOG_FILE
KillMode=mixed

[Install]
WantedBy=multi-user.target
EOF
