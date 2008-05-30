from pyslideshare import pyslideshare

# Have all the secure keys in a file called localsettings.py
try:
    from localsettings import username, password, api_key, secret_key, proxy
except:
    pass
    
obj = pyslideshare.pyslideshare(locals(), verbose=True)
json = obj.get_slideshow_by_tag(tag='java', limit='5')

if not json:
    import sys
    print >> sys.stderr, 'No response. Perhaps slideshare down?'
    sys.exit(1)
    
print 'Total slideshows for this Tag : ', json.Tag.count
slideshows = json.Tag.Slideshow
for show in slideshows:
    print 'Name : %s, Views : %s' % (show.Title, show.Views)
    
    