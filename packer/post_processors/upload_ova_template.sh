#!/bin/sh

source govc-vars.sh
govc vm.destroy atomic-host7
govc import.ova -options=./atomic-host7-options.json ../../output-atomic-host7/atomic-host7.ova
govc vm.markastemplate atomic-host7
