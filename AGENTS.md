# Agent Guidance for Fagan Code Review

This document provides guidance for AI agents using the Fagan Code Review skill.

## Skill Overview

The Fagan Code Review skill enables systematic error detection through structured inspection. Agents should use this skill when users request:

- Code reviews with systematic rigor
- Design reviews before implementation
- Pull request reviews
- Quality audits on critical code
- Error pattern analysis

## Core Capabilities

### 1. Code Inspection (I₂)
Inspect implementation after first clean compilation.

**When to use:** User has working code that needs review.

**Process:**
1. Read the file(s) to inspect
2. Apply code inspection checklist systematically
3. Check every line, every branch
4. Classify errors as TYPE/CATEGORY/SEVERITY
5. Report findings with specific locations

### 2. Design Inspection (I₁)
Inspect design before coding begins.

**When to use:** User has design documents or detailed plans.

**Process:**
1. Review design documentation
2. Apply design inspection checklist
3. Check for logic completeness, interface design, missing edge cases
4. Report design errors before code is written

### 3. Modified Code Inspection
Inspect changes, bug fixes, or pull requests.

**When to use:** Reviewing diffs, changes, or PRs.

**Process:**
1. Identify changed files and lines
2. Check change completeness and regression risk
3. Verify fix addresses root cause
4. Report errors specific to the changes

## Error Classification

Every error must be classified as: `TYPE/CATEGORY/SEVERITY`

### Common Classifications
- `TB/M/MAJ` - Missing null check (Test/Branch, Missing, Major)
- `LO/M/MAJ` - Missing error handling (Logic, Missing, Major)
- `IC/W/MAJ` - Wrong parameter type (Interconnection, Wrong, Major)
- `CC/W/MIN` - Wrong comment (Code Comment, Wrong, Minor)

See `references/error-classification.md` for complete taxonomy.

## Checklists

### Always Use Checklists
Load appropriate checklist from `references/checklists.md`:
- Design Inspection (I₁): Design checklist
- Code Inspection (I₂): Code checklist
- Modified Code: Modified code checklist

### Systematic Application
Work through checklist items methodically:
- Null/undefined checks
- Error handling
- Boundary conditions
- Resource management
- Security validation

## Best Practices for Agents

### DO
- ✅ Be systematic - check every line, every branch
- ✅ Use specific line numbers and file paths
- ✅ Classify every error found
- ✅ Focus on finding, not fixing
- ✅ Check security and error handling rigorously
- ✅ Provide clear impact statements for major errors

### DON'T
- ❌ Skip "obvious" or "simple" sections
- ❌ Fix errors during inspection (violates separation of objectives)
- ❌ Assume code is correct without verification
- ❌ Ignore minor errors
- ❌ Provide vague descriptions without line numbers

## Example Workflow

```
User: "Conduct a Fagan inspection on src/auth/login.js"

Agent:
1. Load code inspection checklist (references/checklists.md)
2. Read src/auth/login.js
3. Apply checklist systematically:
   - Check for null/undefined handling
   - Check error handling paths
   - Check security (input validation, injection risks)
   - Check resource management
   - etc.
4. Report errors with classifications:
   Error #1: TB/M/MAJ - Missing null check at login.js:45
   Error #2: LO/M/MAJ - Missing rate limiting at login.js:15
   etc.
5. Provide summary with error counts and reinspection decision
```

## Generating Reports

When user requests formal reports:
1. Collect all error data
2. Use `scripts/inspection_report.py` to generate:
   - Error list report
   - Module detail report
   - Summary report with metrics
   - JSON export

## Re-inspection

After user fixes errors:
1. Re-read the modified code
2. Verify each fix addresses the root cause
3. Check for new errors introduced by fixes
4. Report verification results

## Integration with Development Workflow

### For Pull Requests
- Author = Designer + Implementor
- Apply modified code checklist
- Check regression risk and completeness
- Track error types in review

### For Solo Development
- Act as entire inspection team
- Apply checklists systematically
- Track personal error patterns
- Provide actionable feedback

## Reference Materials

Load these on-demand:
- `references/checklists.md` - Error-finding prompts
- `references/error-classification.md` - Error taxonomy
- `references/roles-responsibilities.md` - Team roles
- `references/inspection-phases.md` - 5-phase process
- `examples/sample-inspection-session.md` - Example inspection

## Success Metrics

Aim for inspection results matching Fagan research:
- 60-82% error detection efficiency
- Clear classification of all errors
- Systematic coverage verified
- Actionable findings with specific locations
