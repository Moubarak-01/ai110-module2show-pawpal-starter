# PawPal+ Project Reflection

### 1. System Design

#### Core User Actions
1. **Manage Pet Profiles:** Users can create and store profiles for multiple pets, including essential details like name and species, to establish a personalized care context.
2. **Define and Prioritize Tasks:** Users can add specific care activities (feeding, walking, medication) and assign each a duration and priority level (High, Medium, Low) to guide the scheduling logic.
3. **Generate Optimized Schedules:** Users can trigger a scheduling engine that organizes all pending tasks into a chronological daily plan based on priority and time constraints, including a brief explanation of the reasoning.

**a. Initial design**

- **Description:** My initial UML design focused on a modular architecture where data (Pets/Tasks) is separated from the logic (Scheduler). I used Python Dataclasses for the data entities to keep the code clean and focused on attributes.
- **Classes & Responsibilities:**
    - `Owner`: Acts as the primary data store, managing a collection of `Pet` objects.
    - `Pet`: Holds specific information about an animal and a list of `Task` objects assigned to it.
    - `Task`: A simple data object containing the description, duration, priority level, and time for a specific activity.
    - `Scheduler`: The "engine" of the app; it communicates with the `Owner` to gather all tasks and applies sorting and conflict-detection logic to create the daily plan.

**b. Design changes**

- **Did your design change?** Yes.
- **Change & Reason:** Initially, I planned for the `Pet` class to handle its own scheduling. However, during implementation, I realized that a centralized `Scheduler` class was more efficient. This change allowed the system to detect conflicts between tasks for *different* pets (e.g., two dogs needing a walk at the same time) which wouldn't have been possible if the logic was hidden inside individual Pet objects.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

My scheduler considers two main constraints: Priority (High, Medium, Low) and scheduled Time. I decided that Priority was the most important constraint because it ensures critical care activities—like administering medication—happen regardless of their timing. This prioritization reflects real-world pet care needs where urgent tasks must take precedence over routine ones.

**b. Tradeoffs**

I implemented a 'lightweight' conflict detection system that checks for overlapping task times but doesn't account for 'travel time' or 'prep time' between activities. This tradeoff is reasonable for a Minimum Viable Product (MVP) because it keeps the user interface clean and simple, avoiding complexity that could overwhelm new users while still providing essential conflict warnings.

---

## 3. AI Collaboration

**a. How you used AI**

I used AI tools extensively throughout this project for design brainstorming, code generation, and debugging. Specifically, I leveraged AI for brainstorming the initial UML class diagram, generating Mermaid.js syntax for visual diagrams, and scaffolding Python Dataclasses with proper type hints. The most helpful prompts were those asking for complete code implementations with specific requirements, such as "implement this method with these parameters."

**b. Judgment and verification**

I rejected an AI suggestion to put scheduling logic inside the Pet class, instead choosing a centralized Scheduler class. I evaluated this by considering the real-world use case: with multiple pets, conflicts could occur between tasks for different animals (like two dogs needing walks simultaneously). A centralized approach better handles these cross-pet scenarios, which individual Pet objects couldn't detect. I verified this by sketching out the data flow and confirming the Scheduler's access to all tasks.

---

## 4. Testing and Verification

**a. What you tested**

I created a comprehensive pytest suite that verified three critical behaviors: 1. Task addition to pets, ensuring new tasks were properly stored; 2. Priority sorting, confirming High-priority tasks appeared before Medium in the generated schedule; and 3. Conflict detection, validating that overlapping tasks triggered appropriate warnings. These tests were important because they ensured the core scheduling logic worked correctly before integrating with the Streamlit UI.

**b. Confidence**

I have 5-star confidence that my scheduler works correctly for the implemented features. If I had more time, I would test edge cases like 'overnight tasks' (activities crossing midnight) or 'zero-minute duration' tasks to ensure robustness in unusual scenarios.

---

## 5. Reflection

**a. What went well**

I was most satisfied with seeing the backend logic successfully 'drive' the Streamlit UI. Watching tasks appear in the schedule with proper priority colors and conflict warnings made the abstract code feel tangible and functional.

**b. What you would improve**

If I had another iteration, I would add a 'Calendar View' for visualizing the full day's schedule and implement 'Push Notifications' for task reminders to make the app more proactive rather than reactive.

**c. Key takeaway**

I learned that the 'Lead Architect' role is about verifying AI logic—AI is great at generating code, but the human must ensure the relationships between classes (like Owner and Pet) make sense for the real-world use case. A specific challenge was managing Streamlit Session State (st.session_state) to ensure the Owner object and added tasks didn't disappear when the app refreshed after a button click.
