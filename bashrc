if [ -f ~/.bash_aliases ]
then
    . ~/.bash_aliases
fi

###############################
# Defaults
###############################
if [ -f ~/bin/sensible.bash ]; then
   source ~/bin/sensible.bash
fi

###############################
# Variables
###############################
PS1="[\u@\h \W]\$ "
PATH=$PATH:~/bin:
