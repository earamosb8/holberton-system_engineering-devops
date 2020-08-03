# this file create a new file with basic settings
file {'/tmp/holberton':
ensure  => 'file',
mode    => '0744',
owner   => 'www-data',
group   => 'www-data',
content => 'I love Puppet',
}
