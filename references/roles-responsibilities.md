# Roles and Responsibilities in Fagan Inspections

Detailed description of each role in the inspection process, qualifications, and specific duties.

---

## Role Overview

A typical inspection team has **4 people** with distinct roles:

1. **Moderator** - Process manager and facilitator (most critical role)
2. **Designer** - Created the design or architecture
3. **Implementor/Coder** - Implements the design (often the "reader")
4. **Tester** - Responsible for testing the code

**Key principle**: Separation of roles creates objectivity and diverse perspectives.

---

## Moderator

### The Most Critical Role

The moderator makes or breaks the inspection process. This role requires special training and specific qualities.

### Primary Objective
Manage the inspection team and process to maximize error detection while maintaining team morale.

### Qualifications and Requirements

**Must Have:**
- Competent programmer (understands code and design)
- Process discipline and attention to detail
- Team management skills
- Tact, sensitivity, and emotional intelligence

**Should Have:**
- Moderator training (brief but very advantageous)
- Experience with inspection process
- Knowledge of team dynamics

**Should NOT:**
- Be technical expert on the program being inspected
- Have strong opinions about the design approach
- Be from the same project (ideally from unrelated project)

**Why from unrelated project?**
- Preserves objectivity
- No preconceptions about the design
- Can ask "naive" questions that reveal errors
- No personal investment in design decisions

### Responsibilities by Phase

#### Before Inspection

**Planning:**
- Schedule inspection when code/design reaches entry criteria
- Ensure all participants available
- Book suitable meeting room
- Confirm 2-hour maximum duration

**Material Distribution:**
- Collect all documentation from designer
- Distribute to all participants 1-2 days before
- Ensure completeness of materials
- Provide recent error distributions and checklists

**Team Preparation:**
- Confirm all participants are preparing
- Answer process questions
- Provide guidance on checklist usage

#### During Overview (if held)

- Ensure designer presents clearly
- Keep overview high-level and focused
- Prevent debugging or deep technical discussions
- Ensure all participants understand context

#### During Inspection Meeting

**Process Management:**
- Start meeting promptly
- Confirm all participants prepared (if not, reschedule)
- Remind team of objective: find errors only
- Keep team focused on one objective at a time

**Meeting Facilitation:**
- Ensure reader is paraphrasing, not just reading
- Maintain steady pace through material
- Enforce 100% coverage (every line, every branch)
- Prevent solution hunting and design debates
- Use tact to redirect off-topic discussions

**Error Documentation:**
- Note each error as identified
- Write clear, concise description
- Classify by type (LO, IC, TB, etc.)
- Mark severity (Major or Minor)
- Record location (file, line, function)
- Note obvious solutions but don't require them
- Don't let documentation slow the meeting

**Time Management:**
- Monitor time continuously
- Maintain pace to cover all material
- Hard stop at 2 hours (efficiency drops after)
- If material won't fit, schedule continuation session

**Team Dynamics:**
- Ensure all team members can contribute
- Prevent any member from dominating
- Maintain positive, constructive atmosphere
- Use sensitivity to keep discussion professional
- Prevent defensive reactions from author

#### After Inspection Meeting

**Reporting (within 24 hours):**
- Produce written inspection report
- Include all errors with classifications
- Summarize effort (preparation, meeting time)
- Document participants and roles
- Estimate rework effort
- Identify areas for reinspection

**Report Distribution:**
- Provide to author for rework
- Provide to team leader
- File for metrics and process improvement
- Keep copy for follow-up

#### During Follow-Up

**Verification:**
- Review all fixes made by author
- Verify each error properly addressed
- Check for "bad fixes" (fixes that introduce new errors)
- Ensure no items left unresolved

**Reinspection Decision:**
- Calculate percentage of material reworked
- If >5%: Schedule full reinspection (mandatory)
- If <5%: Use discretion
  - Personal verification
  - Partial team reinspection
  - Spot-check critical fixes

**Sign-Off:**
- Verify all exit criteria met
- Obtain signatures from all participants
- Confirm checkpoint complete
- Authorize proceeding to next phase

**Metrics Collection:**
- Record all metrics from inspection
- Update error type distributions
- Calculate inspection effectiveness
- Identify error-prone modules
- Feed data forward to process improvement

### Key Skills for Moderators

**Process Skills:**
- Time management
- Meeting facilitation
- Documentation discipline
- Follow-up persistence

**People Skills:**
- Tact and diplomacy
- Conflict resolution
- Motivation and encouragement
- Objective feedback delivery

**Technical Skills:**
- Code/design comprehension
- Error pattern recognition
- Impact assessment
- Technical judgment

### Moderator Training Topics

A brief training program should cover:

1. **Inspection philosophy and objectives**
   - Why separate finding from fixing
   - Why 2-hour limit
   - Why 100% coverage

