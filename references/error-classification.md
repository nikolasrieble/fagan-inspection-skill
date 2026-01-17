# Error Classification System

A systematic taxonomy for classifying errors found during Fagan inspections. Each error is classified by three dimensions: Type, Category, and Severity.

## Three-Dimensional Classification

Every error should be classified as: `TYPE/CATEGORY/SEVERITY`

Example: `LO/M/MAJ` = Logic error, Missing, Major severity

---

## Dimension 1: Error Type

Error types identify the nature of the defect. Track these to understand error patterns and improve development processes.

### LO - Logic
**Definition**: Errors in the logical flow, algorithms, or decision-making

**Examples:**
- Incorrect conditional logic (wrong comparison operator)
- Missing loop termination condition
- Wrong algorithm or calculation
- Incorrect sequence of operations
- Missing state transitions
- Edge case not handled

**Common in:**
- Complex algorithms
- State machines
- Business logic
- Mathematical calculations

### IC - Interconnection
**Definition**: Errors in calls, interfaces, and linkages between modules

**Examples:**
- Wrong number of parameters passed
- Parameters in wrong order
- Wrong parameter types
- Missing parameter validation
- Incorrect return value handling
- Wrong function/method called

**Common in:**
- API integrations
- Module interfaces
- Library usage
- Microservice calls

### IR - Interface/Request
**Definition**: Errors in external requests and interface definitions

**Examples:**
- Incorrect API endpoint
- Wrong HTTP method
- Missing headers or authentication
- Malformed request body
- Incorrect protocol usage

**Common in:**
- REST APIs
- Database queries
- Network protocols
- External service calls

### TB - Test and Branch
**Definition**: Errors in conditional tests and branch logic

**Examples:**
- Testing wrong variable
- Incorrect condition (should be AND not OR)
- Wrong comparison operator (< vs <=)
- Missing null/empty check
- Unreachable branch
- Missing else clause

**Common in:**
- Conditional statements
- Switch/case blocks
- Guard clauses
- Input validation

### DE - Design Error
**Definition**: Fundamental design flaws or misunderstandings

**Examples:**
- Wrong architectural pattern used
- Incorrect data structure choice
- Missing abstraction layer
- Design doesn't meet requirements
- Scalability issue in design

**Common in:**
- Architecture reviews
- Design inspections (I₁)
- System design

### PR - Prologue/Prose
**Definition**: Errors in documentation, comments, or explanatory text

**Examples:**
- Misleading function description
- Outdated documentation
- Missing parameter documentation
- Incorrect examples in comments
- Missing copyright or license

**Common in:**
- Function/method headers
- README files
- API documentation
- Inline comments

### PU - Programming Language Use
**Definition**: Incorrect use of language features or syntax

**Examples:**
- Wrong type cast
- Misuse of language feature
- Incorrect memory management
- Wrong scope or visibility
- Language-specific pitfalls

**Common in:**
- Complex language features
- Newer language versions
- Tricky syntax patterns

### MN - Maintainability
**Definition**: Issues that make code hard to maintain or understand

**Examples:**
- Unclear variable names
- Code duplication
- Magic numbers
- Overly complex structure
- Poor separation of concerns
- Hard-coded values

**Common in:**
- Legacy code updates
- Complex modules
- Growing codebases

### PE - Performance
**Definition**: Efficiency and performance issues

**Examples:**
- Inefficient algorithm (O(n²) where O(n) possible)
- Unnecessary database queries
- Memory leaks
- Resource not released
- Unbounded loops or recursion

**Common in:**
- Data processing
- Database operations
- Resource management
- High-traffic code paths

### CC - Code Comments
**Definition**: Missing, incorrect, or misleading code comments

**Examples:**
- No comments in complex logic
- Comments contradict code
- Outdated comments
- TODO comments never addressed
- Commented-out code left in

**Common in:**
- Complex algorithms
- Business rule implementations
- Maintenance activities

### CU - Control Block Usage
**Definition**: Errors in using control structures or configuration blocks

**Examples:**
- Incorrect configuration values
- Missing initialization
- Wrong control flow structure
- Improper state management

**Common in:**
- Configuration files
- State machines
- Control systems

### DA - Data Area Usage
**Definition**: Errors in data structure usage or data handling

**Examples:**
- Wrong data structure for use case
- Buffer overflow potential
- Incorrect data type
- Missing data validation
- Improper data transformation

