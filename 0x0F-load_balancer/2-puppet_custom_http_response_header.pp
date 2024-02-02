# custom
exec {'command':
  command => "sudo apt-get update;
              sudo apt-get install -y nginx;
              sudo sed -i '/server_name _;/a \        add_header X-Served-By $hostname;' /etc/nginx/sites-available/default;
              /etc/init.d/nginx restart",
  provider => shell,
}
