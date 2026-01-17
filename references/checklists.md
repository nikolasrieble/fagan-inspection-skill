# Inspection Checklists

Systematic prompts for finding common error types during Fagan inspections. Use these during preparation and inspection meetings to ensure thorough coverage.

---

## How to Use These Checklists

### During Preparation (Individual)
1. Work through the appropriate checklist systematically
2. For each item, check the code/design specifically
3. Note potential errors with line numbers
4. Bring notes to inspection meeting

### During Inspection Meeting (Team)
1. Reader paraphrases the logic
2. Team members apply checklist mentally
3. Raise questions when checklist item reveals issue
4. Moderator notes errors found

### Continuous Improvement
- Add items based on errors your team commonly makes
- Remove items that never find errors
- Prioritize items that find high-severity errors
- Share effective items across teams

---

## Design Inspection (I₁) Checklist

Use when inspecting design before coding begins.

### Logic - Missing (LO/M)

**Constants and Values:**
- [ ] Are all constants explicitly defined?
- [ ] Are all unique values explicitly tested on input parameters?
- [ ] Are all default values explicitly tested?
- [ ] Are all magic numbers explained and justified?

**Data and Storage:**
- [ ] Are values stored after they are calculated?
- [ ] Are all variables initialized before use?
- [ ] If character strings created, are they complete? All delimiters shown?
- [ ] Are all increment counts properly initialized (0 or 1)?

**Control Flow:**
- [ ] Are all loop termination conditions defined?
- [ ] Are all state transitions specified?
- [ ] Are all error paths defined?
- [ ] Are all exceptional conditions handled?

**Concurrency and Resources:**
- [ ] If queue manipulated, can execution be interrupted? Is queue protected?
- [ ] Are registers being restored on exits?
- [ ] Should any registers be saved on entry?
- [ ] Are queues being held in isolation?
- [ ] In queuing/dequeuing, should any value be decremented/incremented?

**Interface and Integration:**
- [ ] Are all required parameters listed?
- [ ] Are all return values specified?
- [ ] Are all error codes defined?
- [ ] Are all callbacks or hooks specified?

**Testing and Keywords:**
- [ ] Are all keywords tested in macro?
- [ ] Are all branches reachable?
- [ ] Are all conditions testable?

### Logic - Wrong (LO/W)

**Data Types and Representation:**
- [ ] Are absolutes shown where there should be symbolics?
- [ ] On comparison of two bytes, should all bits be compared?
- [ ] On built data strings, should they be character or hex?
- [ ] Are correct data types used for each purpose?

**Naming and Clarity:**
- [ ] Are internal variables unique or confusing if concatenated?
- [ ] Are similar-sounding variables actually different?
- [ ] Do variable names accurately represent their purpose?

**Algorithms and Logic:**
- [ ] Is the correct algorithm being used?
- [ ] Are loop bounds correct?
- [ ] Is the order of operations correct?
- [ ] Are formulas and calculations accurate?

### Interface - Missing (IC/M)

- [ ] Are all required interface parameters defined?
- [ ] Are all shared data structures documented?
- [ ] Are all side effects documented?
- [ ] Are all assumptions about caller documented?
- [ ] Are all error conditions returnable defined?

### Interface - Wrong (IC/W)

- [ ] Are parameter types correctly specified?
- [ ] Is parameter order logical and consistent?
- [ ] Are return types appropriate for all cases?
- [ ] Are interface contracts clear and correct?

### Design Error (DE/M or DE/W)

- [ ] Does design meet all requirements?
- [ ] Are all use cases covered?
- [ ] Is the chosen architecture appropriate?
- [ ] Are all non-functional requirements addressed (performance, security, etc.)?
- [ ] Is the design maintainable and extensible?
- [ ] Are design patterns applied correctly?

### Documentation - Missing (PR/M)

- [ ] Is the design rationale documented?
- [ ] Are all assumptions documented?
- [ ] Are all constraints documented?
- [ ] Are all dependencies documented?
- [ ] Are all algorithms explained?

### Documentation - Wrong (PR/W)

