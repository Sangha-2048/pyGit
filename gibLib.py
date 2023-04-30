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




