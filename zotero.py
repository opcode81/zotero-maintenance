import sys
from optparse import OptionParser
import sqlite3
from pathlib import Path
import os
import shutil


if __name__ == '__main__':
    parser = OptionParser(
        prog='Zotero Maintenance',
        description='Supports maintenance operations on the Zotero local storage')
    parser.add_option("--delete-library-storage", dest="delete_library_id",
        help="delete files from local storage that are associated with library ID", metavar="ID")

    (options, args) = parser.parse_args()

    zotero_home = Path.home() / "Zotero"
    db_path = zotero_home / "zotero.sqlite"
    if not os.path.exists(db_path):
        print(f"Could not find Zotero home directory in {zotero_home}")
        parser.print_help()
        sys.exit(1)

    con = sqlite3.connect(db_path)

    if options.delete_library_id:
        library_id = options.delete_library_id
        print(f"Deleting library id {library_id} ...")
        res = con.execute(f"SELECT key FROM items WHERE libraryID={library_id}")
        ids = [x[0] for x in res.fetchall()]
        storage_path = zotero_home / "storage"
        for identifier in ids:
            item_path = storage_path / identifier
            if os.path.exists(item_path):
                print(item_path)
                shutil.rmtree(item_path)
    else:
        parser.print_help()
