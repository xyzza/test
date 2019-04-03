"""
initial migration
"""

from yoyo import step

__depends__ = {"__init__"}

# fmt: off
steps = [
    step(
        """
            CREATE TABLE counter (req INTEGER);
            INSERT INTO counter (req) values (0);
        """,
        """
            DROP TABLE counter;
        """
    )
]
# fmt: on
