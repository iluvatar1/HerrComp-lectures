#!/usr/bin/env python3

import argparse
from glob import glob
import uuid
import nbformat as nbf


def get_cell_id(id_length=8):
    return uuid.uuid4().hex[:id_length]


# -- MAIN
if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(
        description="Fix Jupyter notebook cell IDs if duplicated or forced."
    )
    parser.add_argument(
        "notebook", type=str, help="Path to the target .ipynb file"
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Force overwrite cell IDs even if no duplicates are found",
    )

    args = parser.parse_args()
    ipath = args.notebook

    print(f"Processing: {ipath}")

    # load notebook
    ntbk = nbf.read(ipath, nbf.NO_CONVERT)

    cell_ids = []
    for cell in ntbk.cells:
        # Using .get() prevents KeyErrors if some cells lack an ID
        cell_ids.append(cell.get("id"))
    #print("Current cell IDs:", cell_ids)

    # Check for duplicates
    has_duplicates = len(cell_ids) != len(set(cell_ids))

    # Reset cell ids if duplicates exist OR if --force flag is used
    if has_duplicates or args.force:
        if args.force and not has_duplicates:
            print("No duplicates found, but forcing ID regeneration...")
        else:
            print("Duplicates found! Regenerating cell IDs...")

        for cell in ntbk.cells:
            cell["id"] = get_cell_id()

        nbf.write(ntbk, ipath)
        print("Notebook successfully updated.")
    else:
        print("No duplicates found and --force not specified. No changes made.")
