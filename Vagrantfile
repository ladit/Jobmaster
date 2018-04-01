# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.box_check_update = false
  config.vm.hostname = "ubuntu"
  
  config.ssh.keep_alive = true

  # port mapping
  config.vm.network "forwarded_port", guest: 80, host: 8080
  config.vm.network "forwarded_port", guest: 3306, host: 33060

  # Create a private network, which allows host-only access to the machine using a specific IP.
  config.vm.network "private_network", ip: "192.168.10.10"

  # Project folder synchronize using bindfs
  config.vm.synced_folder ".", "/home/vagrant/jobmaster"
  config.bindfs.bind_folder "/home/vagrant/jobmaster", "/home/vagrant/jobmaster"
end
