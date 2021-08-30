from loguru import logger
from typing import List

import requests
from lxml import etree

from common.classes import CourseInfo


def crawl_course(metadata: CourseInfo) -> CourseInfo:
    """Crawl NCKU course website for infomation

    Args:
        metadata(str): Course's metadata from directory structure
    """
    # Need to re-decode with utf-8, original is encoded with ISO-8859-1
    text: str = requests.get(
        "http://class-qry.acad.ncku.edu.tw/syllabus/online_display.php",
        params={
            "syear": metadata.year.zfill(4),
            "sem": metadata.semester,
            "co_no": metadata.course_id,
            "class_code": metadata.class_code if metadata.class_code != "0" else None
        }
    ).text.encode("ISO-8859-1").decode("utf-8")
    html: etree._Element = etree.HTML(text)

    title: etree._Element = html.xpath('//*[@id="header"]/h1/div/span')[1]
    filtered = list(filter(lambda child: child.tag == "br", title.getchildren()))
    course_names = list(map(lambda child: child.tail.strip(), filtered))

    sidebar: etree._Element = html.xpath('//*[@id="sidebar"]/div')[0]
    filtered = list(filter(lambda child: child.tag == "span", sidebar.getchildren()))
    information = list(map(lambda child: child.tail.strip(), filtered))

    return CourseInfo(**{
        "course_name": f"{course_names[0]} {course_names[1]}",
        "department": information[0],
        "instructor": information[1],
        "year": metadata.year,
        "semester": metadata.semester,
        "serial_number": information[4],
        "attribute_code": information[5],
        "course_id": metadata.course_id,
        "class_code": metadata.class_code,
        "credit": information[8],
        "language": information[9],
        "files": metadata.files,
    })
