# Fagan Inspection Phases - Complete Reference

This document provides detailed guidance on each of the five inspection operations.

## Overview of the Process

1. **Overview** (optional) - Team meeting for new material
2. **Preparation** - Individual study with checklists
3. **Inspection Meeting** - Team error finding (2hr max)
4. **Rework** - Author fixes all errors
5. **Follow-Up** - Moderator verifies fixes

**Reinspection:** Required if >5% reworked, otherwise moderator discretion.

---

## Operation 1: Overview

### Objective
Communication and education about the material being inspected.

### When to Conduct
- New material that team hasn't seen before
- New team members joining the inspection
- Complex or unusual design requiring context
- **Skip if**: Same team that reviewed earlier design phases

### Participants
- Designer (presenter)
- All inspection team members
- Optional: Additional stakeholders for context

### Activities

**Designer presents:**
1. Overall area being addressed
2. Design approach and key decisions
3. Specific areas designed in detail
4. Logic flow and major paths
5. External dependencies and interfaces
6. Any special considerations or constraints

**Team receives:**
- All documentation to be inspected
- Background materials (specs, earlier designs, standards)
- Any reference materials needed

### Duration
- Variable based on material complexity
- Typical rate: 500 LOC/hour for design

### Outputs
- Shared understanding of design intent
- Documentation distributed to all participants
- Questions identified for preparation phase
- Meeting scheduled for inspection

### Best Practices
- Keep it high-level; avoid debugging during overview
- Focus on "what" and "why", not "how"
- Ensure all participants have complete documentation
- Schedule inspection meeting 1-2 days after overview (preparation time)

---

## Operation 2: Preparation

### Objective
Individual education and understanding of the material to maximize inspection effectiveness.

### Participants
All inspection team members work **individually**.

### Duration
- Design (I₁): 100 LOC/hour
- Code (I₂): 125 LOC/hour
- Total time varies by material size

### Activities

**Study Material:**
1. Read through all code/design documentation
2. Understand the design intent and logic flow
3. Follow all execution paths mentally
4. Check all interfaces and interconnections
5. Verify all documentation is complete and consistent

**Review Error History:**
1. Study ranked distributions of error types from recent inspections
2. Focus on high-occurrence error categories
3. Review most costly error types
4. Understand patterns specific to your team/product

**Use Checklists:**
1. Work through appropriate checklist (design or code)
2. Systematically check for each error type
3. Note potential errors or questions
4. Mark areas requiring team discussion

**Document Findings:**
1. Note line numbers of potential errors
2. Write down questions for inspection meeting
3. Flag areas of confusion or ambiguity
4. Do NOT attempt to fix errors

### Preparation Quality Indicators

**Good preparation:**
- Found several potential issues
- Have specific questions about logic or interfaces
- Understand overall flow and intent
- Ready to contribute in inspection meeting

**Insufficient preparation:**
- Haven't read all material
- Don't understand design intent
- Haven't used checklists
- "Looks fine to me" attitude

### Critical Rules
- **Never skip preparation** - meeting effectiveness depends on it
- **Work individually** - no group preparation
- **Don't fix errors** - just identify and note them
- **Study error patterns** - focus preparation on likely issues

### Outputs
- Personally understood material
- List of potential errors and questions
- Readiness for productive inspection meeting

---

## Operation 3: Inspection Meeting

### Objective
**Find errors ONLY.** No fixing, no design debates, no solution hunting.

### Critical Parameters
- **Maximum duration**: 2 hours per session
- **Maximum sessions per day**: 2 (with recovery time between)
- **Coverage rate**: 130 LOC/hour (design), 150 LOC/hour (code)
- **Team size**: 4 people (optimal)

### Participants
- **Moderator** (manages meeting)
- **Designer** (created the design)
- **Implementor/Coder** (reader role)
- **Tester** (testability perspective)

### Meeting Structure

