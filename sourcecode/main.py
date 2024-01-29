#!/usr/bin/env python3
# source communitynotes_env/bin/activate

"""Invoke Community Notes scoring and user contribution algorithms.

Example Usage:
  # If there is only one rating file, pass the file path to the --ratings flag.
  python main.py \
    --enrollment data/userEnrollment-00000.tsv \
    --notes data/notes-00000.tsv \
    --ratings data/ratings-00000.tsv \
    --status data/noteStatusHistory-00000.tsv \
    --outdir data

  # If there are multiple rating files, move them to a directory, 
  # and pass the directory path to the --ratings flag.
  python main.py \
    --enrollment data/userEnrollment-00000.tsv \
    --notes data/notes-00000.tsv \
    --ratings data/ratings \
    --status data/noteStatusHistory-00000.tsv \
    --outdir data
"""
"""
python main.py \
    --enrollment '$path/user.csv' \
    --notes '$path/note.csv' \
    --ratings '$path/rating.csv' \
    --status '$path/status.csv' \
    --outdir '$path'
"""
from scoring.runner import main


if __name__ == "__main__":
  main()
