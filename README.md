# zotero-maintenance

zotero-maintenance is a Python script which provides maintenance functions for the local storage of your Zotero reference database.
Run it with `python zotero.py` for help.

In particular, 

 * it allows to delete the local content that has been downloaded for a library via parameter

       --delete-library-storage <libraryId>

   which will delete all *local* content belonging to a particular library but will not affect its online storage.
   This can be useful when trying to get rid of library content that is no longer relevant, especially in cases where local storage is not readily available (e.g. when using OneDrive).
   
 * it allows to list all available libraries via parameter

       --list-libraries

    in order to determine the library identifier for the former command.
   
Close Zotero before running the tool!
