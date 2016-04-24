#!/bin/bash
cd ~/deluge/texttab
mkdir temp
export PYTHONPATH=./temp
/usr/bin/python setup.py build develop --install-dir ./temp
cp ./temp/textTab.egg-link ~/.config/deluge/plugins
rm -fr ./temp
