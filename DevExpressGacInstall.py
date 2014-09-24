__author__ = "Joseph Gunawan"

import sys, string, argparse, os, subprocess as sub

def main(argv):
	parser = argparse.ArgumentParser(description='Install or Uninstall DevExpress dlls into GAC')
	parser.add_argument('-d', '--directory', help='Directory where DevExpress dlls located')
	parser.add_argument('-i', '--install', help='"True" to install DevExpress dlls into GAC. "False" to uninstall DevExpress dlls from GAC')
	args = parser.parse_args()
	
	if args.directory == None:
		print("Please specify directory using -d flag.")
		sys.exit()
		
	if args.install == None:
		print("Please specify whether you want to install or uninstall DevExpress dlls using -i flag.")
		sys.exit()

	print()
	print("DevExpress directory:", args.directory)
	
	if (args.install == "True"):
		print("Installing the following dlls below into the GAC:")
		for dll in get_list_of_DevExpress_dlls(args.directory):
			dllPath = args.directory + "\\" + dll
			sub.call([r"C:\Program Files (x86)\Microsoft SDKs\Windows\v8.0A\bin\NETFX 4.0 Tools\gacutil.exe", "/i", dllPath])
		sys.exit()
	elif (args.install == "False"):
		print("Uninstalling the following dlls below from the GAC:")
		for dll in get_list_of_DevExpress_dlls(args.directory):
			dllName = dll.replace(".dll", "")
			sub.call([r"C:\Program Files (x86)\Microsoft SDKs\Windows\v8.0A\bin\NETFX 4.0 Tools\gacutil.exe", "/u", dllName])
		sys.exit()

def get_list_of_DevExpress_dlls(directory, list_of_DevEx_dlls=[]):
	files_in_dir = os.listdir(directory)
	for file_in_dir in files_in_dir:
		if (file_in_dir.startswith("DevExpress")):
			list_of_DevEx_dlls.append(file_in_dir)
	return list_of_DevEx_dlls
	
if __name__ == "__main__":
	main(sys.argv[1:])

