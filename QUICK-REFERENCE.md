# Fagan Inspection Quick Reference

**Purpose:** One-page quick reference card for Fagan inspection essentials.

**Use this when:** You need a quick reminder of commands, rates, rules, or error classifications during an inspection.

**For complete details:** See SKILL.md, HOW-TO-USE.md, and reference documents.

---

One-page reference for conducting Fagan inspections.

---

## Basic Commands (With Claude)

```bash
# Basic inspection
"Conduct Fagan inspection on src/auth/login.js"

# Design review (before coding)
"Conduct Fagan I₁ design inspection on [design-doc]"

# Code review (after compilation)
"Conduct Fagan I₂ code inspection on src/payment/process.py"

# Pull request review
"Review PR #123 using Fagan inspection"

# Re-inspection after fixes
"Re-inspect src/auth/login.js after fixes"

# Focus on specific concerns
"Fagan inspection on database.js focusing on security and error handling"
```

---

## The 5-Phase Process

| Phase | Who | Duration | Key Activity | Output |
|-------|-----|----------|--------------|--------|
| **1. Overview** | Team | Variable | Designer presents material | Shared understanding |
| **2. Preparation** | Individual | 1-2 days | Study material, use checklists | Notes on potential errors |
| **3. Inspection** | Team | 2 hours max | Find errors ONLY | Error list |
| **4. Rework** | Author | Varies | Fix all errors | Corrected code |
| **5. Follow-up** | Moderator | Hours | Verify fixes | Sign-off or reinspection |

---

## Inspection Types

| Type | When | Entry Criteria | Focus |
|------|------|----------------|-------|
| **I₀** | Function design | High-level design done | Architecture, approach |
| **I₁** | Detailed design | Design = 3-10 code instructions per statement | Logic, interfaces, data structures |
| **I₂** | Code implementation | First clean compilation | Implementation correctness, standards |
| **I₃** | Test cases | Test cases written | Test coverage, edge cases |
| **Modified** | Bug fixes/changes | Any code change | Regression risk, completeness |

---

## Critical Rules

### ✅ DO

- **Find errors ONLY** - Never mix finding with fixing
- **100% coverage** - Every line, every branch
- **2-hour limit** - Hard stop (schedule continuation if needed)
- **Systematic approach** - Use checklists
- **Paraphrase** - Reader explains in own words
- **Classify errors** - TYPE/CATEGORY/SEVERITY
- **Fix ALL errors** - Before proceeding
- **Reinspect if >5% reworked** - Mandatory

### ❌ DON'T

- **Solution hunt** - Note error and move on
- **Design debate** - Not the objective
- **Skip sections** - Even "obvious" code needs review
- **Exceed time limit** - Efficiency drops after 2 hours
- **Proceed with errors** - All must be fixed
- **Use for performance review** - Data is for improvement only

---

## Error Classification: TYPE/CATEGORY/SEVERITY

### Types (18 total)

| Code | Type | Common Issues |
|------|------|---------------|
| **LO** | Logic | Wrong algorithm, missing edge case |
| **TB** | Test/Branch | Missing null check, wrong comparison |
| **IC** | Interconnection | Wrong parameters, incorrect API call |
| **IR** | Interface/Request | Wrong endpoint, missing headers |
| **DE** | Design Error | Wrong architecture, bad data structure |
| **PR** | Prologue/Prose | Missing/wrong documentation |
| **CC** | Code Comments | Misleading/outdated comments |
| **MN** | Maintainability | Magic numbers, unclear names |
| **PE** | Performance | Inefficient algorithm, memory leak |
| **DA** | Data Area | Buffer overflow, wrong data type |
| **SU** | Storage Usage | Memory leak, improper allocation |
| **ST** | Standards | Violates coding standards |

**Full list:** See references/error-classification.md

### Categories

- **M** = Missing (required element absent)
- **W** = Wrong (element present but incorrect)  
- **E** = Extra (unnecessary element)

### Severities

- **MAJ** = Major (causes malfunction, must fix)
- **MIN** = Minor (should fix, not blocking)

### Example Classifications

```
LO/M/MAJ = Logic error, Missing, Major
  "No error handling for database failure"

TB/M/MAJ = Test/Branch, Missing, Major
  "Missing null check before user.email access"

IC/W/MAJ = Interconnection, Wrong, Major
  "Wrong parameter type passed to API"

CC/W/MIN = Code Comment, Wrong, Minor
  "Comment says 'hash' but code compares hash"
```

---

## Inspection Rates

