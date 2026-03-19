from pawpal_system import Owner, Pet, Task, Scheduler
from datetime import datetime

def run_demo():
    # 1. Setup Data
    owner = Owner(id="o1", name="Moubarak")
    
    dog = Pet(id="p1", name="Buddy", species="Dog")
    cat = Pet(id="p2", name="Luna", species="Cat")
    
    owner.pets.extend([dog, cat])

    # 2. Add Tasks (Mix up the order to test your sorting logic!)
    t1 = Task(id="t1", description="Evening Walk", duration=30, priority="Medium", 
              scheduled_time=datetime(2026, 3, 18, 18, 0)) # 6:00 PM
    
    t2 = Task(id="t2", description="Emergency Meds", duration=10, priority="High", 
              scheduled_time=datetime(2026, 3, 18, 12, 0)) # 12:00 PM
    
    t3 = Task(id="t3", description="Cat Feeding", duration=15, priority="High", 
              scheduled_time=datetime(2026, 3, 18, 8, 0)) # 8:00 AM

    dog.tasks.append(t1)
    dog.tasks.append(t2)
    cat.tasks.append(t3)

    # 3. Run Scheduler
    scheduler = Scheduler(owner)
    daily_plan = scheduler.generate_schedule()

    # 4. Print Results
    print(f"--- {owner.name}'s Daily Pet Care Schedule ---")
    for task in daily_plan:
        time_str = task.scheduled_time.strftime("%I:%M %p") if task.scheduled_time else "Unscheduled"
        print(f"[{time_str}] ({task.priority}) {task.description}")

if __name__ == "__main__":
    run_demo()