# Facebook Marketing Engineering Plan — McCoy Carpentry
Updated 2026-10-16. iPhone-only owner. Target: $0 cash spend.

## Verified
- Metricool connected: brand 7466901 / Facebook Page 1013779581815640. Four text-only auto-publish posts pending for Oct 19, 21, 23, 25. Avoid duplicates.
- Meta retired Facebook Groups API and publish_to_groups on April 22, 2024. Official third-party group publishing is unavailable: https://developers.facebook.com/docs/graph-api/changelog/version19.0
- Facebook group participation and approval depend on admins: https://www.facebook.com/help/1414053028933409/
- Meta Business Suite supports Page inbox instant replies: https://www.facebook.com/help/1698046970464236/
- GitHub scheduled runs can be delayed/dropped and public repository schedules disabled after 60 days of inactivity: https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows
- GitHub does not provide Facebook authentication, private group access, or direct ChatGPT notifications.
- This GitHub repository is public. Never store passwords, session cookies, access tokens, private customer data or private group posts here.

## Architecture
1. Page publisher: Metricool scheduling, actual work photos, deduplication and status verification.
2. Discovery: public-search leads, relevance scoring by service/area/date, URL deduplication and failure logs. Current Bing RSS code is not yet tested.
3. Approved destinations: verify group posting rules, Page eligibility, allowed days/frequency and review date.
4. Outreach: prepare specific helpful replies. No automatic third-party group posting until a permitted, reliable authenticated method is verified.
5. Reporting: read Metricool and GitHub state in ChatGPT; recurring messages require a separately scheduled ChatGPT task and dependable access to results.

## Validation gates
1. Execute GitHub workflow; inspect results.csv for valid, timely, nonduplicate leads and meaningful error logs.
2. Publish one real-photo Facebook Page post and verify live publication.
3. Check Meta Business Suite Page inbox and instant-reply setup.
4. Confirm candidate groups permit business Pages, promotional posts and comments; log rules.
5. Test one approved group interaction manually before attempting any automation.
6. Send a report separating published, pending, failed and unverified actions.

## Non-goals and safety
- No fake Facebook identity, CAPTCHA bypass, hidden Facebook endpoints or mass spam.
- No generic photos misrepresented as actual customer projects.
- No claims of 24/7 Facebook monitoring without an operational mechanism.
- Never send the same advertising comment repeatedly; follow group-specific rules.
- Owner retains full control and ability to inspect Facebook directly.

## Next priority
Validate the existing workflow, collect approved project photos/business card, extend Metricool content schedule, and investigate supported group-access pathways.
