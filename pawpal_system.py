from dataclasses import dataclass, field
from typing import List, Optional, Literal
from datetime import datetime

@dataclass
class Task:
    id: str
    description: str
    duration: int  # in minutes
    priority: Literal['High', 'Medium', 'Low']
    scheduled_time: Optional[datetime] = None
    is_complete: bool = False

@dataclass
class Pet:
    id: str
    name: str
    species: str
    tasks: List['Task'] = field(default_factory=list)

@dataclass
class Owner:
    id: str
    name: str
    pets: List['Pet'] = field(default_factory=list)

class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner

    def generate_schedule(self) -> List[Task]:
        """
        Gathers all tasks from owner's pets, sorts by priority and time,
        and generates optimized daily plan.
        """
        pass

    def detect_conflicts(self, tasks: List[Task]) -> List[str]:
        """
        Detects time conflicts between tasks.
        """
        pass

    def get_all_tasks(self) -> List[Task]:
        """
        Collects all tasks from all pets.
        """
        pass

