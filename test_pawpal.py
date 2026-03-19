import pytest
from pawpal_system import Owner, Pet, Task, Scheduler
from datetime import datetime

def test_task_addition():
    """Verify that adding a task to a Pet increases that pet's task count."""
    pet = Pet(id="p1", name="Buddy", species="Dog")
    initial_count = len(pet.tasks)
    
    new_task = Task(id="t1", description="Walk", duration=20, priority="Low")
    pet.tasks.append(new_task)
    
    assert len(pet.tasks) == initial_count + 1
    assert pet.tasks[0].description == "Walk"

def test_task_completion_status():
    """Verify that the is_complete status can be toggled."""
    task = Task(id="t1", description="Feed", duration=10, priority="High")
    assert task.is_complete is False
    
    task.is_complete = True
    assert task.is_complete is True

def test_scheduling_priority():
    """Verify that the scheduler sorts High priority before Medium."""
    owner = Owner(id="o1", name="Test")
    pet = Pet(id="p1", name="Luna", species="Cat")
    owner.pets.append(pet)
    
    t_med = Task(id="t1", description="Med Task", duration=10, priority="Medium")
    t_high = Task(id="t2", description="High Task", duration=10, priority="High")
    
    pet.tasks.extend([t_med, t_high])
    
    scheduler = Scheduler(owner)
    schedule = scheduler.generate_schedule()
    
    # High priority should be first index [0]
    assert schedule[0].priority == "High"
    assert schedule[1].priority == "Medium"