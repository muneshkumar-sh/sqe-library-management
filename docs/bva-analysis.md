# Boundary Value Analysis

## 1. fine_tier() Boundary Analysis

The `fine_tier()` function determines the fine category based on the number of days a book is overdue.

### Boundary 1 — Domain Edge (0)

| Boundary | Value - 1 | Value | Value + 1 |
|---|---:|---:|---:|
| 0 | -1 → ValueError | 0 → None | 1 → Low |

### Boundary 2 — None/Low (0/1)

| Boundary | Value - 1 | Value | Value + 1 |
|---|---:|---:|---:|
| 1 | 0 → None | 1 → Low | 2 → Low |

### Boundary 3 — Low/Medium (7/8)

| Boundary | Value - 1 | Value | Value + 1 |
|---|---:|---:|---:|
| 8 | 7 → Low | 8 → Medium | 9 → Medium |

### Boundary 4 — Medium/High (14/15)

| Boundary | Value - 1 | Value | Value + 1 |
|---|---:|---:|---:|
| 15 | 14 → Medium | 15 → High | 16 → High |

### Boundary 5 — High/Severe (30/31)

| Boundary | Value - 1 | Value | Value + 1 |
|---|---:|---:|---:|
| 31 | 30 → High | 31 → Severe | 32 → Severe |

## 2. Boundary Summary

| Boundary | Value - 1 | Boundary Value | Value + 1 |
|---|---|---|---|
| Domain edge 0 | -1 → ValueError | 0 → None | 1 → Low |
| None/Low 1 | 0 → None | 1 → Low | 2 → Low |
| Low/Medium 8 | 7 → Low | 8 → Medium | 9 → Medium |
| Medium/High 15 | 14 → Medium | 15 → High | 16 → High |
| High/Severe 31 | 30 → High | 31 → Severe | 32 → Severe |

## 3. Conclusion

Boundary Value Analysis focuses on values immediately below, at, and immediately above each boundary. These values help detect off-by-one errors in `fine_tier()`.