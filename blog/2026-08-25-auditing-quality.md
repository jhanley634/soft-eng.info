
# auditing quality

I was recently asked about

> useful skills or tools for auditing codebase quality

Wow, that's pretty open ended!
Where to begin?

## table stakes

The code _will_ compile.
And it will lint cleanly.

Hopefully on every commit.
Certainly on every
[PR]((https://en.wikipedia.org/wiki/Distributed_version_control#Pull_requests).
A [pre-commit config](https://github.com/jhanley634/ml-2026/blob/main/.pre-commit-config.yaml)
file can help with that,
enforcing similar assumptions across team members.

Most projects I contribute to have a `make lint` target,
but some have used a `just` alias or Bourne scripts.
What matters is that everyone does the same checks,
and that it's easy to do.

I choose to annotate all my python code
so `mypy --strict` passes, but that's
not for everyone.
Choose what makes sense for your project,
and enforce it across all contributors.

## meaning of "quality"

### project setup

Let's say your existing project is

- "big" -- at least several KLOCs
- "mature" -- folks have been hacking on it for months

and you work in two-week sprints,
so no feature branch should last much longer than that.
You work with a pair of contractors, TeamA and TeamB,
and want to ship a pair of unrelated features two weeks from now,
each of them estimated to be about ten days of work.
Maybe one is a new django page for ordering some new product,
and the other is yet another new internal reporting dashboard.
The codebase already supports ordering various products
and viewing various dashboards, supported by some utility routines.

The teams should work in parallel.
During this sprint we're looking for each to submit just a single PR.
We don't want a cleanup refactor from A to impact B.

### metrics

#### man-hours

[WIP]
