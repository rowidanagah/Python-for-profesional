import argparse
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('-n',"--name", help ="parse a name val")

arg_parser.add_argument('-g' , '--greating', default ='Voala' , help ='This is something preserved in here')
arg_parser.add_argument('-p', '--plane', type=str, required=True,
                    choices=['sagittal', 'coronal', 'axial'])
                    
args = arg_parser.parse_args()
print("It works for {greating} and {name} !".format(
	greating =args.greating , name = args.name))