- [ ] Does documentation match the design?
- [ ] Are examples accurate?
- [ ] Are diagrams consistent with text?
- [ ] Are references up to date?

---

## Code Inspection (I₂) Checklist

Use when inspecting implementation after first clean compilation.

### Test and Branch (TB)

**Conditional Logic:**
- [ ] Is correct condition tested? (IF X=ON vs. IF X=OFF)
- [ ] Is the correct variable used for test?
- [ ] Is the correct comparison operator used? (==, !=, <, <=, >, >=)
- [ ] Are compound conditions correct? (AND vs. OR)
- [ ] Is operator precedence handled correctly?

**Branch Coverage:**
- [ ] Are null THENs/ELSEs included as appropriate?
- [ ] Is each branch target correct?
- [ ] Are all cases in switch/match covered?
- [ ] Is there a default case where needed?
- [ ] Is most frequently exercised test leg the THEN clause? (performance)

**Null and Boundary Checks:**
- [ ] Are null/undefined checks present before use?
- [ ] Are empty collection checks present?
- [ ] Are boundary conditions tested? (0, 1, max, max-1, max+1)
- [ ] Are off-by-one errors avoided?
- [ ] Are negative number cases handled?

**Error Conditions:**
- [ ] Are all error conditions tested for?
- [ ] Are error returns handled correctly?
- [ ] Are exceptions caught appropriately?
- [ ] Are error messages clear and helpful?

### Interconnection/Calls (IC)

**Parameter Passing:**
- [ ] Are all required parameters passed?
- [ ] Are parameters in correct order?
- [ ] Are parameter types correct?
- [ ] Are parameter values within expected ranges?
- [ ] If register parameters used, is correct register number specified?

**Return Value Handling:**
- [ ] If interconnection returns, are all returned parameters processed?
- [ ] Are return values checked for errors?
- [ ] Is return value type correct?
- [ ] Is null return value possible and handled?

**Macro and Inline:**
- [ ] If macro, does inline expansion contain all required code?
- [ ] Are there register or storage conflicts between macro and calling module?
- [ ] Are macro parameters properly escaped/scoped?

**API Usage:**
- [ ] Is the correct API/function being called?
- [ ] Is the API being used as documented?
- [ ] Are all required setup steps completed?
- [ ] Are all cleanup steps included?

### Logic Implementation (LO)

**Algorithm Correctness:**
- [ ] Does implementation match design?
- [ ] Are calculations performed correctly?
- [ ] Is order of operations correct?
- [ ] Are type conversions handled properly?

**Loop Implementation:**
- [ ] Are loop initialization, condition, and increment correct?
- [ ] Can loops terminate properly?
- [ ] Are loop variables modified correctly?
- [ ] Are nested loops handled properly?

**State Management:**
- [ ] Is state initialized correctly?
- [ ] Are state transitions implemented as designed?
- [ ] Is state cleanup performed?
- [ ] Are race conditions avoided?

### Data Usage (DA)

**Initialization:**
- [ ] Are all variables initialized before use?
- [ ] Are arrays initialized to correct size?
- [ ] Are pointers initialized to null or valid address?
- [ ] Are objects constructed properly?

**Bounds and Size:**
- [ ] Are array bounds checked?
- [ ] Can buffer overflows occur?
- [ ] Are string operations null-terminated?
- [ ] Are collection sizes validated?

**Type Safety:**
- [ ] Are type casts safe and necessary?
- [ ] Are implicit conversions handled correctly?
- [ ] Are bit operations on correct types?
- [ ] Are signed/unsigned issues avoided?

### Resource Management (SU/RU)

**Allocation and Deallocation:**
- [ ] Is memory allocated and freed properly?
- [ ] Are files opened and closed?
- [ ] Are database connections managed?
- [ ] Are network sockets closed?

**Resource Lifecycle:**
- [ ] Are resources released in all code paths?
- [ ] Are resources released in error paths?
- [ ] Are resources released in exception handlers?
- [ ] Can resource leaks occur?

