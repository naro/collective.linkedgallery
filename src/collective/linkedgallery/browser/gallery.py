from Acquisition import aq_inner
from zope.interface import implements
from zope.component import getMultiAdapter, getUtility, queryAdapter
from plone.memoize import view
from random import shuffle

from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.interfaces import IPloneSiteRoot
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from collective.linkedgallery.browser.interfaces import IGalleryViewlet

class GalleryViewlet(ViewletBase):
    implements(IGalleryViewlet)
    index = ViewPageTemplateFile('gallery.pt')

    _images = []
    _gallery = None
    showClickToEnlarge = True
    
    def render(self):
        return self.index()

    def images(self):
        return self._images

    def gallery_title(self):
        if self._gallery is not None:
            return self._gallery.Title()
        else:
            return ''

    def gallery_description(self):
        if self._gallery is not None:
            return self._gallery.Description()
        else:
            return ''

    def gallery_id(self):
        if self._gallery is not None:
            return self._gallery.getId()
        else:
            return ''

    def gallery_url(self):
        context = aq_inner(self.context)
        field = context.getField('linkedGallery')
        if field is not None:
            gallery = field.get(context)
            if gallery:
                return gallery.absolute_url()
        return ''

    def portal_url(self):
        return getUtility(IPloneSiteRoot).absolute_url()

    def update(self):
        super(GalleryViewlet, self).update()
        context = aq_inner(self.context)
        result = []
        gallery = None
        field = context.getField('linkedGallery')
        if field is not None:
            gallery = field.get(context)
            if gallery:
                ptool = getToolByName(context, 'portal_properties')
                props = ptool.linkedgallery_properties
                # props - random, numberOfPhotos, showLinkToGallery, showTitles
                brains = gallery.getFolderContents()
                ids = [b.getId for b in brains if b.portal_type == 'Image']
                if props.getProperty('random'):
                    shuffle(ids)
                count = props.getProperty('numberOfPhotos')
                if count > 0:
                    ids = ids[:count]
                showTitles = props.getProperty('showTitles')
                self.showClickToEnlarge = props.getProperty('showClickToEnlarge')
                self.showLinkToGallery = props.getProperty('showLinkToGallery')
                gallery_url = gallery.absolute_url()
                for id in ids:
                    if showTitles:
                        img = gallery[id]
                        item = dict(title = img.Title(),
                                    alt   = img.Description(),
                                    url   = img.absolute_url(),
                                    imgtag = img.tag(scale='thumb'),
                                    imgtag_large = img.tag(scale='large'),
                                    )
                    else:
                        image_url = "%s/%s" % (gallery_url, id)
                        item = dict(title = '',
                                    alt   = '',
                                    url   = image_url,
                                    imgtag = '<img src="%s/image_thumb" />' % image_url,
                                    imgtag_large = '<img src="%s/image_large" />' % image_url,
                                    )
                                    
                    result.append(item)
        self._images = result  
        self._gallery = aq_inner(gallery)