2. **Meeting management techniques**
   - Starting strong
   - Maintaining pace
   - Handling discussions
   - Documenting efficiently

3. **Team dynamics**
   - Encouraging participation
   - Managing strong personalities
   - Preventing defensive reactions
   - Using the "coach" approach

4. **Error classification**
   - Type, category, severity system
   - Clear description writing
   - Quick classification during meeting

5. **Follow-up process**
   - Verification techniques
   - Reinspection criteria
   - Sign-off procedure

6. **Common pitfalls and how to avoid them**
   - Solution hunting
   - Design debates
   - Time overruns
   - Incomplete follow-up

### Success Factors for Moderators

**What makes a great moderator:**
- Keeps team focused on finding errors
- Creates synergistic team effect
- Maintains positive atmosphere
- Documents thoroughly and quickly
- Follows up persistently
- Continuously improves process

**What undermines moderator effectiveness:**
- Letting meetings become debugging sessions
- Allowing time to exceed 2 hours
- Incomplete or delayed reporting
- Weak follow-up
- Using inspection results against programmers
- Being too technical or too process-focused

---

## Designer

### Primary Objective
Present the design and participate in finding errors.

### Qualifications
- Programmer who created the design
- Deep understanding of design decisions
- Knowledge of requirements and constraints

### Responsibilities by Phase

#### During Overview
- Present overall design approach
- Explain key decisions and rationale
- Describe logic flow and major paths
- Clarify dependencies and interfaces
- Answer questions about design intent
- Distribute all documentation

#### During Preparation
- Ensure all documentation is complete
- Be available for clarification questions
- Review own design with fresh perspective
- Use checklists to self-inspect

#### During Inspection Meeting
- Answer questions about design intent
- Clarify ambiguities
- Participate in error finding (not just defending)
- Accept feedback professionally
- Don't become defensive
- Focus on finding errors, not justifying choices

#### During Rework (Design Inspection)
- Fix all errors identified
- Update design documentation
- Check for similar errors in related areas
- Complete within agreed timeline

#### During Follow-Up
- Demonstrate all fixes to moderator
- Explain resolution of each error
- Sign off that all issues resolved
- Commit to reinspection if needed

### Critical Mindset
- **Not about defending the design**
- **About finding and fixing errors**
- **Errors are learning opportunities**
- **Team is helping, not attacking**

### Special Considerations

**When designer also codes:**
- May serve dual role in I₁ and I₂
- Harder to maintain objectivity
- More important to have independent moderator
- Consider having external coder review

**When design is by committee:**
- Primary designer leads overview
- All contributors participate in inspection
- Clear ownership for rework
- Ensure consistent design decisions

---

## Implementor/Coder

### Primary Objective
Serve as "reader" in inspection and provide implementor's perspective.

### Qualifications
- Programmer who will implement (or did implement) the design
- Understanding of implementation constraints
- Knowledge of coding standards and practices

### Responsibilities by Phase

#### During Overview
- Understand design from implementor's perspective
- Ask questions about implementation approach
- Clarify ambiguities for coding
- Note areas of complexity

#### During Preparation
- Study design/code thinking about implementation
- Consider how to implement each part
- Use checklists systematically
- Note questions and potential errors

#### During Inspection Meeting - The "Reader" Role

