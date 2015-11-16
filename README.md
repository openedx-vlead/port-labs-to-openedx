# Installing Open edX Fullstack

###Step 1:Install Software Prerequisites
	
	1. VirtualBox 4.3.12 or higher
    	2. Vagrant 1.6.5 or higher
   	3. A Network File System (NFS) client, if your operating system does not include one. 
		* Fullstack uses VirtualBox Guest Editions 		to share folders through NFS.
		* setup NFS from this link https://help.ubuntu.com/community/SettingUpNFSHowTo
###Step 2: Install Open edX Fullstack
	1. Ensure the nfsd client is running.
	2. Create the fullstack directory and navigate to it in the command prompt.
		* mkdir fullstack
		* cd fullstack
	3.Download the fullstack Vagrant file.
		*curl -L https://raw.githubusercontent.com/edx/configuration/master/vagrant/release/fullstack/Vagrantfile > Vagrantfile
	4.Install the Vagrant hostsupdater plugin.
		*vagrant plugin install vagrant-hostsupdater
	5.Create the Fullstack virtual machine.
		*vagrant up
	6.When prompted, enter the administrator password for your local computer.



