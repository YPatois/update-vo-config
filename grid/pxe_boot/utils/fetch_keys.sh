#!/bin/bash
#!/bin/bash
# Fetches and store existing SSH and Grid keys in the vault
# for reinstallation.
# Arguments:
#   Machine name

MC=$1

SCRIPTDIR=`dirname -- "$( readlink -f -- "$0"; )"`
BASEDIR=`dirname $SCRIPTDIR`

DESTDIR=$BASEDIR/vault/$MC

# For SSH
SSHKEYDIR=$DESTDIR/ssh
mkdir -p $SSHKEYDIR
rsync -av root@$MC:/etc/ssh/ssh_host_* $SSHKEYDIR/

# For grid certs
GRIDKEYDIR=$DESTDIR/grid
mkdir -p $GRIDKEYDIR
rsync -av root@$MC:/etc/grid-security/*.key root@$MC:/etc/grid-security/*.pem $GRIDKEYDIR/



