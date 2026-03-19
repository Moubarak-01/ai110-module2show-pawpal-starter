from dataclasses import dataclass, field
from typing import List, Optional, Literal
from datetime import datetime

@dataclass
class Task:
    """Represents a specific care activity for a pet with priority and scheduling information."""
    id: str
    description: str
    duration: int  # in minutes
    priority: Literal['High', 'Medium', 'Low']
    scheduled_time: Optional[datetime] = None
    is_complete: bool = False

@dataclass
class Pet:
    """Represents a pet with associated care tasks."""
    id: str
    name: str
    species: str
    tasks: List['Task'] = field(default_factory=list)

@dataclass
class Owner:
    """Represents the owner who manages multiple pets and their care tasks."""
    id: str
    name: str
    pets: List['Pet'] = field(default_factory=list)

class Scheduler:
    """Organizes and manages pet care tasks into an optimized daily schedule."""
    def __init__(self, owner: Owner):
        """Initialize the scheduler with an owner's data."""
        self.owner = owner

    def generate_schedule(self) -> List[Task]:
        """Retrieves all pet tasks and returns them sorted by priority and time."""
        all_tasks = self.get_all_tasks()
        
        # Define priority order (High > Medium > Low)
        priority_order = {'High': 0, 'Medium': 1, 'Low': 2}
        
        # Sort by priority first, then by scheduled_time
        sorted_tasks = sorted(
            all_tasks,
            key=lambda task: (priority_order[task.priority], task.scheduled_time or datetime.max)
        )
        
        return sorted_tasks

    def detect_conflicts(self, tasks: List[Task]) -> List[str]:
        """Identifies tasks that overlap in time and returns a list of conflict descriptions."""
        pass

    def get_all_tasks(self) -> List[Task]:
        """Collects and returns all tasks from all pets."""
        all_tasks = []
        for pet in self.owner.pets:
            all_tasks.extend(pet.tasks)
        return all_tasks

