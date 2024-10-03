from datetime import datetime
from typing import Union


class TimeStamp():
    created_at: datetime
    modified_at: datetime
    created_by: Union[int, None]
    modified_by: Union[int, None]
