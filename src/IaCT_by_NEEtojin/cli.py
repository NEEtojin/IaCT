import os
import argparse

def main():

	parser = argparse.ArgumentParser(description = "IaCT!!!")

	parser.add_argument("-i", "--input", type = str, nargs = 1,
	metavar = "input file type", default = "cf_template", 
	help = "specify input file type. available options are cf_template (default, for AWS), arm_template (for Azure), cdm_template (for GCP)")

	parser.add_argument("-e", "--extension", type = str, nargs = 1,
	metavar = "input file extension", default = "json",
	help = "specify input file extension. available options are json, yaml, template(?)")

	args = parser.parse_args()

	return 0
	
if __name__ == "__main__":
	main()
