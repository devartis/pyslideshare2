from pyslideshare import pyslideshare

# Have all the secure keys in a file called localsettings.py
try:
    from localsettings import username, password, api_key, secret_key, proxy
except:
    pass
    
obj = pyslideshare.pyslideshare(locals(), verbose=False)
json = obj.get_slideshow_by_group(group_name='friendfeed', limit=2)

if not json:
    import sys
    print >> sys.stderr, 'No response. Perhaps slideshare down?'
    sys.exit(1)

print 'Total slideshows by this group : ', json.Group.count
slideshows = json.Group.Slideshow
for show in slideshows:
    print 'Name : %s, Tags : %s' % (show.Title, show.Tags)
    
    