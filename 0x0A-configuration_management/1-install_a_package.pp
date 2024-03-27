exec { 'install_flask':
  command     => 'pip3 install Flask==2.1.0',
  path        => ['/bin', '/usr/bin'],
  environment => ['PATH=/usr/local/bin:/usr/bin:/bin'],
  unless      => 'pip3 show Flask | grep -q "Version: 2.1.0"',
}

