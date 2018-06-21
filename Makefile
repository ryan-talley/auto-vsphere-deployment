.PHONY: ova

ova:
	packer build ./packer/atomic-host7-packer.json
	cd ./terraform; terraform init; terraform apply -auto-approve
	rm -r ./output-atomic-host7
