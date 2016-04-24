#!/bin/bash
cd /media/sdf1/home/fh8123789/deluge/texttab
mkdir temp
export PYTHONPATH=./temp
/usr/bin/python setup.py build develop --install-dir ./temp
cp ./temp/textTab.egg-link /media/sdf1/home/fh8123789/.config/deluge/plugins
rm -fr ./temp
