#!/bin/bash

################################################################
# Filename: uninstall.sh
# Location: /home/ssatish/repos/util
# Project : 
# Date    : 2015-05-24
# User    : ssatish
# Scope   : 
################################################################

# Files
    cmd="rm ~/.vimrc ~/.bash_aliases ~/.bashrc"
    eval ${cmd}

# Directories
    cmd="rm -rf ~/bin ~/temp ~/learn ~/quick ~/backup"
    eval ${cmd}
