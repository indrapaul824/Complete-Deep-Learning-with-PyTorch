# Arcane incantation to print all the other targets, from https://stackoverflow.com/a/26339924
help:
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

# Create conda environment with required Python version
conda-update:
	conda update -n base -c defaults conda -y
	conda env update --prune -f env.yml
# After activating environment
# Compile and install exact conda packages and required dependencies
reqs:
	conda install pytorch torchvision torchaudio cudatoolkit=11.1 -c pytorch -c nvidia -y
	pip-compile requirements.in
	pip-sync requirements.txt
	conda install ipykernel -y