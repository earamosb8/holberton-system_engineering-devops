# change the Os configuration.
exec { '/usr/bin/env sed -i "s/holberton/foo/" /etc/security/limits.conf': }
