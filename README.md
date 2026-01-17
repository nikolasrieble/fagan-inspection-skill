# Fagan Inspection Skill

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.0.0-green.svg)](CHANGELOG.md)

Systematic code inspection methodology for finding errors through structured team review. Based on Michael Fagan's formal inspection process (1976).

> Find 60-82% of errors before testing through systematic code review with defined roles, checklists, and metrics.

## Quick Start

**With AI Agents (Claude Code, Cursor, etc.):**
```
"Conduct a Fagan inspection on src/auth/login.js"
```

**For Human Teams:**
See [SKILL.md](SKILL.md) for the complete 5-phase inspection process.

## What This Skill Provides

A proven methodology for systematic error detection through structured inspection:

## Installation

No installation required. This is a pure skill - just load it in your AI agent or follow the human team process.

For generating formal reports:
```bash
cd scripts
python3 inspection_report.py --help
```

## Documentation

| File | Description |
|------|-------------|
| **[SKILL.md](SKILL.md)** | Complete methodology and 5-phase process |
| **[HOW-TO-USE.md](HOW-TO-USE.md)** | Step-by-step instructions for AI and teams |
| **[QUICK-REFERENCE.md](QUICK-REFERENCE.md)** | One-page quick reference card |
| **[AGENTS.md](AGENTS.md)** | Guidance for AI agents using this skill |
| **[references/](references/)** | Checklists, error classifications, roles, phases |
| **[examples/](examples/)** | Sample inspection sessions |

## When to Use

- Critical code reviews (security, payments, data integrity)
- Pre-deployment quality audits
- Design reviews before implementation
- Pull request reviews requiring rigor
- Training teams in systematic review

## Expected Results

When properly executed (based on Fagan 1976 research):
- **60-82%** of errors found before testing
- **38%** fewer errors vs. informal reviews  
- **10-100×** cost savings vs. fixing errors in production
- **20%+** productivity improvement

## License

Apache License 2.0 - See [LICENSE](LICENSE) for details.

## Contributing

Contributions welcome! Please feel free to submit issues or pull requests.

## References

Fagan, M.E. (1976). "Design and Code Inspections to Reduce Errors in Program Development." IBM Systems Journal, 15(3), 182-211.
