# Puppet manifest to optimize Nginx configuration

# Define a class for managing Nginx configurations
class nginx_config {

  # Resource to manage the Nginx configuration file
  file { '/etc/nginx/nginx.conf':
    ensure  => file,
    owner   => 'root',
    group   => 'root',
    mode    => '0644',
    content => template('/home/joyce/alx-system_engineering-devops/0x1B-web_stack_debugging_4/templates/nginx.conf.erb'), # Use a template file for Nginx configuration
    notify  => Service['nginx'], # Notify the Nginx service to reload when the config changes
  }

  # Resource to manage the Nginx service
  service { 'nginx':
    ensure    => running, # Ensure the service is running
    enable    => true,    # Enable the service to start on boot
    hasstatus => true,    # Check the status of the service
    hasrestart => true,   # Restart the service if needed
  }
}

# Include the nginx_config class to apply the configuration
include nginx_config

