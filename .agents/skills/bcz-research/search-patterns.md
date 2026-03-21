# How to Search Existing Research

## Quick Search Commands

Search all research documents for a keyword:
```bash
grep -ri "keyword" research/*/README.md
```

Search across research + ZAO OS research library:
```bash
grep -ri "topic" research/*/README.md /tmp/zaoos/research/*/README.md
```

Find which docs mention a specific technology:
```bash
grep -rli "farcaster\|sdk\|miniapp" research/*/README.md
```

## Common Patterns

### Find implementation details
```bash
grep -ri "npm install\|import.*from\|cdn\|esm.sh" research/*/README.md
```

### Find best practices
```bash
grep -ri "best practice\|recommend\|avoid\|don't" research/*/README.md
```

### Find specific API/URL patterns
```bash
grep -ri "https://\|api\|endpoint" research/*/README.md
```

## Also Check

- ZAO OS research library: `/tmp/zaoos/research/*/README.md`
- ZAO OS docs: `/tmp/zaoos/docs/*.md`
