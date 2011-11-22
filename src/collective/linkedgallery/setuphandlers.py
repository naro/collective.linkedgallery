from Products.CMFCore.utils import getToolByName

_PROPERTIES = [
    # Randomize photos in the gallery
    dict(name='random', type_='boolean', value=True),
    # Number of photos shown in the gallery (0 = all)
    dict(name='numberOfPhotos', type_='int', value=4),
    # Show link to gallery
    dict(name='showLinkToGallery', type_='boolean', value=True),
    # Show titles of photos (requires wake object so use with care)
    dict(name='showTitles', type_='boolean', value=False),
    # Show "click to enlarge" message
    dict(name='showClickToEnlarge', type_='boolean', value=True),
]


def importVarious(context):
    if not context.readDataFile('collective.linkedgallery.txt'):
        return

    site = context.getSite()
    ptool = getToolByName(site, 'portal_properties')
    props = ptool.linkedgallery_properties

    for prop in _PROPERTIES:
        if not props.hasProperty(prop['name']):
            props.manage_addProperty(prop['name'], prop['value'], prop['type_'])
