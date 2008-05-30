from pyslideshare import pyslideshare

# Have all the secure keys in a file called localsettings.py
try:
    from localsettings import username, password, api_key, secret_key, proxy
except:
    pass
    
obj = pyslideshare.pyslideshare(locals(), verbose=False)
json = obj.get_slideshow_by_user(username_for='desistartups')

if not json:
    import sys
    print >> sys.stderr, 'No response. Perhaps slideshare down?'
    sys.exit(1)
    
print 'Total slideshows by this user : ', json.User.count
slideshows = json.User.Slideshow
for show in slideshows:
    print 'Name : %s, Views : %s' % (show.Title, show.Views)
    
    