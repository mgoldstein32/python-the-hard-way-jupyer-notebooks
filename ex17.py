from sys import argv;script, from_file, to_file = argv;in_file = open(from_file, 'r');indata = in_file.read();out_file = open(to_file, 'w');out_file.write(indata);out_file.close();in_file.close()
