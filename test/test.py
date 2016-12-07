from dota2crawler.config import DOTA2_URL
from dota2crawler.utils.utils import print_error
from dota2crawler.__main__ import get_info, get_one, get_response
from nose import with_setup
import os


save_dir = os.path.abspath('./pictest')


def setup():
    if os.path.exists(save_dir):
        if not os.path.isdir(save_dir):
            print_error('pic exists as a file, specify directory')
            assert 0
    else:
        os.mkdir(save_dir)


@with_setup(setup)
def test():
    response = get_response(DOTA2_URL)
    soup, _ = get_info(response)
    get_one(soup, save_dir)
