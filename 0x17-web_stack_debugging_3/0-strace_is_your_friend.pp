# fix the typo in the wp-settings.php file

exec { 'replace phpp to php':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/usr/local/bin/:/bin/'
}
