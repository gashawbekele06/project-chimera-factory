# Runtime Agent Skills

Skills are specific capability packages that Chimera Worker agents invoke via MCP Tools.

Each skill lives in its own sub-folder with a README.md defining:

- Description
- Input schema (JSON)
- Output schema (JSON)
- MCP Tool name

No full implementation yet — only contracts (structure ready for TDD/future filling).

## Defined Skills

- fetch_trends: Retrieve trending topics from social platforms
- generate_video: Create short-form video content matching persona
- post_content: Publish text/media to social channels with disclosure

Add more skills later (e.g., reply_comment, execute_transaction, download_youtube).
