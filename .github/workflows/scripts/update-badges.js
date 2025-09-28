#!/usr/bin/env node
/**
 * Inserts/updates Scorecards & OpenSSF Best Practices badges in README.md.
 * Supply env: REPO_OWNER, REPO_NAME, OSSF_BP_ID
 */
const fs = require('fs');
const path = require('path');

const owner = process.env.REPO_OWNER;
const repo = process.env.REPO_NAME;
const bpId = process.env.OSSF_BP_ID;

if (!owner || !repo || !bpId) {
  console.error('Missing env: REPO_OWNER, REPO_NAME, OSSF_BP_ID');
  process.exit(1);
}

const badgeBlock =
`[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/${owner}/${repo}/badge)](https://securityscorecards.dev/viewer/?platform=github&org=${owner}&repo=${repo})
[![OpenSSF Best Practices](https://bestpractices.coreinfrastructure.org/projects/${bpId}/badge)](https://bestpractices.coreinfrastructure.org/projects/${bpId})
`;

const readmePath = path.join(process.cwd(), 'README.md');
let readme = fs.readFileSync(readmePath, 'utf8');

if (readme.includes('OpenSSF Scorecard')) {
  readme = readme.replace(/\[!\[OpenSSF Scorecard][\s\S]*?\)\n?/, badgeBlock);
} else {
  // insert after first H1 or at top
  readme = readme.replace(/^# .*\n?/, (m) => m + '\n' + badgeBlock);
}

fs.writeFileSync(readmePath, readme, 'utf8');
console.log('✅ README badges updated.');

