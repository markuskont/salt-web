# vi: set ft=ruby :

MASTER_IP = '192.168.56.130'
# NOTE - building from git can take a lot of time and contain bugs
SALT = 'stable' # stable|git|daily|testing
# version to check out if using git
SALT_VERSION = "v2016.11.2"

boxes = [
  {
    :name       => "web-xenial",
    :mem        => "1024",
    :cpu        => "2",
    :ip         => "192.168.56.131",
    :image      => 'ubuntu/xenial64',
    :saltmaster => false,
    :provision     => [
      "./vagrant/scripts/apache.sh",
      "./vagrant/scripts/php7.sh"
    ]
  },
  {
    :name       => "web-jessie",
    :mem        => "1024",
    :cpu        => "2",
    :ip         => "192.168.56.132",
    :image      => 'debian/jessie64',
    :saltmaster => false,
    :provision     => [
      "./vagrant/scripts/apache.sh",
      "./vagrant/scripts/php5.sh"
    ]
  },
  {
    :name       => "db-jessie",
    :mem        => "1024",
    :cpu        => "2",
    :ip         => "192.168.56.133",
    :image      => 'debian/jessie64',
    :saltmaster => false,
    :provision     => [
      "./vagrant/scripts/postgre.sh",
    ]
  },
  {
    :name       => "saltmaster",
    :mem        => "512",
    :cpu        => "2",
    :ip         => MASTER_IP,
    :image      => "ubuntu/xenial64",
    :saltmaster => true
  }
]

Vagrant.configure(2) do |config|
  boxes.each do |opts|
    config.vm.define opts[:name] do |config|
      config.vm.box = opts[:image]
      config.vm.hostname = opts[:name]
      config.vm.network 'private_network',
        ip: opts[:ip]
      config.vm.provider "virtualbox" do |v|
        v.customize ["modifyvm", :id, "--memory", opts[:mem]]
        v.customize ["modifyvm", :id, "--cpus", opts[:cpu]]
      end
      config.vm.provision "shell",
        inline: "grep salt /etc/hosts || sudo echo \"#{MASTER_IP}\"  salt >> /etc/hosts"
      config.vm.provision :salt do |salt|
        salt.minion_config = "vagrant/config/minion"
        salt.masterless = false
        salt.run_highstate = false
        salt.install_type = SALT
        salt.install_master = opts[:saltmaster]
        if opts[:saltmaster] == true
          salt.master_config = "vagrant/config/master"
        end
      end
      config.vm.provision "shell", path: "./vagrant/scripts/assign_roles.py"
      if opts[:saltmaster] == false
        opts[:provision].each do |script|
          config.vm.provision "shell", path: script
        end
      end
    end
  end
end
