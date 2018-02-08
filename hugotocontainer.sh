#!/bin/bash
# hugotocontainer.sh - pull from github, build, and move to container /www

# define locations
site_dir=$HOME/servotron.club
publish_dir=public
container_www=/$HOME/docker-server/dockerconfigs/letsencrypt/www

# pull site and build to publish_dir
cd $site_dir
git pull
hugo -D

# copy contents from publish_dir to container webroot
cp -r "$site_dir/$publish_dir/"* $container_www

# finished
echo "Done"
