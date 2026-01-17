# How to Use the Fagan Code Review Skill

Step-by-step instructions for conducting Fagan inspections with Claude Code (AI-assisted) or human teams.

## Table of Contents

1. [Using with Claude Code (AI-Assisted)](#using-with-claude-code-ai-assisted)
2. [Using with Human Teams](#using-with-human-teams)
3. [Common Use Cases with Examples](#common-use-cases-with-examples)
4. [Quick Reference Commands](#quick-reference-commands)

---

## Using with Claude Code (AI-Assisted)

### Basic Usage Pattern

Simply ask Claude to conduct a Fagan inspection on your code:

```
"Conduct a Fagan inspection on src/auth/login.js"
```

Claude will:
1. Load the skill automatically
2. Read the file and surrounding context
3. Apply appropriate checklists
4. Report errors with classifications

### Inspection Types

#### **I₁ - Design Inspection** (Before Coding)

**When:** You have a design document or detailed plan but haven't coded yet

```
"I've designed a new caching layer. Here's the design:
[paste design or architecture description]

Please conduct a Fagan I₁ design inspection."
```

**What Claude will check:**
- Logic completeness (missing edge cases, state transitions)
- Interface design (parameters, return values, error handling)
- Design errors (wrong architecture, incorrect algorithms)
- Documentation accuracy

**Example output:**
```
Error #1: LO/M/MAJ - Missing cache eviction policy design
Location: Cache Design Section 3
Description: No specification for what happens when cache is full

Error #2: IC/W/MIN - Inconsistent parameter naming
Location: CacheInterface.get() vs CacheInterface.set()
Description: get() uses 'key' but set() uses 'cacheKey'
```

---

#### **I₂ - Code Inspection** (After First Compile)

**When:** You've written code that compiles/runs but want systematic review

```
"Conduct a Fagan I₂ code inspection on src/payment/processor.py"
```

**What Claude will check:**
- Test and branch errors (null checks, conditionals, loops)
- Interconnection errors (parameter passing, API calls)
- Logic implementation (algorithm correctness)
- Resource management (memory leaks, file handles)
- Security issues (input validation, injection risks)

**Example output:**
```
Error #1: TB/M/MAJ - Missing null check at processor.py:45
Location: processor.py:45
Description: user.payment_method accessed without null check
Impact: NullPointerException if user has no payment method

Error #2: LO/W/MAJ - Wrong algorithm for discount calculation
Location: processor.py:78
Description: Using simple percentage instead of tiered discount structure
```

---

#### **Modified Code Inspection** (For Bug Fixes/Changes)

**When:** Reviewing changes, bug fixes, or pull requests

```
"Conduct a Fagan modified code inspection on my recent changes to auth.js"
```

Or with a PR:
```
"Review PR #123 using Fagan inspection"
```

**What Claude will check:**
- Change completeness (all necessary files updated)
- Regression risk (side effects, breaking changes)
- Fix correctness (root cause addressed)
- Test coverage (new tests added)

---

### Specifying Detail Level

**Quick Scan:**
```
"Do a quick Fagan inspection focusing on security issues in login.js"
```

**Comprehensive Review:**
```
"Conduct a thorough Fagan I₂ inspection on the entire auth/ directory.
Be very detailed and check every error type."
```

**Focus Areas:**
```
"Fagan inspection on database.py focusing on:
- SQL injection risks
- Connection pooling
- Error handling"
```

---

### Working with Inspection Reports

**Generate Full Report:**
```
"Conduct Fagan inspection on payment.py and generate a formal report"
```

Claude will use `scripts/inspection_report.py` to create:
- Error list with classifications
- Module detail report (error counts by type)
- Summary with metrics

**Review Fixes:**
```
"I've fixed the errors from the last inspection. Re-inspect payment.py"
```

---

## Using with Human Teams

### Step-by-Step Team Process

#### **1. Planning (Moderator)**

**Before scheduling:**
- Verify code/design meets entry criteria
  - **I₁**: Design complete to 3-10 code instructions per statement
  - **I₂**: Code has first clean compilation
- Identify team members for each role:
  - Moderator (from unrelated project ideally)
  - Designer (design author)
  - Coder/Implementor (will/did implement)
  - Tester (responsible for testing)

**Schedule meeting:**
```
Meeting: Code Inspection - Authentication Module
Duration: 2 hours maximum
Date: [1-2 days from material distribution]
Participants: 
  - Moderator: Alice
  - Designer: Bob
  - Coder: Carol
  - Tester: Dave
```

**Distribute materials:**
- Code/design to be inspected
- Supporting documentation (specs, architecture)
- Checklists: `references/checklists.md`
- Error classification guide: `references/error-classification.md`

---

#### **2. Preparation (Individual - 1-2 Days Before)**

**Each participant independently:**

1. **Study the material** (100-125 LOC/hour)
   - Read through all code/design
   - Understand logic flow and intent
   - Follow all execution paths

2. **Apply checklists systematically**
   ```
   For code inspection, check:
   [ ] Are null checks present before dereferencing?
   [ ] Are all error conditions handled?
   [ ] Are parameters validated?
   [ ] Are resources properly released?
   [ ] etc.
   ```

3. **Note potential errors**
   ```
   Potential Error #1:
   Location: auth.js:45
   Issue: No null check before user.email access
   Classification: TB/M/MAJ
   ```

4. **Mark questions for discussion**

**DO NOT:**
- Fix errors you find
- Discuss findings with other team members
- Skip "obvious" or "simple" sections

---

#### **3. Inspection Meeting (2 Hours Max)**

**Opening (5 minutes):**
- Moderator confirms everyone prepared
- Review objective: FIND ERRORS ONLY
- Reminder: No fixing, no solution hunting, no design debates

**Main Inspection (110 minutes):**

**The Reader (Coder) paraphrases:**
```
Reader: "In the authenticateUser function, I first check if the 
        username is provided. Then I query the database for the user..."

Team Member: "Wait - what happens if the database is down?"

Reader: "Looking at line 34... there's no try-catch around the query."

Moderator: [Notes error] "IC/M/MAJ - Missing exception handling around 
           database query at line 34. Continue."
```

**Process:**
- Cover EVERY line systematically
- Take EVERY branch (if/else, switch cases)
- When error found:
  1. Recognize it exists
  2. Moderator notes: location, description, classification
  3. MOVE ON (don't discuss solutions)

**Moderator documents each error:**
```
Error #5:
Location: auth.js:67
Type: TB (Test and Branch)
Category: M (Missing)  
Severity: MAJ (Major)
Description: No validation that password field is non-empty
```

**Closing (5 minutes):**
- Quick count of errors found
- Confirm all material was covered
- Set expectations for rework timeline

---

#### **4. Rework (Author - Days After Meeting)**

**Author fixes ALL errors:**

For each error:
1. Understand the root cause
2. Design and implement fix
3. Verify fix doesn't introduce new errors
4. Update tests if needed

**Track progress:**
```
✓ Error #1: Added null check at line 45
✓ Error #2: Added try-catch around database query
✓ Error #3: Added password validation
⚠ Error #4: In progress
```

---

#### **5. Follow-Up (Moderator)**

**Moderator verifies all fixes:**

```bash
# Review the fixed code
# Check each error was properly addressed

# Generate final report
cd scripts
python3 inspection_report.py --from-file inspection_data.json

# Calculate rework percentage
# If >5% reworked → Schedule full reinspection
# If <5% reworked → Moderator's discretion
```

**Sign-off when:**
- All errors resolved
- No new errors introduced
- All documentation updated
- Reinspection completed (if required)

---

## Common Use Cases with Examples

### Use Case 1: Pull Request Review

**Scenario:** Reviewing a pull request for critical code

**Command:**
```
"Review PR #456 using Fagan modified code inspection.
Focus on regression risk and change completeness."
```

**Claude will:**
1. Fetch PR diff
2. Read full context of changed files
3. Apply modified code checklist
4. Report errors with severity

**Follow-up:**
```
"The author has updated the PR. Re-inspect the changes."
```

---

### Use Case 2: Security Audit

**Scenario:** Auditing authentication code for security issues

**Command:**
```
"Conduct a security-focused Fagan inspection on:
- src/auth/login.js
- src/auth/session.js
- src/auth/password.js

Check for:
- SQL injection
- XSS vulnerabilities
- Authentication bypass
- Session management issues
- Input validation"
```

---

### Use Case 3: Pre-Deployment Review

**Scenario:** Final check before deploying payment processing code

**Command:**
```
"Conduct a comprehensive Fagan I₂ inspection on src/payment/*.
This is critical code for production deployment.
Be thorough with error handling, edge cases, and data validation."
```

---

### Use Case 4: Design Review

**Scenario:** Reviewing API design before implementation

**Command:**
```
"I'm designing a new REST API for user management. Here's the design:

[paste OpenAPI spec or design doc]

Conduct a Fagan I₁ design inspection. Check for:
- Missing endpoints or operations
- Inconsistent interface design
- Missing error responses
- Authentication/authorization gaps"
```

---

### Use Case 5: Bug Fix Verification

**Scenario:** Verifying a bug fix is complete and correct

**Command:**
```
"I fixed bug #789 (null pointer in user profile).
Changes in src/profile/UserProfile.java lines 45-67.

Conduct Fagan modified code inspection to verify:
1. Root cause addressed (not just symptom)
2. No new errors introduced
3. All related code updated
4. Similar issues in other places"
```

---

## Quick Reference Commands

### Inspection Requests

```bash
# Basic inspection
"Conduct Fagan inspection on <file>"

# Specify type
"Conduct Fagan I₁ design inspection on <design-doc>"
"Conduct Fagan I₂ code inspection on <file>"

# Pull request
"Review PR #<number> using Fagan inspection"

# Focus areas
"Fagan inspection on <file> focusing on security"
"Fagan inspection on <file> checking error handling"

# Comprehensive
"Thorough Fagan inspection on <directory>/*"
```

### Report Generation

```bash
# With Claude
"Generate a formal Fagan inspection report for <file>"

# Using script directly
cd skills/fagan-code-review/scripts
python3 inspection_report.py --interactive
python3 inspection_report.py --from-file errors.json --output-dir ./reports
```

### Re-inspection

```bash
# After fixes
"Re-inspect <file> after fixes"
"Verify all errors from previous inspection are resolved"

# Partial re-inspection
"Re-inspect only the error handling section of <file>"
```

---

## Loading Reference Materials

During inspection, load these as needed:

```
"Load the Fagan code inspection checklist"
→ Loads references/checklists.md (I₂ section)

"Load the error classification guide"
→ Loads references/error-classification.md

"Load the Fagan roles and responsibilities"
→ Loads references/roles-responsibilities.md

"Load the complete process guide"
→ Loads references/inspection-phases.md
```

---

## Understanding Error Classifications

Every error reported will use this format: `TYPE/CATEGORY/SEVERITY`

**Example:** `LO/M/MAJ`
- **LO** = Logic error
- **M** = Missing (something required is absent)
- **MAJ** = Major severity (causes malfunction)

**Common classifications you'll see:**

```
TB/M/MAJ - Missing null check (Test/Branch, Missing, Major)
IC/W/MAJ - Wrong parameter type (Interconnection, Wrong, Major)
LO/W/MAJ - Wrong algorithm used (Logic, Wrong, Major)
CC/W/MIN - Wrong comment (Code Comment, Wrong, Minor)
MN/E/MIN - Dead code (Maintainability, Extra, Minor)
PR/M/MIN - Missing documentation (Prologue, Missing, Minor)
```

---

## Tips for Effective Use

### With Claude (AI)

**DO:**
- ✅ Be specific about what you want checked
- ✅ Ask for re-inspection after fixes
- ✅ Request focus on critical areas (security, data handling)
- ✅ Ask for formal reports for documentation

**DON'T:**
- ❌ Ask Claude to fix errors during inspection (violates separation)
- ❌ Skip reading the full error descriptions
- ❌ Ignore "minor" errors (they accumulate)

### With Teams

**DO:**
- ✅ Enforce preparation (meeting fails without it)
- ✅ Hard stop at 2 hours (schedule continuation if needed)
- ✅ Focus on finding, not fixing
- ✅ Track metrics to improve over time

**DON'T:**
- ❌ Let meetings become debugging sessions
- ❌ Skip "obvious" sections
- ❌ Use inspection results for performance reviews
- ❌ Proceed without fixing all errors

---

## When NOT to Use Fagan

Skip full Fagan inspection for:
- Single-line trivial changes
- Emergency hotfixes (inspect after)
- Prototype/throwaway code
- Personal learning projects

Use lightweight review instead, or self-inspection with checklists.

---

## Getting Started Checklist

**First time using this skill:**

- [ ] Read SKILL.md for overview
- [ ] Review references/checklists.md for your language
- [ ] Try inspection on small module (100-200 LOC)
- [ ] Note which error types you find most
- [ ] Customize checklist for your team's common errors
- [ ] Track metrics to measure improvement

**For your team:**

- [ ] Train a moderator (brief course on process)
- [ ] Conduct pilot inspection on non-critical code
- [ ] Gather feedback and refine process
- [ ] Integrate into development workflow at checkpoints
- [ ] Review error patterns monthly
- [ ] Update checklists based on actual errors found

---

## Common Questions

**What's the difference between I₁ and I₂?**
- I₁ = Design inspection (before coding)
- I₂ = Code inspection (after first compile)

**How long does an inspection take?**
- Preparation: 1-2 days (background activity)
- Meeting: 2 hours max
- Rework: Varies by error count
- Total: ~3-5 days for formal inspection

**Can I use this for solo development?**
- Yes. Use checklists for self-inspection or ask Claude to act as inspection team.

**What if I find >50 errors?**
- Code isn't ready for inspection. Fix obvious errors first, then return to inspection.

**Should every PR use Fagan?**
- No. Use for critical/high-risk changes. Lightweight review for routine changes.

---

## Example Session

```
You: "Conduct Fagan I₂ code inspection on src/auth/login.ts"

Claude: [Loads skill, reads file and context, applies checklist]

Claude: "I've completed the inspection. Found 8 errors:

Error #1: TB/M/MAJ - Missing null check at login.ts:23
Location: login.ts:23
Description: user.email accessed without checking if user exists
Impact: TypeError if user is null/undefined

Error #2: LO/M/MAJ - Missing rate limiting at login.ts:15
Location: login.ts:15  
Description: No rate limiting on login attempts
Impact: Brute force attacks possible

[... 6 more errors ...]

Summary:
- Total errors: 8
- Major: 5
- Minor: 3
- Most common type: TB (Test/Branch) - 4 errors

Recommendation: Fix all major errors before deployment.
No reinspection needed (estimated <5% rework)."

You: "I've fixed errors #1-#5. Re-inspect please."

Claude: [Verifies fixes, checks for new errors]

Claude: "Fixes verified. All 5 errors properly addressed.
No new errors introduced. Remaining minor errors can be 
addressed in next iteration."
```

---

**Ready to start?** Try: `"Conduct Fagan inspection on [your-file]"`
