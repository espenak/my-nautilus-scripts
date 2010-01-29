from os import path, environ, system, getcwd
import subprocess, urllib


def error(msg):
	subprocess.call(["zenity", "--error", "--text", msg])
	raise SystemExit()

def info(msg):
	subprocess.call(["zenity", "--info", "--text", msg])

def find_repo(d):
	while True:
		if path.exists(path.join(d, ".git")):
			return d
		if d == "/":
			return None
		d = path.dirname(d)

def get_dirname():
	curi = environ.get("NAUTILUS_SCRIPT_CURRENT_URI")
	if curi:
		curi = urllib.unquote(curi)
	else:
		curi = getcwd()
	dirname = path.normpath(curi.replace("file://", ""))
	return dirname

def get_shelldirname(d):
	return '"%s"' % d

def open_gitg(*args):
	repodir = find_repo(get_dirname())
	if not repodir:
		error("Not a git-repository.")
	args = " ".join(args)
	system("gitg %s %s" % (args, get_shelldirname(repodir)))

def open_stupidgit():
	repodir = find_repo(get_dirname())
	if not repodir:
		error("Not a git-repository.")
	system("stupidgit %s" % get_shelldirname(repodir))

def cmd(*command):
	args = " ".join(command)
	p = subprocess.Popen(args, executable="/bin/bash", shell=True,
		stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	stdout, stderr = p.communicate()
	out = stdout + "\n" + stderr
	return p.returncode, out

def cmd_failerror(*command):
	retcode, out = cmd(*command)
	if retcode != 0:
		error(" ".join(command) + ": " + out)