**Opening (5 minutes):**
- Moderator confirms all participants prepared
- Quick review of inspection scope
- Reminder of objective: find errors only
- Review of process and roles

**Main Inspection (110 minutes):**
1. **Reader paraphrases** the logic
   - Implementor explains how they will implement the design
   - Or coder explains how they implemented it
   - Must paraphrase, not just read

2. **Systematic coverage**
   - Every piece of logic covered at least once
   - Every branch taken at least once
   - All documentation verified for completeness

3. **Error identification**
   - Any team member can raise potential error
   - Question pursued ONLY until error is recognized
   - Moderator notes: description, type, severity
   - If solution obvious, note it, but don't require it
   - **NO solution hunting or debugging**

4. **Keep moving**
   - Don't get stuck on any single issue
   - Note the error and move on
   - Maintain steady pace to cover all material

**Closing (5 minutes):**
- Quick review of errors identified
- Confirm all material was covered
- Schedule follow-up timeline
- Set expectations for rework

### Moderator Responsibilities During Meeting

**Process management:**
- Keep team focused on one objective: finding errors
- Ensure reader is paraphrasing, not just reading
- Enforce 2-hour time limit strictly
- Maintain coverage of all material

**Error documentation:**
- Write clear description of each error
- Classify by type (LO, IC, TB, DE, etc.)
- Mark severity (Major or Minor)
- Note location (line number, module, function)
- Record any obvious solutions (but don't require them)

**Team management:**
- Prevent solution hunting
- Stop design alternative debates
- Keep questions focused on error identification
- Use tact and sensitivity to maintain positive atmosphere
- Ensure all team members can contribute

### Coverage Requirements

**Must cover:**
- Every line of code/design
- Every branch (if/else, switch cases)
- Every loop entry and exit
- All error handling paths
- All interface calls
- All data structure usage

**Must have present:**
- All design documentation
- Higher-level specifications
- Interface definitions
- Macro and control block listings (for code inspection)
- Standards documents

### Time Management

**Why 2-hour limit:**
- Error detection efficiency dwindles after 2 hours
- Team fatigue reduces effectiveness
- Diminishing returns on time invested

**If material won't fit in 2 hours:**
- Split into multiple sessions (same or different days)
- Allow recovery time between sessions
- Prioritize critical sections if necessary

### Outputs
- Comprehensive list of errors found
- Each error classified (type, category, severity)
- Coverage confirmation (all material inspected)
- Estimated rework effort
- Moderator notes for report

---

## Operation 4: Rework

### Objective
Fix all problems identified during inspection.

### Participants
- **Design inspection**: Designer
- **Code inspection**: Coder/Implementor
- Individual work

### Duration
- Design (I₁): ~20 hours per thousand lines
- Code (I₂): ~16 hours per thousand lines
- Varies by error count and complexity

### Activities

**For each error identified:**
1. Understand the error fully
2. Determine root cause
3. Design and implement fix
4. Verify fix doesn't introduce new errors
5. Check impact on related code/design
6. Update documentation if needed

**Quality checks:**
- Ensure fix addresses root cause, not just symptom
- Verify no side effects introduced
- Check all related areas for similar errors
- Update test cases if needed
- Document any design changes

### Critical Rules
- **All errors must be fixed** - no exceptions
- **No new errors** - "bad fixes" are common, be careful
- **Complete within timeline** - rework delays affect schedule
- **Document changes** - for follow-up verification

### Common Rework Pitfalls

**Bad fixes:**
- Fixing symptom instead of root cause
- Introducing new errors while fixing old ones
- Not considering side effects
- Incomplete fixes

**Process issues:**
- Delaying rework until later
- Skipping "minor" errors
- Not tracking completion
- Poor communication with moderator

### Outputs
- All identified errors resolved
- Updated code/design
- Documentation of changes made
- Readiness for follow-up

---

## Operation 5: Follow-Up

### Objective
Ensure all fixes are correctly installed and complete before proceeding.

### Participants
- **Moderator** (leads)
- **Author** (available for questions)
- Optional: Full team if reinspection needed

### Moderator Activities

**Verification:**
1. Review list of all errors from inspection
2. Check that each error has been addressed
3. Verify fix is correct and complete
4. Ensure no new errors introduced
5. Confirm documentation updated

**Decision making:**
- Calculate percentage of material reworked
- If **>5% reworked**: Schedule full reinspection (mandatory)
- If **<5% reworked**: Moderator's discretion
  - Option A: Moderator personally verifies all fixes
  - Option B: Reconvene team for partial reinspection
  - Option C: Spot-check critical fixes

**Reporting:**
1. Update inspection report with rework results
2. Document reinspection decision and rationale
3. Obtain signatures (designer, programmer, team leader, moderator)
4. File report for metrics and process improvement
5. Communicate completion to stakeholders

### Reinspection Criteria

**Full reinspection required if ANY:**
- More than 5% of material reworked
- Major structural changes made
- New functionality added during rework
- Moderator has concerns about fix quality
- Author requests reinspection

**Reinspection process:**
- Treat as new inspection (may skip overview)
- Focus on reworked areas plus surrounding context
- Use full inspection meeting process
- Document as continuation of original inspection

### Exit Criteria Verification

**Before signing off, confirm:**
- All errors from inspection list resolved
- All rework verified correct
- No new errors introduced
- Documentation complete and accurate
- All higher-level documents updated
- Reinspection completed if required

**Critical rule:**
All known errors up to this checkpoint must be correctly fixed before claiming checkpoint is met.

### Outputs
- Completed inspection report with signatures
- Verification of all fixes
- Reinspection scheduled (if needed)
- Exit criteria met confirmation
- Metrics data recorded

---

## Inspection Checkpoints in Development Process

### I₀ - Function Level Inspection
- **Entry**: High-level design/function definition complete
- **Focus**: Overall approach, architecture, interfaces
- **Exit**: Function design approved

### I₁ - Design Inspection
- **Entry**: Design reduced to 3-10 code instructions per design statement
- **Focus**: Detailed logic, control flow, data structures, interfaces
- **Exit**: Design complete and ready for coding

### I₂ - Code Inspection
- **Entry**: First clean compilation
- **Focus**: Implementation correctness, coding standards, testability
- **Exit**: Code ready for unit testing

### I₃ - Unit Test Inspection
- **Entry**: Unit test cases written
- **Focus**: Test coverage, test quality, edge cases
- **Exit**: Tests ready for execution

### Modified Code Inspection
- **Entry**: Any code modification, regardless of size
- **Focus**: Change correctness, regression risk, side effects
- **Exit**: Modification ready for testing
- **Special note**: Error rate in modified code is higher than new code

---

## Metrics Collection During Phases

### During Preparation
- Time spent per person
- Lines of code reviewed

### During Inspection Meeting
- Meeting duration
- Lines of code covered
- Errors found by type
- Errors found by severity
- Participants and roles

### During Rework
- Time spent fixing
- Lines of code changed
- Errors fixed

### During Follow-Up
- Verification time
- Reinspection decision
- Total inspection effort

### Aggregate Metrics
- **Inspection rate**: LOC per hour
- **Error density**: Errors per K.LOC
- **Effort**: Person-hours per K.LOC
- **Effectiveness**: Errors found / Total errors

---

## Process Improvement Feedback

After each inspection:
1. **Analyze error patterns** - which types dominate?
2. **Review checklist effectiveness** - did it find errors?
3. **Assess team performance** - good preparation? good meeting?
4. **Update error distributions** - feed forward to next inspections
5. **Improve checklists** - add new items based on errors found
6. **Train team** - share patterns, techniques, lessons learned

The inspection process creates a continuous improvement loop where each inspection improves the next.
