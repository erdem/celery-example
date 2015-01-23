# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
    config.vm.box = "blogto"
    config.vm.box_url = "http://files.vagrantup.com/precise64.box"

    config.vm.network :forwarded_port, guest: 80, host: 8080
    config.vm.network :forwarded_port, guest: 8080, host: 8081
    config.vm.network :forwarded_port, guest: 83, host: 8083
    config.vm.network :private_network, ip: "33.33.33.10"
    config.vm.synced_folder ".", "/celery_example", :nfs => true

    config.vm.provider :virtualbox do |vb|
        vb.customize ["modifyvm", :id, "--memory", "1024"]
        vb.customize ["modifyvm", :id, "--rtcuseutc", "on"]
    end



end
