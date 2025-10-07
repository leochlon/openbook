# CONTRIBUTORS.md

## About This Book

**Information Geometry: From Bayesian Foundations to Production Systems** is a collaborative academic book that makes cutting-edge theory accessible and connects it to real-world practice. The book is written with ADHD-friendly structure: clear breathing space, one concept at a time, and explicit break points between dense sections.

## Current Contributors

### Primary Author
- **[Leon Chlon]** - Chapter structure, primary content, overall narrative arc

### Contributing Authors
*Contributors will be listed here as they make substantive contributions*

## Contribution Philosophy

This book aims to democratize knowledge about information geometry. We welcome contributions from researchers, practitioners, and students who can help make the material clearer, more accurate, or more connected to practice. Quality matters more than credentials.

## The One Subsection Rule

**You may edit or create ONE subsection per pull request.**

This is the most important rule. It ensures:
- **Style consistency**: Your contribution blends seamlessly with existing text
- **Coherent voice**: The chapter reads as unified, not patchwork
- **Focused reviews**: Reviewers can give deep feedback on focused contributions
- **Quality over quantity**: Better to do one thing excellently than many things adequately

If you want to contribute to multiple areas, submit separate PRs and wait for approval before the next contribution. After your first PR is merged, you're welcome to contribute another subsection through a new PR.

## What Counts as "One Subsection"

A subsection is a third-level heading in LaTeX: `\subsection{Title}`. For example, in Chapter 1:
- `\subsection{Shannon's Foundational Insight}` is one subsection
- `\subsection{From Bits to Nats}` is another subsection
- `\subsection{Why Log Loss Is Codelength}` is a third subsection

You may:
- **Edit** an existing subsection (improve clarity, fix errors, add examples)
- **Create** a new subsection within an existing section
- **Extend** a subsection with additional paragraphs, examples, or clarifications

You may not:
- Edit multiple subsections in one PR
- Create new sections (section = `\section{Title}`)
- Create new chapters
- Restructure existing chapter organization

## Style Must Be Indistinguishable

**If reviewers can identify where your contribution begins and ends, revisions will be required.**

Before contributing:
1. **Read the entire section** (not just the subsection you're editing)
2. **Study the voice**: Conversational yet precise, building intuition before formalism
3. **Match the pacing**: One concept at a time, with breathing space
4. **Use consistent notation**: Check existing usage before introducing symbols
5. **Follow ADHD-friendly patterns** (see below)

### ADHD-Friendly Writing Patterns

All contributions must maintain these attention management features:

**Breathing space:**
```latex
\vspace{0.3cm}  % Between dense concepts within subsections
\vspace{1em}    % Between subsections
\vspace{1.5em}  % Before/after example boxes
\vspace{2em}    % Between major sections
