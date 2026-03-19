import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler
from datetime import datetime, timedelta

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

# --- STEP 1: INITIALIZE SESSION STATE ---
# This ensures our Owner object persists across button clicks
if "owner" not in st.session_state:
    # Create a default owner and one default pet to start
    initial_owner = Owner(id="o1", name="Moubarak")
    initial_pet = Pet(id="p1", name="Boss", species="Dog") # Changed from "Mochi" to "Boss" cause my dog is called Boss and I want to see his name in the app :)
    initial_owner.pets.append(initial_pet)
    st.session_state.owner = initial_owner

owner = st.session_state.owner

st.title("🐾 PawPal+")

# --- STEP 2: OWNER & PET INFO ---
st.subheader(f"Owner: {owner.name}")
# Simple pet display
if owner.pets:
    pet_names = ", ".join([p.name for p in owner.pets])
    st.caption(f"Managing care for: {pet_names}")

st.divider()

# --- STEP 3: ADD TASKS (Wired to Logic) ---
st.subheader("Add a New Task")
col1, col2, col3, col4 = st.columns(4)
with col1:
    task_title = st.text_input("Task title", value="Morning Walk")
with col2:
    duration = st.number_input("Duration (mins)", min_value=1, value=30)
with col3:
    priority = st.selectbox("Priority", ["High", "Medium", "Low"])
with col4:
    task_time = st.time_input("Scheduled Time", datetime.now().time())

if st.button("Add Task"):
    # Create the Task object
    combined_dt = datetime.combine(datetime.now().date(), task_time)
    new_task = Task(
        id=f"t{datetime.now().timestamp()}", 
        description=task_title, 
        duration=int(duration), 
        priority=priority,
        scheduled_time=combined_dt
    )
    
    # Add it to the first pet (Mochi) for this demo
    owner.pets[0].tasks.append(new_task)
    st.success(f"Added '{task_title}' to {owner.pets[0].name}'s list!")

# --- STEP 4: GENERATE SCHEDULE (Wired to Logic) ---
st.divider()
st.subheader("Today's Optimized Schedule")

if st.button("Generate Schedule"):
    scheduler = Scheduler(owner)
    daily_plan = scheduler.generate_schedule()
    
    # NEW: Check for conflicts
    conflicts = scheduler.detect_conflicts(daily_plan)
    for warning in conflicts:
        st.warning(warning)
    
    if not daily_plan:
        st.info("No tasks added yet. Add a task above to see the scheduler in action.")
    else:
        # Display the sorted schedule
        for task in daily_plan:
            time_str = task.scheduled_time.strftime("%I:%M %p")
            # Use color based on priority
            color = "🔴" if task.priority == "High" else "🟡" if task.priority == "Medium" else "🟢"
            st.write(f"{color} **{time_str}** - {task.description} ({task.duration} mins)")
        
        st.balloons()
        st.info("💡 Reasoning: High priority tasks are scheduled first, followed by Medium and Low.")