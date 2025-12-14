# Microtasks for Cline — NanoSOC Foundry (40 tasks)

[x] 1. Create repo skeleton and add README.md (top-level) and LICENSE.
[x] 2. Add requirements.txt and a top-level .gitignore.
3. Implement `normalizer/app.py` (FastAPI) with /ingest endpoint.
4. Implement `normalizer/normalizer_core.py` with normalize(raw_event) function and unit tests.
5. Add basic Sigma-lite rule loader `normalizer/rules/loader.py`.
6. Implement in-memory rule engine `normalizer/rules/engine.py` and sample rule YAMLs.
7. Create `simulator/simulator.py` CLI and scenario loader; add `scenarios/lateral_movement.json`.
8. Add `scenarios/data_exfil.json` and `scenarios/phishing_click.json`.
9. Implement file sink option for simulator (write JSONL).
10. Implement HTTP sink option for simulator (POST to /ingest).
11. Add `deception/deception_service.py` with simple GET honeypot endpoint and logging.
12. Implement honeytoken generator `deception/honeytoken_generator.py` and sample tokens.
13. Wire deception service to post hits to normalizer's /ingest endpoint.
14. Create `orchestrator/orchestrator.py` to start components for demo.
15. Add `ui/index.html` single-file app with CSS and basic layout.
16. Implement SSE or polling endpoint in normalizer `app.py` for live stream.
17. Connect UI to the live stream and display events in a scrollable pane.
18. Add alerts pane in UI — display Sigma-lite matches.
19. Add simple timeline/replay control in UI to replay a scenario.
20. Add unit tests for normalize() and simulator scenario loading.
21. Create Dockerfile for normalizer and deception components.
22. Add docker-compose.yml to run normalizer+deception+ui.
23. Add logging config and rotate logs for long runs.
24. Implement deduplication in normalizer_core (basic event hashing).
25. Add geoip stub enrichment in normalizer_core (lookup by IP -> country).
26. Add sample Sigma-like rule: detect psexec process_create after remote auth.
27. Add sample Sigma-like rule: detect large outbound data transfer events.
28. Add sample Sigma-like rule: detect honeytoken access.
29. Add README docs for adding new rules and scenarios.
30. Create `docs/demo_instructions.md` with step-by-step demo commands.
31. Add GitHub Actions workflow to run pytest on pushes/PRs.
32. Provide example report template under docs/templates/report_template.md.
33. Implement small CLI `tools/generate_sample_scenarios.py` to auto-generate many events.
34. Add small utility `tools/pretty_print_event.py` for debugging.
35. Create CHANGELOG.md and initial entry.
36. Harden normalizer endpoint to validate input schema with pydantic.
37. Implement basic rate limiting on /ingest to avoid floods (configurable).
38. Add API endpoint to normalizer to list active rules and toggle them.
39. Add sample screenshot GIF for README (placeholder file).
40. Zip the completed MVP into starter.zip and place at repo root.
41. Implement canary generator deception/canary_generator.py that creates fake credentials using AWS‑style patterns (e.g., AKIA*).
42. Add canary registry in deception/canary_store.json to track active canaries and the files/locations where they should be deployed.
43. Add canary hit endpoint in deception/deception_service.py that logs when a canary token is used (e.g., GET /trigger_canary id=...)
44. Add Sigma‑lite rule to detect AWS‑style token exposure or usage.
45. Add UI support to show canary hits in Alerts pane with special formatting (e.g., 🔥 or highlight color).
46. Add sample “canary deployment locations” for the demo (fake files, fake URLs, fake config entries).
47. Add background watcher that scans ingested events+raw logs for AWS‑style token patterns.
48. Add expiration + rotation for canaries.

Tokens regenerate every X hours, old ones marked inactive.

***Notes:*** Each microtask should create or modify no more than 1-3 files and include short tests where appropriate.
