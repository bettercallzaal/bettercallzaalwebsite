# How to Add New Research

## Step 1: Pick the Next Number

Check the highest numbered folder in `research/` and use the next number. Also update [research-index.md](./research-index.md).

## Step 2: Create the Folder

```bash
mkdir -p research/{number}-{topic-name}
```

## Step 3: Write the README with This Template

```markdown
# {Number} — {Title}

> **Status:** Research complete
> **Date:** {Today's date}
> **Goal:** {One-line description of what this research answers}

---

## Key Takeaways

{Bullet list of the main recommendations — put these FIRST}

---

## {Section 1}

{Research content with tables, code blocks, comparisons}

## {Section 2}

{More content}

---

## Sources

- [Source Name](URL)
```

### Rules for Writing Research Docs

1. **Recommendations first** — readers get the answer in 30 seconds
2. **Use tables** for comparisons and feature lists
3. **Include specific versions, URLs, and dates**
4. **Link sources** at the bottom
5. **Keep it actionable** — "here's what to do", not just "here's what exists"
6. **Filter through BetterCallZaal's context** — static HTML site, Farcaster mini app, personal brand for a web3 connector

## Step 4: Update the Index

Add the new doc to `research/README.md` and `.agents/skills/bcz-research/research-index.md`.

## Step 5: Commit

```bash
git add research/{number}-{topic}/ research/README.md .agents/skills/bcz-research/research-index.md
git commit -m "docs: add {topic} research (doc {number})"
```

## Quality Checklist

- [ ] Key takeaways/recommendations at the top
- [ ] Specific to BetterCallZaal (static HTML, Farcaster mini app)
- [ ] Numbers, versions, and dates included
- [ ] Sources linked
- [ ] Both index files updated
