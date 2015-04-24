#!/bin/bash

################################################################
# Filename: init.sh
# Location: /Users/Atom/Temp
# Project : 
# Date    : 2014-12-13
# User    : Atom
# Scope   : 
################################################################

################################################################
# Constants
################################################################

FILE_NAME=`basename $0`

BASH_RCODE_FAILURE=1
BASH_RCODE_SUCCESS=0

FUNCTION_RCODE_FAILURE=0
FUNCTION_RCODE_SUCCESS=1

################################################################
# Functions
################################################################

###############################
# Superuser: Check
superuser_check() {

    FUNCTION_NAME="superuser_check"
    LOG_PREFIX=${FILE_NAME}": "${FUNCTION_NAME}": "
    
    if [ `id -u` -eq 0 ]; then
        return ${FUNCTION_RCODE_SUCCESS}
    else
        echo "error: init.sh, not a superuser, exiting"
        exit ${BASH_RCODE_FAILURE}
    fi
}

###############################
# Git: Install
git_install() {

    apt-get install -y git
    return $?
}

###############################
# Git: Remove
git_purge() {
    apt-get purge -y git
    return $?
}

###############################
# Git: Status
git_status() {

    dpkg -s git
    return $?
}

case "$1" in
  install)
    superuser_check
    git_install
    exit $?
    ;;
    
  remove)
    superuser_check
    git_purge
    echo $?
    ;;
    
  status)
    git_status
    exit $?
    ;;

  *)
    echo "Usage: init.sh {install|remove|status}"
    exit ${BASH_RCODE_FAILURE}
esac
