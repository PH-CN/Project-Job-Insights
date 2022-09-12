from functools import lru_cache
import csv


@lru_cache
def read(path):
    result = []
    with open(path) as file:
        jobs_reader = csv.DictReader(file, delimiter=",")
        for job in jobs_reader:
            result.append(job)
    return result
    # """Reads a file from a given path and returns its contents

    # Parameters
    # ----------
    # path : str
    #     Full path to file

    # Returns
    # -------
    # list
    #     List of rows as dicts
    # """
