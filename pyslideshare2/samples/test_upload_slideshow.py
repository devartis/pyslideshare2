from pyslideshare import pyslideshare

# Have all the secure keys in a file called localsettings.py
try:
    from localsettings import username, password, api_key, secret_key, proxy
except:
    pass

# Use proxy if available    
obj = pyslideshare.pyslideshare(locals(), verbose=False, proxy=proxy)
json = obj.upload_slideshow(username=username, password=password, slideshow_srcfile='test.ppt',
                               slideshow_title='pyslideshare works!')
if not json:
    import sys
    print >> sys.stderr, 'No response. Perhaps slideshare down?'
    sys.exit(1)
    
showId = json.SlideShowUploaded.SlideShowID
print 'Uploaded successfully. Id is %s.'%showId