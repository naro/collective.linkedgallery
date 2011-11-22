from zope.interface import implements
from zope.component import adapts, getUtility
from archetypes.schemaextender.interfaces import IBrowserLayerAwareExtender
from archetypes.schemaextender.field import ExtensionField
from Products.Archetypes.atapi import ReferenceField, AnnotationStorage
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget

from collective.linkedgallery.interfaces import ILinkedGallerySpecific
from collective.linkedgallery.interfaces import ILinkedGalleryAware
from collective.linkedgallery import linkedGalleryMessageFactory as _

class ExtReferenceField(ExtensionField, ReferenceField):
    """ just a field """

class LinkedGalleryExtender(object):
    adapts(ILinkedGalleryAware)
    implements(IBrowserLayerAwareExtender)

    layer = ILinkedGallerySpecific

    fields = [
        ExtReferenceField(
            name='linkedGallery',
            required = False,
            storage = AnnotationStorage(),
            languageIndependent = True,
            multiValued=False,
            relationship='isGalleryOf',
            keepReferencesOnCopy = True,
            allowed_types=('Folder',),
            widget = ReferenceBrowserWidget(
                           label=_(u"Gallery"),
                           description=_(u"Select folder with images. These images will be displayed under the body as gallery." ),
                           force_close_on_insert=1,
                           hide_inaccessible=True,
                 ),
        ),            
    ]
    
    def __init__(self, context):
        self.context = context
        
    def getFields(self):
        return self.fields