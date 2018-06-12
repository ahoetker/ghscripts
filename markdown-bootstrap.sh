#!/usr/bin/env bash
# markdown-bootstrap.sh - make bootstrap HTML from markdown
# USAGE: pandoc [MARKDOWN SRC] [HTML DST]

htmltemplate=~/Nextcloud/Documents/pandoc-bootstrap-template/template.html
csstemplate=~/Nextcloud/Documents/pandoc-bootstrap-template/template.css

pandoc ${1} -o ${2} --template $htmltemplate --css $csstemplate --self-contained --toc --toc-depth 2
