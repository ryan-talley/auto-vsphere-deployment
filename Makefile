.PHONY: ova clean

ova:
	packer build ./packer/atomic-host7-packer.json
	cd ./terraform; terraform init; terraform apply -auto-approve

clean:
	rm -rf ./output-atomic-host7
	cd ./terraform; terraform destroy -auto-approve
	govc vm.destroy atomic-host7
