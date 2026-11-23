# TOOL-dBoundRoles-44 widen 13 — dead-path-waivers widened

**Serves:** widen TOOL-dBoundRoles-44

- **Population:** dead-path-waivers
- **Keys:** `{prefix}/govkit/fixtures/adopter-ic-2cff5855.receipt.json	"{prefix}/hooks/agent-cap.js",`, `{prefix}/govkit/fixtures/adopter-ic-2cff5855.receipt.json	".claude/hooks/agent-cap.js"`, `{prefix}/govkit/fixtures/adopter-ic-2cff5855.receipt.json	"{prefix}/hooks/agent-cap.test.sh",`, `{prefix}/govkit/fixtures/adopter-ic-2cff5855.receipt.json	".claude/hooks/agent-cap.test.sh"`, `{prefix}/govkit/fixtures/adopter-ic-2cff5855.receipt.json	"path": ".claude/hooks/agent-cap.js",`, `{prefix}/govkit/fixtures/adopter-ic-2cff5855.receipt.json	"source": "{prefix}/hooks/agent-cap.js"`, `{prefix}/govkit/fixtures/adopter-ic-2cff5855.receipt.json	"path": ".claude/hooks/agent-cap.test.sh",`, `{prefix}/govkit/fixtures/adopter-ic-2cff5855.receipt.json	"source": "{prefix}/hooks/agent-cap.test.sh"`
- **Reason:** a frozen adopter receipt fixture records the retired hook and its suite as an install once wrote them, and is never edited
- **Caused-by:** TOOL-dBoundRoles-44
