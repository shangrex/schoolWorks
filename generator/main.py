import argparse
import os

from loguru import logger

from crawler import crawl_course
from utilities import get_metadata, generate_data, generate_index

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--path",
        "-P",
        required=True,
        help="asset path",
    )
    args = parser.parse_args()
    courses = []
    for metadatum in get_metadata(args.path):
        if courses:
            break
        try:
            courses.append(crawl_course(metadatum))
        except Exception as warning:
            logger.warning(warning)
            courses.append(metadatum)

    for course in courses:
        generate_data(args.path, course)
    generate_index(args.path, courses)