**Lifetime and Scope:**
- [ ] Are object lifetimes managed correctly?
- [ ] Are variables properly scoped?
- [ ] Are closures capturing correct values?
- [ ] Are static variables used appropriately?

### Code Comments (CC)

**Presence:**
- [ ] Is complex logic commented?
- [ ] Are non-obvious decisions explained?
- [ ] Are workarounds documented?
- [ ] Are TODOs tracked and resolved?

**Accuracy:**
- [ ] Do comments match the code?
- [ ] Are examples in comments correct?
- [ ] Are outdated comments updated?

**Quality:**
- [ ] Do comments explain WHY, not WHAT?
- [ ] Are comments clear and concise?
- [ ] Is commented-out code removed?

### Standards Compliance (ST)

**Naming Conventions:**
- [ ] Do names follow team standards?
- [ ] Are names clear and descriptive?
- [ ] Are abbreviations standard?
- [ ] Are naming patterns consistent?

**Code Style:**
- [ ] Is indentation consistent?
- [ ] Is formatting standard?
- [ ] Are line lengths appropriate?
- [ ] Is file organization standard?

**Best Practices:**
- [ ] Are language idioms used correctly?
- [ ] Are framework patterns followed?
- [ ] Are security best practices applied?
- [ ] Are performance guidelines followed?

### Performance (PE)

**Algorithmic Efficiency:**
- [ ] Is the algorithm efficient for expected data size?
- [ ] Are nested loops necessary?
- [ ] Can operations be cached or memoized?
- [ ] Are database queries optimized?

**Resource Usage:**
- [ ] Is memory usage reasonable?
- [ ] Are large objects copied unnecessarily?
- [ ] Are string concatenations efficient?
- [ ] Are collections pre-sized appropriately?

### Security and Safety

**Input Validation:**
- [ ] Are all inputs validated?
- [ ] Are inputs sanitized before use?
- [ ] Are injection attacks prevented? (SQL, XSS, etc.)
- [ ] Are file paths validated?

**Authentication and Authorization:**
- [ ] Are authentication checks present?
- [ ] Are authorization checks correct?
- [ ] Are credentials never hardcoded?
- [ ] Are secrets managed securely?

**Data Protection:**
- [ ] Is sensitive data encrypted?
- [ ] Are secrets not logged?
- [ ] Is PII handled appropriately?
- [ ] Are data retention requirements met?

---

## Modified Code Inspection Checklist

Use when inspecting changes, fixes, or modifications.

### Change Scope

- [ ] Is the modification complete?
- [ ] Are all necessary files updated?
- [ ] Is documentation updated?
- [ ] Are tests updated?

### Change Correctness

- [ ] Does the change fix the intended issue?
- [ ] Does the change address root cause, not symptom?
- [ ] Are related issues also addressed?
- [ ] Is the fix minimal and focused?

### Regression Risk

- [ ] Could this change affect other functionality?
- [ ] Are there side effects in related code?
- [ ] Are all callers still compatible?
- [ ] Are database schemas compatible?
- [ ] Are API contracts maintained?

### Testing

- [ ] Do existing tests still pass?
- [ ] Are new tests added for the change?
- [ ] Are edge cases tested?
- [ ] Is rollback tested?

### Special Attention Areas

**Small Changes (1-25 lines):**
- [ ] Don't assume "too small to have errors"
- [ ] Check surrounding context carefully
- [ ] Verify off-by-one errors
- [ ] Check for typos

**Bug Fixes:**
- [ ] Does fix introduce new bugs?
- [ ] Are similar bugs in other places?
- [ ] Is the fix properly tested?
- [ ] Is root cause addressed?

---

## Language-Specific Checklists

### JavaScript/TypeScript

**Type Safety:**
- [ ] Are types declared correctly?
- [ ] Are type assertions safe?
- [ ] Are null/undefined handled?
- [ ] Is strict mode enabled?

**Async Operations:**
- [ ] Are promises handled correctly?
- [ ] Are async/await used properly?
- [ ] Are errors in async code caught?
- [ ] Are race conditions avoided?

