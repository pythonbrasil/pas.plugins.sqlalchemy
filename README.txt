SQLAlchemy PAS plugin
=====================

This package is a fork of the SQLPASPlugin. It uses SQLAlchemy as the
database abstraction layer; some tests have been rewritten but most
are preserved. It's used in production with a PostgreSQL database.

Setup
-----

To configure the plugin with a database, use ``z3c.saconfig`` and
define a named scoped session "pas.plugins.sqlalchemy" in your configure.zcml 
or in the "zcml-additional" parameter of the plone.recipe.zope2instance recipe in your buildout.

Example::

  <include package="z3c.saconfig" file="meta.zcml"/>
  <configure xmlns="http://namespaces.zope.org/db">
    <engine name="pas" url="postgresql://localhost/pas" />
        <session name="pas.plugins.sqlalchemy" engine="pas" />
  </configure>

Install the plugin using the included GenericSetup-profile. Note that
tables will be created automatically on installation.

You can reinstall anytime to create non-existing tables. Note that
tables are preserved on uninstallation.

Memberdata
----------

The users table has an extensive number of metadata fields; it's on
the to-do to figure out a nice way to make this pluggable.

Plone3.x compatibility
----------------------

This product should work with Zope2.9 and Python2.4.
You only need a new version of DateTime package.
On your buildout add DateTime to eggs:

[buildout]
...
eggs = 
    ...
    DateTime==2.12.6

Credits
-------

Authors

  - Rocky Burt <rocky@serverzen.com> of ServerZen Software

  - Nate Aune <natea@jazkarta.com> of Jazkarta

  - Stefan Eletzhofer <stefan.eletzhofer@inquant.de> of InQuant

  - Malthe Borch <mborch@gmail.com>
  
  - Derek Broughton <auspex@pointerstop.ca>

Contributors

  - Ruda Porto Filgueiras <rudazz@gmail.com>

  - Daniel Nouri <daniel.nouri@gmail.com>

  - Dorneles Treméa <deo@jarn.com> of Jarn

  - Wichert Akkerman <wichert@wiggy.net> of Simplon

  - Riccardo Lemmi <riccardo@reflab.it> of Reflab Srl

Sponsors

  - Thanks to ChemIndustry.com Inc. for financing the development of
    SQLPASPlugin

  - Thanks to Statens Byggeforskninginstitut (http://www.sbi.dk) for sponsoring
    the caching support.

  - Thanks to Gis & Web S.r.l. (http://www.gisweb.it) for sponsoring
    the groups management support.
    
  - Thanks to the Ocean Tracking Network (http://oceantrackingnetwork.org/) for
    adding Group Capabilities and migration of existing users.

License
-------

  GNU GPL v2 (see LICENCE.txt for details)
