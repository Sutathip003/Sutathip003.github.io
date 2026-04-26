# AGENTS.md

## 1. Purpose
This file provides instructions for AI agents working on this repository.

Goals:
- Maintain clean, modular, and readable code
- Follow consistent project structure
- Avoid breaking existing functionality
- Prefer clarity over cleverness

---

## 2. Project Structure Principles

- Keep responsibilities separated:
  - UI / presentation
  - business logic
  - data access

- Do NOT mix layers unnecessarily
- Reuse existing modules before creating new ones
- Avoid duplicate logic

---

## 3. General Development Rules

- Make minimal, focused changes
- Do not refactor unrelated code
- Do not introduce breaking changes unless required
- Always preserve existing behavior unless explicitly asked

- Prefer:
  - simple solutions
  - readable code
  - explicit logic

---

## 4. Code Style Guidelines

### Naming
- Use descriptive names (no abbreviations)
- Functions → verbs
- Variables → clear meaning

### Structure
- Small, single-purpose functions
- Avoid deeply nested logic
- Extract reusable components

### Comments
- Explain *why*, not *what*
- Avoid obvious comments

---

## 5. Working with Existing Code

- Read surrounding code before making changes
- Match existing patterns and conventions
- Do not introduce new patterns unless necessary

- If unclear:
  - choose the simplest consistent approach

---

## 6. Error Handling

- Validate inputs where appropriate
- Fail clearly and predictably
- Do not silently ignore errors

---

## 7. Dependencies

- Do not add new dependencies unless necessary
- Prefer built-in or existing solutions
- If adding dependency:
  - justify why
  - keep it minimal

---

## 8. File Editing Rules

- Modify only relevant files
- Do not rename or move files unless required
- Keep changes small and traceable

---

## 9. Testing & Validation

- Ensure changes do not break existing functionality
- Test edge cases when relevant
- Keep logic deterministic

---

## 10. Performance & Security

- Avoid unnecessary computation
- Do not introduce obvious security risks
- Be careful with:
  - user input
  - data handling
  - external calls

---

## 11. UI / Frontend Guidelines

- Keep UI simple and consistent
- Avoid unnecessary complexity
- Maintain readability and usability

---

## 12. When Unsure

If requirements are unclear:
- choose the simplest working solution
- follow existing patterns
- avoid overengineering

---

## 13. What to Avoid

- Overcomplicated abstractions
- Large, unrelated refactors
- Hidden side effects
- Duplicate code
- Magic values without explanation

---

## 14. Output Expectations

When making changes:
- Be precise
- Be minimal
- Be consistent with existing code

The goal is maintainability and clarity, not cleverness.