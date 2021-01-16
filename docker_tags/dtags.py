# -*- coding:utf-8 -*-
"""To list tags of a docker repo

Get from https://registry.hub.docker.com/v1/repositories/{repo}/tags

..
 @author XieY.J.
 Created on 2021.01.16

"""
import requests


def get_tags(repo_name):
    """
    Get docker tags from https://registry.hub.docker.com/v1/repositories/{repo}/tags

    Parameters
    ----------
    repo_name : str
        repo name

    Returns
    -------
    list of str
        tags list
    """
    url_ = 'https://registry.hub.docker.com/v1/repositories/{repo}/tags'

    resp = requests.get(url_.format(repo=repo_name))
    if resp.status_code != 200:
        raise RuntimeError('Gotten HTTP code {}.'.format(str(resp.status_code)))
    reso = resp.json()
    if not isinstance(reso, list):
        raise RuntimeError('Invalid result:\n{}'.format(resp.text))
    return reso


if __name__ == '__main__':
    pass
