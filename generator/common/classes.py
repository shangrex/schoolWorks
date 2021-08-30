from typing import List
from dataclasses import dataclass, field


@dataclass
class CourseInfo():
    course_id: str
    class_code: str
    year: str
    semester: str
    course_name: str = None
    department: str = None
    instructor: str = None
    serial_number: str = None # act as registeration code
    attribute_code: str = None
    credit: str = None
    language: str = None
    files: List[str] = field(default_factory=list)

    def dump_data(self):
        return {
            "files": self.files
        }

    def dump_index(self):
        return {
            "course_name": self.course_name,
            "course_id": self.course_id,
            "class_code": self.class_code,
            "year": self.year,
            "semester": self.semester,
            "department": self.department,
            "instructor": self.instructor,
            "serial_number": self.serial_number
        }
