pyslideshare2
=============

Python wrapper for slideshre API v2

Forked from pyslideshare - http://code.google.com/p/pyslideshare/

Sample Usage
------------

    from pyslideshare2 import pyslideshare

    api_key = '' # Your api key
    secret_key = '' # Your secret key

    api = pyslideshare.pyslideshare(locals(), verbose=True)
    print api.get_slideshow(slideshow_id=436333)

Methods
-------

* get_slideshow_by_user
* get_slideshow
* get_slideshow_by_tag
* get_slideshow_by_group
* upload_slideshow
* delete_slideshow
* help(pyslideshare) should explain you the usage

Support
-------

Email me : german at devartis dot com

