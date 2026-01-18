---
name: test-create
description: Generate test cases for code
---

# Skill: Create Tests

## Purpose
Generate comprehensive test cases for new or existing code.

## Inputs
- Code to test
- Requirements/acceptance criteria

## Test Types

| Type | Purpose | When to Use |
|------|---------|-------------|
| Unit | Test individual functions | Always |
| Integration | Test component interactions | APIs, DB |
| E2E | Test full user flows | Critical paths |

## Workflow

1. **Analyze** - Understand the code's purpose
2. **Identify** - List testable behaviors
3. **Design** - Plan test cases
4. **Write** - Implement tests
5. **Run** - Verify all pass

## Test Case Categories

### Happy Path ✅
- Normal expected inputs
- Standard use cases

### Edge Cases 🔸
- Empty inputs
- Boundary values
- Maximum/minimum values

### Error Cases ❌
- Invalid inputs
- Network failures
- Missing data

## Output Template

### Python (pytest)
```python
import pytest
from module import function_to_test

class TestFunctionName:
    """Tests for function_to_test"""
    
    # Happy Path
    def test_normal_input_returns_expected(self):
        """Given valid input, should return expected result"""
        result = function_to_test("valid_input")
        assert result == "expected_output"
    
    # Edge Cases
    def test_empty_input_returns_empty(self):
        """Given empty input, should return empty result"""
        result = function_to_test("")
        assert result == ""
    
    # Error Cases
    def test_invalid_input_raises_error(self):
        """Given invalid input, should raise ValueError"""
        with pytest.raises(ValueError):
            function_to_test(None)

# Fixtures
@pytest.fixture
def sample_data():
    return {"key": "value"}
```

### JavaScript (Jest)
```javascript
describe('functionName', () => {
  // Happy Path
  it('should return expected result for valid input', () => {
    expect(functionName('valid')).toBe('expected');
  });

  // Edge Cases
  it('should handle empty input', () => {
    expect(functionName('')).toBe('');
  });

  // Error Cases
  it('should throw for invalid input', () => {
    expect(() => functionName(null)).toThrow();
  });
});
```

## Test Naming Convention

```
test_[what]_[condition]_[expected]

Examples:
- test_login_with_valid_credentials_returns_token
- test_login_with_wrong_password_raises_auth_error
- test_get_user_when_not_found_returns_none
```

## Coverage Goals

| Code Type | Target |
|-----------|--------|
| Business logic | 80%+ |
| Utility functions | 90%+ |
| UI components | 60%+ |
| Infrastructure | 50%+ |

## Tips
- Test behavior, not implementation
- One assertion per test (when possible)
- Use descriptive test names
- Mock external dependencies
- Keep tests fast and isolated
