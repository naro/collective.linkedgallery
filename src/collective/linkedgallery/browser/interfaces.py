from zope.interface import Interface

class IGalleryViewlet(Interface):
    """ """
    def images():
        """ return list of dicts with image data """
        
    def gallery_title():
        """ """

    def gallery_description():
        """ """

    def gallery_id():
        """ """

    def gallery_url():
        """ """

    def portal_url():
        """ Returns portal URL (as string) """