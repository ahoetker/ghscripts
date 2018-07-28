#!/usr/bin/env bash
# addgithubkeys.sh - add SSH keys and configure them for github
# Usage: addgithubkeys.sh [GITHUB_USERNAME]

cd ~/.ssh

# Create the ssh config file if it does not exist
sshconfig=~/.ssh/config
if [[ ! -e $sshconfig ]]; then
    touch $sshconfig
fi

# Generate SSH keys, this will prompt for a passphrase
ssh-keygen -t rsa -C "github-${1}" -f "github-${1}"

# Add this entry to the ssh config file
echo -e "Host github.com-${1}\n \
    \tHostName github.com\n \
    \tUser git\n \
    \tIdentityFile ~/.ssh/github-${1}\n" >> $sshconfig
