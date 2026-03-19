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

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