**Common in:**
- Data processing
- Buffer management
- Type conversions

### RU - Register Usage
**Definition**: Errors in variable or resource usage (modern: variable scope/lifecycle)

**Examples:**
- Variable not initialized
- Using wrong variable
- Variable scope issue
- Resource lifecycle error
- Register/variable conflict

**Modern interpretation:**
- Variable shadowing
- Unintended closure capture
- Scope leakage

### SU - Storage Usage
**Definition**: Memory or storage-related errors

**Examples:**
- Memory leak
- Buffer overflow
- Stack overflow
- Improper allocation/deallocation
- Excessive memory usage

**Common in:**
- Low-level code
- Resource-intensive operations
- Long-running processes

### ST - Standards
**Definition**: Violations of coding standards or conventions

**Examples:**
- Naming convention violated
- Formatting incorrect
- Missing required structure
- Architecture pattern violated
- Security standard not followed

**Common in:**
- Code reviews
- Standards compliance checks
- Team consistency

### MA - Module Attributes
**Definition**: Issues with module-level properties or characteristics

**Examples:**
- Wrong module visibility
- Missing module metadata
- Incorrect dependencies
- Module too large/complex
- Improper module coupling

**Common in:**
- Architecture reviews
- Module refactoring
- Dependency management

### MD - More Detail Needed
**Definition**: Insufficient detail or clarity

**Examples:**
- Ambiguous requirements
- Incomplete specification
- Missing edge case handling
- Unclear error messages
- Vague variable names

**Common in:**
- Design reviews
- Specification reviews
- Early development stages

### OT - Other
**Definition**: Errors that don't fit other categories

**Examples:**
- Unique or unusual errors
- Tool-specific issues
- Build or deployment errors

**Use sparingly**: If using OT frequently, consider defining a new error type.

---

## Dimension 2: Error Category

Identifies what's wrong with the code/design.

### M - Missing
**Definition**: Required element is absent

**Examples:**
- Missing parameter validation
- Missing error handling
- Missing null check
- Missing documentation
- Missing test case
- Missing function call
- Missing return statement

**Questions to ask:**
- Should something be here that isn't?
- Is there a required element that's absent?
- Are all necessary cases covered?

### W - Wrong
**Definition**: Element present but incorrect

**Examples:**
- Wrong algorithm used
- Wrong variable referenced
- Wrong comparison operator
- Wrong parameter order
- Wrong data type
- Wrong error message

**Questions to ask:**
- Is this the correct implementation?
- Are the right values being used?
- Is the logic correct?

### E - Extra
**Definition**: Unnecessary or superfluous element

**Examples:**
- Dead code
- Unreachable branch
- Redundant calculation
- Duplicate code
- Unnecessary complexity
- Extra parameters

**Questions to ask:**
- Is this code actually needed?
- Could this be simplified?
- Is there duplication here?

---

## Dimension 3: Severity

Indicates the impact of the error.

### MAJ - Major
**Definition**: Error that causes malfunction or prevents attainment of specified results

**Characteristics:**
- Causes incorrect results
- Causes system crash or hang
- Prevents feature from working
- Security vulnerability
- Data corruption or loss
- Performance degradation (significant)

**Examples:**
- Null pointer dereference
- Infinite loop
- SQL injection vulnerability
- Wrong calculation in critical path
- Memory leak in long-running process
- Authentication bypass

**Priority**: Must be fixed before release

### MIN - Minor
**Definition**: Lesser impact; doesn't prevent functionality but should be fixed

**Characteristics:**
- Cosmetic issue
- Minor inconvenience
- Documentation error
- Non-critical standard violation
- Inefficiency in non-critical path
- Poor naming

**Examples:**
- Misleading variable name
- Missing comment
- Code formatting issue
- Inefficient but working algorithm
- Minor logging issue

**Priority**: Should be fixed but doesn't block release

---

## Complete Classification Examples

### Example 1: Missing Null Check
- **Type**: TB (Test and Branch)
- **Category**: M (Missing)
- **Severity**: MAJ (Major - will cause crash)
- **Classification**: `TB/M/MAJ`
- **Description**: "No null check before dereferencing user object at line 45"

### Example 2: Wrong Algorithm
- **Type**: LO (Logic)
- **Category**: W (Wrong)
- **Severity**: MAJ (Major - produces incorrect results)
- **Classification**: `LO/W/MAJ`
- **Description**: "Using bubble sort instead of required quicksort algorithm at line 120, violating performance requirements"

