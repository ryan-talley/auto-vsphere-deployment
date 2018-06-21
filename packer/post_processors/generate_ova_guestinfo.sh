#!/bin/sh

dir=../packer/post_processors
cd ../../output-atomic-host7
tar -xvf atomic-host7.ova
rm ./atomic-host7.mf
rm ./atomic-host7.ova
python $dir/generate_ova_guestinfo.py ./atomic-host7.ovf $dir/atomic-host7-guestinfo.xml ./atomic-host7-edited.ovf
rm ./atomic-host7.ovf
tar -cvf ./atomic-host7.ova ./
cd $dir
