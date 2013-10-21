import subprocess

class Error(Exception) :
	pass

def write_gif(files, fps, output_file) :
	cmd = ['convert', '-delay', '1x%d' % fps] + files + ['-coalesce', '-layers', 'OptimizeTransparency', output_file]
	if subprocess.call(cmd) != 0 :
		raise Error