### Example 3: Misleading Comment
- **Type**: CC (Code Comments)
- **Category**: W (Wrong)
- **Severity**: MIN (Minor - doesn't affect functionality)
- **Classification**: `CC/W/MIN`
- **Description**: "Comment at line 67 says 'calculates average' but code calculates median"

### Example 4: Missing Error Handling
- **Type**: LO (Logic)
- **Category**: M (Missing)
- **Severity**: MAJ (Major - unhandled exceptions)
- **Classification**: `LO/M/MAJ`
- **Description**: "No try-catch around database call at line 89; will crash on connection failure"

### Example 5: Dead Code
- **Type**: MN (Maintainability)
- **Category**: E (Extra)
- **Severity**: MIN (Minor - no functional impact)
- **Classification**: `MN/E/MIN`
- **Description**: "Lines 200-215 are unreachable code (after return statement)"

### Example 6: Wrong Parameter Type
- **Type**: IC (Interconnection)
- **Category**: W (Wrong)
- **Severity**: MAJ (Major - type mismatch causes error)
- **Classification**: `IC/W/MAJ`
- **Description**: "Passing string to function expecting integer at line 34"

### Example 7: Missing Documentation
- **Type**: PR (Prologue)
- **Category**: M (Missing)
- **Severity**: MIN (Minor - code works but hard to understand)
- **Classification**: `PR/M/MIN`
- **Description**: "Complex function at line 145 has no header documentation explaining purpose or parameters"

### Example 8: Security Vulnerability
- **Type**: LO (Logic)
- **Category**: M (Missing)
- **Severity**: MAJ (Major - security hole)
- **Classification**: `LO/M/MAJ`
- **Description**: "No input sanitization before SQL query at line 78 (SQL injection risk)"

---

## Using Classifications for Process Improvement

### Track Error Type Distributions

Monitor which types occur most frequently:
- If **LO** is high: Focus on logic training, better design reviews
- If **IC** is high: Focus on interface documentation, integration testing
- If **TB** is high: Emphasize edge case thinking, better test coverage
- If **MN** is high: Improve coding standards, refactoring practices

### Analyze by Category

- High **M (Missing)**: Checklists not being used effectively
- High **W (Wrong)**: Requirements unclear or misunderstood
- High **E (Extra)**: Code bloat, need refactoring discipline

### Prioritize by Severity

- **MAJ** errors: Cannot proceed until fixed
- **MIN** errors: Track as technical debt, fix when practical

### Create Targeted Checklists

If your team consistently has:
- **TB/M** errors: Add checklist items for null checks, boundary conditions
- **IC/W** errors: Add checklist items for parameter verification
- **LO/W** errors: Add checklist items for algorithm verification

### Feed Forward to Future Inspections

Share error distributions with team:
- "Last 3 inspections: 40% of errors were TB/M (missing null checks)"
- "Focus preparation on null checking and boundary conditions"
- Update checklists based on patterns
- Train on common error types

---

## Error Recording Template

For each error found during inspection:

```
Error #: ___
Location: File/Module:_____ Line:_____ Function:_____
Classification: TYPE/CATEGORY/SEVERITY
Description:
[Clear description of what's wrong]

Expected:
[What should be here instead]

Impact:
[What happens if this error is not fixed]

Possible Solution (optional):
[If obvious, note it, but not required]
```

---

## Metrics to Track

### By Error Type
- Errors per type per K.LOC
- Percentage distribution by type
- Trend over time
- Comparison to installation average

### By Severity
- Major vs Minor ratio
- Major errors per K.LOC
- Trend in major errors

### By Category
- Missing vs Wrong vs Extra distribution
- Indicates process gaps

### Combined Analysis
- Most common combinations (e.g., LO/M/MAJ)
- Error-prone modules by type
- Effectiveness of checklists by type

---

## Adapting Classifications for Modern Development

### Web Development Additions
- **API** - API design errors
- **UI** - User interface errors
- **SEC** - Security-specific errors
- **AUTH** - Authentication/authorization errors

### Data Science/ML Additions
- **DQ** - Data quality errors
- **ML** - Model logic errors
- **VAL** - Validation/testing errors

### DevOps/Infrastructure Additions
- **CFG** - Configuration errors
- **DEP** - Deployment errors
- **INF** - Infrastructure errors

Adapt the taxonomy to your domain while maintaining the three-dimensional structure (Type/Category/Severity).
