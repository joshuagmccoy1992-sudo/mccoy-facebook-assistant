# McCoy Carpentry marketing operating skeleton

## Goal
Discover relevant homeowner requests, advertise McCoy Carpentry where authorized, maintain a publishing queue, and report outcomes to the owner in ChatGPT.

## Current working components
- `lead_watch.py` + GitHub Actions: daily **public web search** discovery. CSV artifact must be manually reviewed; not verified active Facebook leads.
- Metricool brand `7466901`: connected Facebook business-page scheduling. Four posts were previously scheduled for Oct 19, 21, 23 and 25, 2026; avoid duplicates.

## Control files
- `config/business.json`: identity, service territory, restrictions.
- `config/locations.csv`: approved group/page inventory. Do not post until each destination's permissions are verified.
- `config/content_queue.csv`: draft/approved/scheduled/published post ledger.
- `config/reply_templates.csv`: starting points, customize to actual requests.

## Execution boundaries
- Do not invent customer leads, project photos, testimonials, permission to advertise, or successful publications.
- Never claim to be continuously monitoring Facebook or responding to messages unless an actual connected tool performs it.
- Only use authentic business/project photos approved by the owner.
- Group posts and third-party comments are NOT connected. Facebook access is needed; GitHub Actions alone does not provide it.
- Report what actually published, what is pending, what failed, and leads requiring owner follow-up.

## Next integrations
1. Verify first GitHub workflow run produces a useful report.
2. Import owner's approved project photos and business-card image.
3. Build and verify approved group/page destination list.
4. Set up a permitted authenticated Facebook group-post/comment mechanism, with human review where required.
5. Configure recurring ChatGPT report delivery when connected metrics and lead reports can be retrieved.
