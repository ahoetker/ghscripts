#!/usr/bin/env bash
# pullscripts.sh - pull ghscripts repo and copy contents to scripts folder
# remember to add ssh keys as a first step!

repo=/home/andrew/ghscripts
scripts=/home/andrew/scripts
filetypes=(py sh)

cd $repo
git pull
for filetype in $filetypes;
do
    cp *.$filetype $scripts/
done
