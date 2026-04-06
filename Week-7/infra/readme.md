Here's a proper README documentation for all the errors faced and fixed:

```markdown
# Week 7 — CI/CD Pipeline: Issues & Fixes

## Overview
This document captures all errors encountered while building the CI/CD pipeline and how each was resolved.

---

## Error 1 — Ruff Lint: Unused Imports

### What happened
The `Lint with ruff` step failed in GitHub Actions with exit code 1.

### Error output
```
F401 `time` imported but unused
 --> app/metrics.py:2:8

F401 `werkzeug.security.generate_password_hash` imported but unused
 --> app/models/models.py:3:31

F401 `flask.session` imported but unused
 --> app/routes/auth.py:1:82

F401 `flask_login.current_user` imported but unused
 --> app/routes/auth.py:4:50

F401 `app.models.models.Announcement` imported but unused
 --> tests/test_app.py:7:70
```

### Root cause
Imports were added during development but never used in the code.

### Fix
Removed all unused imports from the respective files.

```python
# metrics.py — removed
import time

# models.py — removed generate_password_hash, kept check_password_hash
from werkzeug.security import generate_password_hash, check_password_hash
# changed to
from werkzeug.security import check_password_hash

# auth.py — removed session and current_user
from flask import ..., session
from flask_login import ..., current_user

# test_app.py — removed Announcement
from app.models.models import User, Student, Attendance, Assignment, Announcement
# changed to
from app.models.models import User, Student, Attendance, Assignment
```

---

## Error 2 — Ruff Lint: Unused Variables

### What happened
Ruff flagged variables that were assigned but never used.

### Error output
```
F841 Local variable `total_marked_days` is assigned to but never used
  --> app/routes/routes.py:21:5

F841 Local variable `e` is assigned to but never used
  --> app/routes/routes.py:125:25
  --> app/routes/routes.py:175:29
  --> app/routes/routes.py:208:29

F841 Local variable `today` is assigned to but never used
  --> tests/test_app.py:117:5
```

### Root cause
Variables were assigned during development but never referenced afterward.

### Fix
```python
# Deleted unused variable
total_marked_days = Attendance.query.distinct(Attendance.date).count()

# Changed except blocks from
except Exception as e:
# to
except Exception:

# Deleted unused variable in test_app.py
today = date.today().isoformat()
```

---

## Error 3 — Ruff Lint: Wrong Boolean Comparisons

### What happened
Ruff flagged equality comparisons to `True` and `False` as bad practice.

### Error output
```
E712 Avoid equality comparisons to `False`
  --> app/routes/routes.py:41:9
  --> app/routes/routes.py:221:9

E712 Avoid equality comparisons to `True`
  --> app/routes/routes.py:224:9
```

### Root cause
Using `== False` and `== True` in Python is considered bad style. Ruff enforces PEP 8.

### First fix attempt (wrong)
```python
# Ruff suggested this — works in plain Python but BREAKS SQLAlchemy queries
not Assignment.is_completed
```

### Why it broke the app
`not Assignment.is_completed` is evaluated by Python immediately and returns `True` or `False`. SQLAlchemy never receives it as a filter condition, so **all assignments disappeared** from the UI.

### Final correct fix
```python
# Use SQLAlchemy's .is_() method — satisfies ruff AND works in database queries
Assignment.is_completed.is_(False)   # replaces == False
Assignment.is_completed.is_(True)    # replaces == True
```

---

## Error 4 — Trivy Scan: HIGH Vulnerabilities

### What happened
The `scan the container` step failed because Trivy found HIGH severity vulnerabilities.

### Error output
```
Total: 6 (HIGH: 6, CRITICAL: 0)

Library       | CVE            | Severity | Status   | Fixed Version
libncursesw6  | CVE-2025-69720 | HIGH     | affected | (none)
```

### Root cause
The base Docker image contained OS-level packages with known vulnerabilities. The `Fixed Version` column was empty, meaning no patch was available yet.

### Fix
Added `ignore-unfixed: true` to the Trivy scan step so vulnerabilities with no available fix are skipped.

```yaml
- name: scan the container
  uses: aquasecurity/trivy-action@master
  with:
    image-ref: ${{ env.ECR_REGISTRY }}/${{ env.ECR_REPOSITORY }}:${{ env.IMAGE_TAG }}
    format: 'table'
    exit-code: '1'
    vuln-type: 'os,library'
    severity: 'CRITICAL,HIGH'
    hide-progress: 'true'
    ignore-unfixed: true        # ← added this
```

---

## Error 5 — Assignment Feature Not Working

### What happened
Assignments were being added successfully (flash message appeared) but the Pending list always showed 0 assignments.

### Root cause
When fixing the ruff E712 error, the SQLAlchemy filter was incorrectly changed to:

```python
# This evaluates in Python, not in the database query
pending = Assignment.query.filter(
    not Assignment.is_completed    # ← always True, no filter applied
).all()
```

This caused ALL assignments to be returned as completed and NONE as pending.

### Fix
```python
# Correct SQLAlchemy syntax
pending = Assignment.query.filter(
    Assignment.is_completed.is_(False)
).order_by(Assignment.due_date.asc()).all()

completed = Assignment.query.filter(
    Assignment.is_completed.is_(True)
).order_by(Assignment.due_date.desc()).limit(10).all()
```

---

## Final Pipeline Order

```
1. Lint with ruff       ← catches unused imports, style issues
2. Run unit tests       ← catches broken functionality  
3. Build Docker image   ← only if code is clean and tested
4. Scan with Trivy      ← only if image is built
5. Push to ECR          ← only if scan passes
6. Approval gate        ← human reviewer approves
7. Deploy to ECS        ← rolling deploy
```

---

## Key Learnings

| # | Learning |
|---|---|
| 1 | Always run `ruff check .` locally before pushing to avoid pipeline failures |
| 2 | `ruff check --fix .` auto-fixes most issues but not all |
| 3 | SQLAlchemy filters must use `.is_(False)` not `== False` to satisfy both ruff and the ORM |
| 4 | `ignore-unfixed: true` in Trivy skips vulnerabilities that have no available patch |
| 5 | Lint runs first because it is the cheapest and fastest check — fail early |
```

---

