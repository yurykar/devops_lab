#!/bin/bash

sudo yum install -y zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel xz xz-devel
curl -L https://raw.github.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
sudo echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> $HOME/.bash_profile
sudo echo 'eval "$(pyenv init -)"' >> $HOME/.bash_profile
sudo echo 'eval "$(pyenv virtualenv-init -)"' >> $HOME/.bash_profile
source $HOME/.bash_profile
pyenv install 2.7.14
pyenv global 2.7.14
pyenv virtualenv 1st
pyenv deactivate
pyenv install 3.5.4
pyenv global 3.5.4
pyenv virtualenv 2st

