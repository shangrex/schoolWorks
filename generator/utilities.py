from typing import List
import os
import json

from common.classes import CourseInfo

def get_metadata(asset: str) -> List[CourseInfo]:
    """Get list of courses' metadata for later crawler use

    Args:
        path (str): Asset path
    """
    courses: List[CourseInfo] = []
    # Grep courses by DFS
    course_ids = os.listdir(asset)
    course_ids.remove("EXAMPLE")
    course_ids.remove("index.json")
    for course_id in course_ids:
        semesters = os.listdir(f"{asset}/{course_id}")
        if "unknown" in semesters:
            semesters.remove("unknown")
        for semester in semesters:
            # remove json data
            class_codes =  list(
                filter(lambda class_code: ".json" not in class_code, os.listdir(f"{asset}/{course_id}/{semester}"))
            )
            for class_code in class_codes:
                courses.append(CourseInfo(**{
                    "course_id": course_id,
                    "class_code": class_code,
                    "year": semester.split("_")[0],
                    "semester": semester.split("_")[1],
                    "files": os.listdir(f"{asset}/{course_id}/{semester}/{class_code}")
                }))
    return courses


def generate_data(path: str, course: CourseInfo):
    """Generate data.json according to course info

    Args:
        path (str): Asset path
        course (CourseInfo): course info to be dumped
    """
    with open(
        f"{path}/{course.course_id}/{course.year}_{course.semester}/{course.class_code}.json",
        "w+"
    ) as fp:
        json.dump(course.dump_data(), fp, ensure_ascii=False)


def generate_index(path: str, courses: List[CourseInfo]):
    """Fetch each data.json and create an index.json"""
    with open(f"{path}/index.json", "w+") as fp:
        json.dump([course.dump_index() for course in courses], fp, ensure_ascii=False)
