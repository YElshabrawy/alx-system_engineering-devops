# Increase hard file limit for Holberton user
exec { 'increase-hard-file-limit-for-holberton-user':
  command => 'sed -i "/holberton hard/s/5/4096/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

# Increase soft file limit for Holberton user.
exec { 'increase-soft-file-limit-for-holberton-user':
  command => 'sed -i "/holberton soft/s/4/4096/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
