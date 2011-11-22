from setuptools import setup, find_packages
import os

version = '1.2'

tests_require = ['collective.testcaselayer']

setup(name='collective.linkedgallery',
      version=version,
      description="Link and show gallery below content body in Plone.",
      long_description=open("README.txt").read() + "\n\n" +
                       open(os.path.join("docs", "UPGRADE.txt")).read() + "\n\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='gallery plone',
      author='Radim Novotny',
      author_email='novotny.radim@gmail.com',
      url='http://plone.org',
      license='GPL',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir = {'':'src'},
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'collective.fancybox',
          'archetypes.schemaextender',
      ],
      tests_require=tests_require,
      extras_require={'tests': tests_require},
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
