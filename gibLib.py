# Python library file

# To parse command line arguments (simple + effective)
import argparse

# To use more collection type objects, rather than primitive types
import collections

# TO read config path
import configparser

# To use SHA-1 key functionality 
import hashlib

from math import ceil

# For path management importing os
import os

# For implementing and using regular expression
import re

# To access actual command line args and run some system commands
import sys

# For compression and optimized storage
import zlib

argParser = argparse.ArgumentParser(description="Creating a argument parser for git Commands")

# To handle subCommands such as GIT INIT, GIT ADD ... adding subParsers
argSubParser = argParser.add_subparsers(title="Git Commands",dest="command")
argSubParser.required = True
# The dest="command" argument states that the name of the chosen 
# subparser will be returned as a string in a field called command


# TO-DO add function definitions for following functions
def cmd_add(args): return None
def cmd_cat_file(args): return None
def cmd_checkout(args): return None
def cmd_commit(args): return None
def cmd_hash_object(args): return None
def cmd_init(args): return None
def cmd_log(args): return None
def cmd_ls_files(args): return None
def cmd_ls_tree(args): return None
def cmd_merge(args): return None
def cmd_rebase(args): return None
def cmd_rev_parse(args): return None
def cmd_rm(args): return None
def cmd_show_ref(args): return None
def cmd_tag(args): return None


def repo_path(repo, *path):
    return os.path.join(repo.gitDir, *path)


def repo_dir(repo, *path, mkdir=False):
    """
        Same as repo_path, but mkdir *path if absent 
    """

    path = repo_path(repo, *path)

    if os.path.exists(path):
        if (os.path.isdir(path)):
            return path
        else:
            raise Exception("Not a directory %s" % path)

    if mkdir:
        os.makedirs(path)
        return path
    else:
        return None


def repo_file(repo, *path, mkdir = False):
    """Same as repo_path, but create dirname(*path) if absent.
       For example, repo_file(r, \"refs\", \"remotes\", \"origin\", \"HEAD\") 
       will create
            .git/refs/remotes/origin.
    """

    if repo_dir(repo, *path[:-1], mkdir=mkdir):
        return repo_path(repo, *path)


def repo_create(path):
    """Create a new repository at path."""

    repo = GitRepository(path, True)

    # First, we make sure the path either doesn't exist or is an
    # empty dir.

    if os.path.exists(repo.worktree):
        if not os.path.isdir(repo.worktree):
            raise Exception ("Not a directory! :" + path)
        if os.listdir(repo.worktree):
            raise Exception("Not an empty Directory! :" % path)
    else:
        os.makedirs(repo.worktree)

    assert(repo_dir(repo, "branches", mkdir=True))
    assert(repo_dir(repo, "objects", mkdir=True))
    assert(repo_dir(repo, "refs", "tags", mkdir=True))
    assert(repo_dir(repo, "refs", "heads", mkdir=True))

    # .git/description
    with open(repo_file(repo, "description"), "w") as f:
        f.write("Unnamed repository: edit this file 'description' to name the repository.\n")

    # .git/HEAD
    with open(repo_file(repo, "HEAD"), "w") as f:
        f.write("ref: refs/heads/master\n")

    with open(repo_file(repo, "config"), "w") as f:
        config = repo_default_config()
        config.write(f)

    return repo

class GitRepository(object):
    """
        Git repository Class
    """

    workTree = None
    gitDir = None
    conf = None

    def __init__(self,path,force=False):

        # force = False means that the git repository exist
        # force = True => override and create a repository
        self.workTree = path
        self.gitDir = os.path.join(path,".git")

        if force and (os.path.isdir(self.gitDir) == False):
            raise Exception("Not a git repository" + path)

        # Read configuration file in .git/config
        self.conf = configparser.ConfigParser()
        cf = repo_file(self, "config")

        if cf and os.path.exists(cf):
            self.conf.read([cf])
        elif not force:
            raise Exception('Configuration file is missing on path: ' + cf)

        if not force:
            vers = int(self.conf.get("core","repositoryformatversion"))

            if vers != 0:
                raise Exception('Unsupported repositoryformatversion :'+ vers)
        


def main(argv=sys.argv[1:]):
    args = argParser.parse_args(argv)

    if   args.command == "add"         : cmd_add(args)
    elif args.command == "cat-file"    : cmd_cat_file(args)
    elif args.command == "checkout"    : cmd_checkout(args)
    elif args.command == "commit"      : cmd_commit(args)
    elif args.command == "hash-object" : cmd_hash_object(args)
    elif args.command == "init"        : cmd_init(args)
    elif args.command == "log"         : cmd_log(args)
    elif args.command == "ls-files"    : cmd_ls_files(args)
    elif args.command == "ls-tree"     : cmd_ls_tree(args)
    elif args.command == "merge"       : cmd_merge(args)
    elif args.command == "rebase"      : cmd_rebase(args)
    elif args.command == "rev-parse"   : cmd_rev_parse(args)
    elif args.command == "rm"          : cmd_rm(args)
    elif args.command == "show-ref"    : cmd_show_ref(args)
    elif args.command == "tag"         : cmd_tag(args)




