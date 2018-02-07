#!/bin/bash
# hugotocontainer.sh - pull from github, build, and move to container /www

site_dir=$HOME/servotron.club
cd $site_dir
hugo server -D