**Common Pitfalls:**
- [ ] Is `this` binding correct?
- [ ] Are closures capturing correct values?
- [ ] Is equality comparison correct (=== vs ==)?
- [ ] Are truthy/falsy values handled correctly?

### Python

**Type and None Handling:**
- [ ] Are None checks present?
- [ ] Are type hints accurate?
- [ ] Are duck-typing assumptions safe?

**Resource Management:**
- [ ] Are context managers used (with statements)?
- [ ] Are files closed properly?
- [ ] Are exceptions handled?

**Common Pitfalls:**
- [ ] Are mutable default arguments avoided?
- [ ] Is integer division handled correctly?
- [ ] Are list comprehensions readable?
- [ ] Is variable scope clear (global, nonlocal)?

### Java

**Exception Handling:**
- [ ] Are checked exceptions handled?
- [ ] Are resources auto-closed (try-with-resources)?
- [ ] Are custom exceptions meaningful?

**Null Safety:**
- [ ] Are null checks present?
- [ ] Is Optional used appropriately?
- [ ] Are NullPointerExceptions prevented?

**Concurrency:**
- [ ] Is thread safety handled?
- [ ] Are collections thread-safe when needed?
- [ ] Are race conditions avoided?
- [ ] Is synchronization correct?

### C/C++

**Memory Management:**
- [ ] Is memory allocated and freed correctly?
- [ ] Are pointers checked before dereferencing?
- [ ] Is delete/free called exactly once per allocation?
- [ ] Are smart pointers used appropriately (C++)?

**Buffer Safety:**
- [ ] Are buffer sizes checked?
- [ ] Are string operations safe?
- [ ] Is array indexing bounded?

**Common Pitfalls:**
- [ ] Are pointers initialized?
- [ ] Is use-after-free avoided?
- [ ] Is the correct delete used (delete vs delete[])?
- [ ] Are copy constructors/assignment operators correct?

---

## Creating Custom Checklists

### For Your Team

1. **Analyze error patterns** from past inspections
2. **Identify frequent error types** (top 5-10)
3. **Create specific checklist items** for each
4. **Test effectiveness** in next inspection
5. **Refine based on results**

### For Your Domain

**Web Applications:**
- CSRF protection present?
- XSS prevention implemented?
- Input validation complete?
- Authentication on all protected routes?

**Data Processing:**
- Schema validation present?
- Data type conversions safe?
- Large dataset handling efficient?
- Data pipeline error handling?

**APIs:**
- All endpoints documented?
- Rate limiting implemented?
- Error responses standardized?
- Versioning handled?

### Checklist Best Practices

**Effective checklist items:**
- ✅ Specific and concrete
- ✅ Based on actual errors found
- ✅ Easy to verify yes/no
- ✅ Find high-severity issues

**Ineffective checklist items:**
- ❌ Too vague or general
- ❌ Theoretical issues never seen
- ❌ Require deep analysis to check
- ❌ Rarely find actual errors

---

## Checklist Usage Tips

### Don't Be Mechanical
- Use checklists as prompts, not rigid scripts
- Think about the intent behind each item
- Adapt items to specific code being reviewed

### Focus on High-Value Items
- Prioritize items that find major errors
- Skip items not applicable to current code
- Add custom items for specific modules

### Update Regularly
- Add items when new error patterns emerge
- Remove items that never find errors
- Share effective items across team

### Combine with Paraphrasing
- Reader paraphrases implementation
- Team applies checklist mentally
- Questions reveal errors
- Synergistic effect finds more than either alone

---

## Preparation Checklist

Before you begin inspection, ensure:

- [ ] All materials received 1-2 days before inspection
- [ ] Time allocated for preparation (100-125 LOC/hour)
- [ ] Appropriate checklist selected (design vs code)
- [ ] Recent error distributions reviewed
- [ ] Questions and potential errors noted
- [ ] Ready to contribute in inspection meeting

---

Remember: The goal is not to check every box, but to systematically examine the code to find errors. Use checklists as a tool to guide thorough inspection, not as a substitute for thinking.
