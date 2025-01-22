# Utils tools

The get_machine_data.sh is used to fetch network data from the machines.
Results are stored in .txt files in the data directory.

The list of machines is taken from the ansible_data/hosts file, from the mywork2_all branch.

Once the script ran and data are in the data directory, you can use the data2ansible.py script to convert them in .yml files.

Then just copy those in the ansible mywork2_all repository.