| Activity | Rate | Notes |
|----------|------|-------|
| Preparation | 100-125 LOC/hour | Individual study |
| Design Inspection | 130 LOC/hour | Team meeting |
| Code Inspection | 150 LOC/hour | Team meeting |
| Overview | 500 LOC/hour | High-level presentation |

---

## Team Roles (4 People Optimal)

| Role | Responsibility | Key Skills |
|------|----------------|------------|
| **Moderator** | Manage process, note errors, verify fixes | Process discipline, tact |
| **Designer** | Created design/architecture | Deep understanding of design |
| **Coder/Reader** | Paraphrases implementation | Implementation knowledge |
| **Tester** | Testability perspective | Quality mindset, edge cases |

**Critical:** Moderator should be from **unrelated project** (objectivity)

---

## Reinspection Criteria

**Full reinspection REQUIRED if:**
- >5% of material reworked
- Major structural changes made  
- Moderator has concerns about fix quality
- Author requests it

**Moderator discretion if:**
- <5% of material reworked
- Simple, localized fixes
- High confidence in fix quality

---

## When to Use Fagan

### ✅ Use For

- Critical code (security, payments, data integrity)
- Major architectural changes
- Pre-deployment reviews
- High-risk modifications
- Establishing quality standards
- Training teams in systematic review

### ❌ Don't Use For

- Trivial changes (typos, formatting)
- Emergency hotfixes (inspect after)
- Throwaway prototypes
- Personal learning projects
- When overhead exceeds benefit

---

## Checklist Categories

### Design Inspection (I₁)

- Logic Missing/Wrong
- Interface Missing/Wrong
- Design Errors
- Documentation Missing/Wrong

### Code Inspection (I₂)

- Test and Branch (conditionals, null checks)
- Interconnection/Calls (parameters, API usage)
- Logic Implementation
- Data Usage (initialization, bounds)
- Resource Management (memory, files)
- Code Comments
- Standards Compliance
- Performance
- Security

### Modified Code

- Change Completeness
- Regression Risk
- Fix Correctness
- Test Coverage

**Full checklists:** See references/checklists.md

---

## Common Error Patterns

1. **Missing null/undefined checks** (TB/M/MAJ)
2. **Missing error handling** (LO/M/MAJ)
3. **Wrong comparison operators** (TB/W/MAJ)
4. **Parameter type mismatches** (IC/W/MAJ)
5. **Missing input validation** (LO/M/MAJ)
6. **Resource leaks** (SU/M/MAJ)
7. **Off-by-one errors** (LO/W/MAJ)
8. **Misleading comments** (CC/W/MIN)
9. **Magic numbers** (MN/W/MIN)
10. **Dead code** (MN/E/MIN)

---

## Expected Results (From Research)

**When properly executed:**
- 60-82% error detection efficiency
- 38% fewer errors vs. informal reviews
- 20%+ productivity improvement  
- 10-100× cost savings vs. late-stage fixes

---

## Scripts and Tools

```bash
# Interactive report generation
cd skills/fagan-code-review/scripts
python3 inspection_report.py --interactive

# Generate from JSON file
python3 inspection_report.py --from-file errors.json --output-dir ./reports

# Generate specific report type
python3 inspection_report.py --from-file errors.json --report-type summary
```

**Report types:**
- `error-list` - Detailed error descriptions
- `module-detail` - Error statistics  
- `summary` - Inspection summary with sign-off
- `json` - Machine-readable data
- `all` - Generate all reports (default)

---

## One-Minute Inspection Checklist

Before calling inspection complete:

- [ ] Every line covered? (not "looks fine")
- [ ] Every branch taken? (if/else, switch, loops)
- [ ] All null/undefined checks present?
- [ ] All errors handled?
- [ ] All parameters validated?
- [ ] All resources released?
- [ ] All security concerns addressed?
- [ ] All major errors classified?
- [ ] Reinspection decision made?
- [ ] All errors must be fixed?

---

## Getting Help

- **Process details:** See references/inspection-phases.md
- **Role responsibilities:** See references/roles-responsibilities.md  
- **Error taxonomy:** See references/error-classification.md
- **Detailed checklists:** See references/checklists.md
- **Usage guide:** See HOW-TO-USE.md
- **Example session:** See examples/sample-inspection-session.md

---

## Key Insight from Fagan (1976)

> "The cost of fixing a defect increases by 10-100× as it moves through the 
> development cycle. Find errors as close to their origin as possible."

**Implication:** Invest time in systematic inspection early. It's always cheaper than debugging in production.

---

**Ready to start?** 

With Claude: `"Conduct Fagan inspection on [your-file]"`

With team: Schedule 2-hour meeting, distribute materials 1-2 days ahead, use checklists during preparation.
