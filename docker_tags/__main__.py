#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""main entry of dtags"""
import sys

from . import get_tags


def main():
    if len(sys.argv) != 2:
        print('Invalid parameters!\nUsage: dtags repo_name')
        exit(-1)
    repo_name = sys.argv[1]
    try:
        tags = get_tags(repo_name)
        tag_list = [tag['name'] for tag in tags]
        tag_list = sorted(tag_list, reverse=True)
        print('\n'.join(tag_list))
    except Exception as e:
        print(repr(e))


if __name__ == '__main__':
    main()
