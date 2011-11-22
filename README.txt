Introduction
============

collective.linkedgallery allows to link any folder in Plone to any content
item (using reference field). If the target folder contain images, these
images will be displayed under body of particular content item.

Installation
------------

Add collective.linkedgallery to your buildout as normal. See
http://plone.org/documentation/tutorial/buildout. Don't forget to load the
configure.zcml file!

Then install the product via Plone's Add-on products control panel.

Usage
-----

Edit any Document or News Item object and use Gallery field to reference
existing folder with pictures. Pictures will be displayed on the view template
below content body.

Configuration
-------------

There are several properties in the portal_properties/linkedgallery_properties
property sheet.

 * random (True) - Randomize photos in the gallery view
 
 * numberOfPhotos (4) - Number of photos shown in the gallery (0 = all)
 
 * showLinkToGallery (True) - Show link to gallery. If not set, show gallery
   title only.
 
 * showTitles (False) - Show titles of photos (wakes images from ZODB)
 
 * showClickToEnlarge (True) - Show "click to enlarge" message

