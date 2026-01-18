---
name: webapp-testing
description: Toolkit for testing web applications using Playwright. Use when verifying frontend functionality, debugging UI behavior, capturing screenshots, or viewing browser logs.
---

# Web Application Testing

Test web applications using Python Playwright scripts.

## Decision Tree

```
User task → Is it static HTML?
    ├─ Yes → Read HTML file directly for selectors
    │         └─ Write Playwright script
    │
    └─ No (dynamic webapp) → Is server already running?
        ├─ No → Start server first, then test
        │
        └─ Yes → Reconnaissance-then-action:
            1. Navigate and wait for networkidle
            2. Take screenshot or inspect DOM
            3. Identify selectors from rendered state
            4. Execute actions
```

## Basic Playwright Script

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('http://localhost:5173')
    page.wait_for_load_state('networkidle')  # CRITICAL: Wait for JS
    
    # Reconnaissance
    page.screenshot(path='/tmp/inspect.png', full_page=True)
    
    # Actions
    page.click('button#submit')
    
    browser.close()
```

## Reconnaissance Pattern

1. **Inspect DOM**:
   ```python
   page.screenshot(path='/tmp/inspect.png', full_page=True)
   content = page.content()
   page.locator('button').all()
   ```

2. **Identify selectors** from results

3. **Execute actions** with discovered selectors

## Common Pitfall

❌ Inspect DOM before waiting for `networkidle`
✅ Always `page.wait_for_load_state('networkidle')` first

## Best Practices

- Use `sync_playwright()` for synchronous scripts
- Always close browser when done
- Use descriptive selectors: `text=`, `role=`, CSS, IDs
- Add waits: `wait_for_selector()`, `wait_for_timeout()`
- Launch chromium in `headless=True` mode
