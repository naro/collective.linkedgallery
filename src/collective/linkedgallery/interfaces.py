from zope.interface import Interface
from plone.theme.interfaces import IDefaultPloneLayer

class ILinkedGallerySpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer.
    """
    
class ILinkedGalleryAware(Interface):
    """ Marker interface for linked gallery aware types (IATDocument by
        default) 
    """