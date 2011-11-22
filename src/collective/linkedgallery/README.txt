.. -*-doctest-*-

Add folder with some dummy (empty) images

    >>> _ = self.folder.invokeFactory('Folder', 'gallery')
    >>> gallery = self.folder.gallery
    >>> _ = gallery.invokeFactory('Image', 'image1', title='Image 1')
    >>> _ = gallery.invokeFactory('Image', 'image2')
    >>> _ = gallery.invokeFactory('Image', 'image3')
    >>> _ = gallery.invokeFactory('Image', 'image4')
    >>> _ = gallery.invokeFactory('Image', 'image5')
    >>> _ = gallery.invokeFactory('Image', 'image6')
    >>> _ = self.folder.invokeFactory('Document', 'doc')
    >>> _ = self.folder.invokeFactory('News Item', 'news')
    >>> doc = self.folder.doc
    >>> news = self.folder.news

Check Document and News item has Gallery field (provided by extender), but not
Folders

    >>> doc.getField('linkedGallery')
    <Field linkedGallery(reference:rw)>
    >>> news.getField('linkedGallery')
    <Field linkedGallery(reference:rw)>
    >>> self.folder.getField('linkedGallery') is None
    True
    
Render the viewlet for Document and check there is nothing

    >>> from collective.linkedgallery.browser.gallery import GalleryViewlet
    >>> request = self.app.REQUEST
    >>> viewlet = GalleryViewlet(doc, request, None, None)
    >>> viewlet.update()
    >>> viewlet._gallery is None
    True
    >>> viewlet.images()
    []
    
Let assign the gallery

    >>> doc.getField('linkedGallery').set(doc, self.folder.gallery)
    >>> viewlet.update()
    >>> viewlet._gallery is None
    False
    >>> viewlet._gallery
    <ATFolder at /plone/Members/test_user_1_/gallery>
    >>> viewlet.images()
    [{...}]
    
Let's play with properties 

    >>> props = self.portal.portal_properties.linkedgallery_properties
    >>> len(viewlet.images()) == props.getProperty('numberOfPhotos')
    True
    
    >>> props._updateProperty('numberOfPhotos', 0)  # show all images
    >>> viewlet.update()
    >>> len(viewlet.images())
    6
    
    >>> props._updateProperty('random', False)
    >>> viewlet.update()
    >>> props.getProperty('showTitles')
    False
    >>> viewlet.images()[0]['title']
    ''
    >>> props._updateProperty('showTitles', True)
    >>> viewlet.update()
    >>> viewlet.images()[0]['title']
    'Image 1'

