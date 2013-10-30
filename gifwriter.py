import subprocess

class Error(Exception) :
	pass

def write_gif(files, fps, output_file) :
	# include +dither?
	# or +remap or -remap? read http://www.imagemagick.org/Usage/quantize/#remap_common
	cmd = ['convert', '-delay', '1x%d' % fps] + files + ['-coalesce', '-layers', 'OptimizeTransparency', output_file]
	if subprocess.call(cmd) != 0 :
		raise Error