**Most Active Participant:**
- Paraphrase how they will/did implement
- Explain logic in own words (don't just read)
- Walk through every line systematically
- Take every branch mentally
- Expose misunderstandings through paraphrasing

**Why Paraphrasing Works:**
- Forces active processing
- Reveals gaps in understanding
- Exposes ambiguities in design
- Triggers questions from team
- Creates "aha moments" for errors

**Reader Technique:**
- "In this function, I will..."
- "First I check whether..."
- "Then I loop through..."
- "In the error case, I return..."

#### During Rework (Code Inspection)
- Fix all errors identified
- Update code and comments
- Run tests to verify fixes
- Check for side effects

#### During Follow-Up
- Demonstrate fixes
- Explain resolution approach
- Verify no new errors introduced

### Success Factors

**Effective readers:**
- Paraphrase clearly and completely
- Cover all material systematically
- Don't rush or skip "obvious" parts
- Accept questions and feedback
- Stay focused on implementation

**Ineffective readers:**
- Just read code verbatim
- Skip sections as "too simple"
- Become defensive about implementation
- Argue about questions
- Rush to finish

---

## Tester

### Primary Objective
Provide testability and quality perspective.

### Qualifications
- Programmer responsible for testing
- Knowledge of testing techniques
- Understanding of quality requirements

### Responsibilities by Phase

#### During Preparation
- Study design/code from testing perspective
- Consider how to test each feature
- Identify hard-to-test areas
- Note edge cases and error paths
- Review checklist for test coverage

#### During Inspection Meeting

**Testing Perspective Questions:**
- Is this testable?
- How would I test this?
- What edge cases exist?
- Are error paths testable?
- Is observability sufficient?

**Error Finding Focus:**
- Missing error handling
- Untestable logic
- Missing edge cases
- Insufficient validation
- Poor error messages

**Contributions:**
- Raise testability concerns
- Identify missing test cases
- Note observability issues
- Suggest test scenarios

#### After Inspection
- Update test plans based on inspection
- Add test cases for errors found
- Consider edge cases identified

### Value to Inspection

**Tester brings:**
- Quality mindset
- Edge case thinking
- Error path focus
- Testability awareness
- Different perspective from designer/coder

---

## Team Composition Variations

### Ideal 4-Person Team
- Moderator (from unrelated project)
- Designer
- Coder (reader)
- Tester

### When Roles Overlap

**Designer Also Codes:**
- Designer serves dual role
- Bring in coder from related project for reader role
- Important to have external perspective

**Designer/Coder Also Tests:**
- Bring in two external programmers:
  - One for coder/reader role
  - One for tester role
- Or bring in tester with testing experience

**Small Team:**
- Minimum: Moderator + Author + 1 external reviewer
- Less ideal but better than no inspection
- External reviewer serves multiple perspectives

### Large or Complex Code

**May Include:**
- Additional programmers if many interfaces
- Domain expert for specialized logic
- Security expert for security-critical code
- Performance expert for performance-critical code

**Keep team manageable:**
- Don't artificially inflate beyond 4
- Additional specialists join for specific sections
- Rotating team members for different modules

---

## Role Interaction Dynamics

### Healthy Dynamics
- Mutual respect among all participants
- Collaborative error finding
- Professional questioning
- Accepting feedback constructively
- Shared goal of quality

### Unhealthy Dynamics to Avoid
- Designer becomes defensive
- Coder criticizes design choices
- Tester finds fault personally
- Moderator becomes too authoritarian
- Team becomes adversarial

### Moderator's Role in Team Dynamics

**Create positive environment:**
- Emphasize team goal: find errors
- Remind: errors are opportunities to improve
- Prevent personal criticism
- Recognize contributions
- Keep discussion professional
- Use humor appropriately

**The "Coach" Approach:**
- Moderator as coach, not referee
- Team as collaborative, not competitive
- Errors as learning, not failure
- Inspection as improvement, not judgment

---

## Role Assignment Best Practices

### Selecting Moderator
- Choose from unrelated project (objectivity)
- Must have moderator training
- Should have inspection experience
- Good interpersonal skills essential

### Selecting Team Members
- Designer: Original design author
- Coder: Person who will/did implement
- Tester: Person responsible for testing
- All should have inspection experience or training

### Avoiding Conflicts of Interest
- Manager should not moderate subordinate's code
- Competitors for promotion should not inspect each other
- Political rivals should not be on same team

### Rotation Strategy
- Rotate moderator role among trained personnel
- Rotate team members across projects
- Cross-pollinate knowledge and techniques
- Build inspection capability across organization

---

## Training for All Roles

### All Participants Should Understand:
- Inspection objectives and philosophy
- Five-phase process
- Their specific role and responsibilities
- Error classification system
- Checklist usage
- Meeting protocols

### Role-Specific Training:
- **Moderator**: Team management, process facilitation (half-day course)
- **Reader**: Paraphrasing techniques, pacing (2 hours)
- **All**: Error classification, checklist usage (2 hours)

### Continuous Learning:
- Review metrics after each inspection
- Discuss what worked/didn't work
- Share effective techniques
- Update checklists based on errors found
- Improve process continuously

---

## Measuring Role Effectiveness

### Moderator Effectiveness:
- Inspections completed on time?
- Reports delivered within 24 hours?
- Follow-up completed thoroughly?
- Team satisfaction with process?
- Error detection efficiency?

### Reader Effectiveness:
- All material covered?
- Paraphrasing revealing errors?
- Pace appropriate?
- Team able to follow?

### Team Effectiveness:
- Errors found per inspection?
- Major errors identified?
- Preparation quality?
- Meeting productivity?
- Positive team dynamics?

---

## Special Situations

### Remote/Distributed Teams
- Use video conferencing for inspection meeting
- Share screens for code walkthrough
- Moderator shares notes in real-time
- Preparation still individual
- May need longer meeting (communication overhead)

### Solo Developer
- Can't have traditional inspection
- Use "self-inspection" with checklists
- Pair programming as inspection variant
- External code review asynchronously
- Still track errors and metrics

### Open Source Projects
- Pull request reviews as inspection variant
- Maintainer as moderator
- Contributor as designer/coder
- Reviewers as team members
- Asynchronous but systematic

---

Remember: The roles exist to create diverse perspectives and objectivity. Each role contributes unique value. The synergistic effect of the team finds more errors than any individual could alone.
