#!/bin/bash

################################################################
# Filename: install.sh
# Location: /home/ssatish/repos/util
# Project : Util
# Date    : 2015-05-24
# User    : ssatish
# Scope   : 
################################################################

###############################
# Files: Individual
###############################
    # Vim Environment
        printf "Setting up %-16s .vimrc \n"
        source_file="vimrc"
        target_file="~/.vimrc"
        #printf "\t Target file: $target_file \n"
        if [ -f $target_file ]
        then
            cmd="cat "$source_file" >> "$target_file
        else
            cmd="cp "$source_file" "$target_file
        fi
        printf "\t Command    : $cmd \n"
        eval $cmd

    # BASH Aliases
        printf "Setting up %-16s .bash_aliases \n"
        source_file="bash_aliases"
        target_file="~/.bash_aliases"
        #printf "\t Target file: $target_file \n"
        if [ -f $target_file ]
        then
            cmd="cat "$source_file" >> "$target_file
        else
            cmd="cp "$source_file" "$target_file
        fi
        printf "\t Command    : $cmd \n"
        eval $cmd

    # BASH Environment
        printf "Setting up %-16s .bashrc \n"
        source_file="bashrc"
        target_file="~/.bashrc"
        #printf "\t Target file: $target_file \n"
        if [ -f $target_file ]
        then
            cmd="cat "$source_file" >> "$target_file
        else
            cmd="cp "$source_file" "$target_file
        fi
        printf "\t Command    : $cmd \n"
        eval $cmd

###############################
# Directories
###############################

    # { temp, learn, backup}
        mkdir ~/temp ~/learn ~/backup        

    # ~/bin
        printf "Setting up %-16s directory, ~/bin \n"
        target_directory="~/bin"
        if [ ! -e $target_directory ]
        then
            cmd="mkdir "$target_directory
            printf "\t Command    : $cmd \n"
            eval ${cmd}
        fi

        # Copy files
        printf "Setting up %-16s directory, ~/bin copying files\n"

        # touchf & touchf.py
            cmd="cp touchf.py ~/bin"
            eval ${cmd}

            cmd="cp --no-dereference touchf ~/bin"
            eval ${cmd}

        # createp & create.py
            cmd="cp project_create.py ~/bin"
            eval ${cmd}

            cmd="cp --no-dereference createp ~/bin"
            eval ${cmd}

        # backup & backup.sh
            cmd="cp backup.sh ~/bin"
            eval ${cmd}

            cmd="cp --no-dereference backup ~/bin"
            eval ${cmd}

###############################
# Directories & Files
###############################

    # Dirctories { quick, quick/cpp, quick/python}
        mkdir --parents ~/quick/cpp
        mkdir --parents ~/quick/python
        
    # File { z.cpp}
        cmd="cp --no-dereference z.cpp ~/quick/cpp"
        eval ${cmd}

    # File { x.py}
        cmd="cp --no-dereference x.py ~/quick/python"
        eval ${cmd}
        