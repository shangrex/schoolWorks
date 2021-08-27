from endpoints.classes import Resource

from .get import DOC as get_doc
from .get import get

HEALTH = [
    Resource(
        "GET",
        "/health",
        get,
        """
            Health check, used to check service availability
        """,
        "Health check",
        get_doc,
    )
]
