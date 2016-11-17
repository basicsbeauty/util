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
        echo "===================================="
        printf "Setting up %-16s .vimrc \n"
        echo "===================================="
        source_file="vimrc"
        target_file="$HOME/.vimrc"
        if [ ! -f "$target_file" ]
        then
            cmd="cp "$source_file" "$target_file
            printf "\t Command    : $cmd \n"
            eval $cmd
        else
            printf "\t Skipping\n"
        fi

    # BASH Aliases
        echo "===================================="
        printf "Setting up %-16s .bash_aliases \n"
        echo "===================================="
        source_file="bash_aliases"
        target_file="$HOME/.bash_aliases"
        #printf "\t Target file: $target_file \n"
        if [ ! -f $target_file ]
        then
            cmd="cp "$source_file" "$target_file
            printf "\t Command    : $cmd \n"
            eval $cmd
        else
            printf "\t Skipping\n"
        fi

    # BASH Environment
        echo "===================================="
        printf "Setting up %-16s .bashrc \n"
        echo "===================================="
        source_file="bashrc"
        target_file="$HOME/.bashrc"
        #printf "\t Target file: $target_file \n"
        if [ ! -f $target_file ]
        then
            cmd="cp "$source_file" "$target_file
            printf "\t Command    : $cmd \n"
            eval $cmd
        else
            printf "\t Skipping\n"
        fi

    # BASH: Sensible
        # cmd="cp sensible.bash ~/bin/"
	eval $cmd

###############################
# Directories
###############################

    # { temp, learn, backup}
        mkdir $HOME/temp $HOME/learn $HOME/backup $HOME/bin

    # $HOME/bin
        echo "===================================="
        printf "Setting up %-16s directory, $HOME/bin \n"
        target_directory="$HOME/bin"
        echo "===================================="
        if [ ! -e $target_directory ]
        then
            cmd="mkdir "$target_directory
            printf "\t Command    : $cmd \n"
            eval ${cmd}
        fi

        # Copy files
        printf "Setting up %-16s directory, $HOME/bin copying files\n"

        # mkdirpy & mkdirpy.sh
            cmd="cp mkdirpy.sh $HOME/bin"
	    echo "Cmd: ", $cmd
            eval ${cmd}

            cmd="cp --no-dereference mkdirpy $HOME/bin"
            cmd="cp mkdirpy $HOME/bin"
            eval ${cmd}

        # touchf & touchf.py
            cmd="cp touchf.py $HOME/bin"
	    echo "Cmd: ", $cmd
            eval ${cmd}

            cmd="cp --no-dereference touchf $HOME/bin"
            cmd="cp touchf $HOME/bin"
	    echo "Cmd: ", $cmd
            eval ${cmd}

        # createp & create.py
            cmd="cp project_create.py $HOME/bin"
	    echo "Cmd: ", $cmd
            eval ${cmd}

            cmd="cp --no-dereference createp $HOME/bin"
            cmd="cp createp $HOME/bin"
	    echo "Cmd: ", $cmd
            eval ${cmd}

        # backup & backup.sh
            cmd="cp backup.sh $HOME/bin"
	    echo "Cmd: ", $cmd
            eval ${cmd}

            cmd="cp --no-dereference backup $HOME/bin"
            cmd="cp backup $HOME/bin"
	    echo "Cmd: ", $cmd
            eval ${cmd}

###############################
# Directories & Files
###############################

    # Dirctories { quick, quick/cpp, quick/python}
        mkdir --parents $HOME/quick/cpp
        mkdir --parents $HOME/quick/python

    # File { z.cpp}
        cmd="cp --no-dereference z.cpp $HOME/quick/cpp"
        cmd="cp z.cpp $HOME/quick/cpp"
        eval ${cmd}

    # File { x.py}
        cmd="cp --no-dereference x.py $HOME/quick/python"
        cmd="cp x.py $HOME/quick/python"
        eval ${cmd}
