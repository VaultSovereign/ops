# Educational Content Prompt Library — Blogs, Teaching & Learning {#educational-content-library}

VaultMesh — Earth's Civilization Ledger

## Introduction
The Educational Content Prompt Library is a sovereign grimoire for creating insightful blogs, lesson plans, research summaries and learning experiences. Each prompt is defined like an API: it has a clear purpose, structured inputs and outputs, a quality checklist, and guardrails to ensure accuracy, inclusivity and ethical conduct. Replace {{placeholders}} at run time and keep prompts under version control alongside catalog updates.

## Navigation
### Core Prompts
- Research Synthesizer
- Topic Outliner
- Lesson Planner
- Pedagogy Advisor
- Learning Objective Refiner
- Content Evaluator
- Engagement Strategist
- Inclusive Language Checker
- SEO Enhancer
- Multimedia & Interactive Designer
- Audience Understanding Survey
- Student Feedback Collector
- Reflection Prompter
- Content Calendar Planner
- Citation & Credibility Validator
- Resource Summarizer
- Curriculum Alignment Checker
- Assessment Designer
- Gamified Learning Challenge Designer
- Accessibility Auditor
- Social Media Booster
- Community Builder
- Podcast & Webinar Advisor
- Data Visualization Suggestor
- Responsive Design Consultant
- Peer Review Coordinator
- Source Finder & Summarizer
- Standards & Compliance Checker
- Student Feedback Analyzer
- Content Recycling Planner
- Ethics & Privacy Guard
- Publication Format Advisor
- Writing Style & Tone Coach
- Idea Brainstormer
- Audience Personalizer
- Trend Watcher

### Tag Index
- research: literature review, summarization, sources, credibility
- structure: outlines, lesson plans, calendars, sequencing
- pedagogy: teaching strategies, Bloom's taxonomy, objectives
- writing: style, tone, clarity, concision
- engagement: interaction, storytelling, questions, audience participation
- inclusivity: inclusive language, accessible design, DEI
- seo: keywords, meta tags, search engine visibility
- multimedia: images, audio, video, interactive elements
- analysis: evaluation, feedback, reflection, improvement
- community: social media, user-generated content, collaboration
- ethics: privacy, academic honesty, citations, consent
- publication: format, platform choices, responsiveness

## Research Synthesizer {#research-synthesizer}

**Tags:** research, summarization, credibility  
**Safety class:** read‑only

**Purpose:** Generate a comprehensive yet concise summary of a topic by identifying credible sources, synthesising key points and highlighting gaps for further study. This is ideal for literature reviews, blog research or background sections of lesson plans.

**Inputs:**
- topic: {{subject_area}}
- scope: {{broad | focused}}
- timeframe: {{historical | last_5_years | last_year}}
- output_format: {{markdown | json | yaml}}

**Expected Outputs:**
- A summary paragraph presenting the main findings and why the topic matters
- Structured sections with source summaries, key facts and contradictory views
- Annotated bibliography with citations and credibility ratings
- A list of unanswered questions or future research directions

**Quality Checklist:**
- Verify each fact against at least two credible sources; flag anything with limited evidence
- Open with a clear statement of the topic and its significance[1]
- Use headings and short paragraphs to make the summary scannable[2]; include bullet lists for complex sets[3]
- Maintain a conversational tone appropriate for an intelligent lay audience[4]

**Safety Guardrails:**
- Only summarise publicly available or properly licensed sources
- Avoid speculation; label opinions and unresolved debates explicitly
- Cite all sources with inline footnotes

**Output Example:**
```json
{
  "summary": "Renewable energy adoption has accelerated in the last decade due to falling costs and climate policies.",
  "sources": [
    {
      "title": "IEA Renewables 2024",
      "authors": ["International Energy Agency"],
      "year": 2024,
      "key_points": ["Solar PV dominates growth", "Policy uncertainty in some regions"],
      "credibility": 0.9
    },
    {
      "title": "UN climate report",
      "authors": ["IPCC"],
      "year": 2024,
      "key_points": ["Net zero pathways require rapid scaling", "Need for grid flexibility"],
      "credibility": 0.95
    }
  ],
  "unanswered_questions": ["How will emerging economies finance transitions?", "What are the social impacts of rapid decarbonisation?"]
}
```

## Topic Outliner {#topic-outliner}

**Tags:** structure, planning, writing  
**Safety class:** read‑only

**Purpose:** Generate an outline for a blog post, article or lesson by identifying major sections, subtopics and narrative flow. This helps writers plan content efficiently and ensures key points are covered early[5].

**Inputs:**
- title: {{proposed_title}}
- main_points: {{list_of_key_ideas}}
- audience: {{general | expert | students}}
- length: {{short | medium | long}}
- tone: {{formal | conversational | reflective}} (optional)

**Expected Outputs:**
- Opening section that hooks readers and states the main idea upfront[6]
- Ordered list of sections with brief descriptions and suggested word counts
- Closing section suggesting a reflection, call to action or questions for readers[7]

**Quality Checklist:**
- Align section order with the inverted pyramid model: most important information first[8]
- Keep headings short and descriptive[9]
- Ensure each section aligns with the stated main_points and addresses the audience's needs
- Include at least one interactive or reflective element to encourage engagement[10]

**Safety Guardrails:**
- Do not include plagiarised phrases; all sections should be original or properly cited
- Avoid unnecessarily long outlines; if length is long, suggest splitting into multiple posts[11]

**Output Example:**
```yaml
outline:
  - title: "Introduction"
    description: "Introduce the importance of climate literacy, summarising global temperature trends."
    word_count: 150
  - title: "Causes of Climate Change"
    description: "Explain greenhouse gases, human activities and evidence from scientific studies."
    word_count: 300
  - title: "Impacts on Ecosystems"
    description: "Highlight effects on oceans, forests and biodiversity, using case studies."
    word_count: 300
  - title: "Solutions"
    description: "Discuss mitigation and adaptation strategies; encourage personal actions."
    word_count: 250
  - title: "Conclusion"
    description: "Summarise key messages and pose questions for reflection."
    word_count: 100
```

## Lesson Planner {#lesson-planner}

**Tags:** structure, pedagogy, planning  
**Safety class:** advisory

**Purpose:** Draft a structured lesson plan that aligns with learning objectives, curriculum standards and time constraints. It provides sequence of activities, estimated durations, and assessments, helping educators organise effective sessions.

**Inputs:**
- topic: {{lesson_topic}}
- grade_level: {{age_or_education_level}}
- learning_objectives: {{list_of_outcomes}}
- duration: {{minutes}}
- resources: {{materials_or_links}} (optional)

**Expected Outputs:**
- Overview summarising the lesson's importance and connection to curriculum[12]
- Timeline with warm‑up, instruction, practice and assessment segments
- Activity descriptions with pedagogical notes (e.g. storytelling, examples, group work)[13]
- Assessment plan aligned with objectives and suggestions for feedback

**Quality Checklist:**
- Align activities with declared learning_objectives and curriculum[12]
- Incorporate varied instructional strategies: storytelling, examples, multimedia[13][14]
- Ensure each activity fits within the allotted duration
- Recommend interactive or formative assessments to monitor understanding[15]

**Safety Guardrails:**
- Avoid including any personal data about students
- Respect copyright when linking resources; prefer open educational resources
- Do not recommend assessments that may cause harm or undue stress

**Output Example:**
```json
{
  "overview": "Students will learn about photosynthesis, linking the process to everyday plant care.",
  "timeline": [
    {
      "segment": "Warm‑up",
      "duration": 10,
      "description": "Ask students to describe how plants grow; show a short video."
    },
    {
      "segment": "Instruction",
      "duration": 20,
      "description": "Explain photosynthesis using visuals and simple equations."
    },
    {
      "segment": "Practice",
      "duration": 20,
      "description": "Students draw the process and label parts; discuss in pairs."
    },
    {
      "segment": "Assessment",
      "duration": 10,
      "description": "Quick quiz and open questions to assess understanding."
    }
  ],
  "assessment": {
    "method": "Formative quiz",
    "criteria": ["Correct identification of reactants and products", "Ability to explain process in own words"]
  }
}
```

## Pedagogy Advisor {#pedagogy-advisor}

**Tags:** pedagogy, strategy, guidance  
**Safety class:** advisory

**Purpose:** Recommend teaching strategies and classroom techniques tailored to a topic, audience and context. This helps educators choose approaches that maximise engagement and understanding.

**Inputs:**
- topic: {{subject_area}}
- grade_level: {{education_level}}
- learning_style_distribution: {{visual | auditory | kinesthetic | mixed}}
- class_size: {{number_of_students}}
- goal: {{knowledge | skills | attitude | mindset}}

**Expected Outputs:**
- Recommended instructional strategies (e.g. storytelling, hands‑on activities, discussions)[13][15]
- Tips to adapt instruction for diverse learning styles (visual, auditory, kinesthetic)[14]
- Suggestions for formative assessment and feedback loops
- Notes on culturally responsive teaching and inclusivity[16]

**Quality Checklist:**
- Explain why each strategy suits the grade_level and learning_style_distribution
- Avoid jargon; keep advice accessible[4]
- Encourage the use of inclusive language and diverse examples[16]
- Include at least one interactive technique to foster active learning[15]

**Safety Guardrails:**
- Do not suggest methods that require equipment unavailable in typical classrooms
- Respect cultural differences; avoid biased examples or stereotypes
- Remind educators to obtain necessary permissions for recordings or personal data collection

**Output Example:**
```yaml
strategies:
  - method: "Storytelling"
    rationale: "Puts abstract concepts into relatable context, aiding retention."
  - method: "Think‑Pair‑Share"
    rationale: "Encourages collaboration and allows quieter students to participate."
  - method: "Hands‑on experiment"
    rationale: "Supports kinesthetic learners by providing tactile experience."
  - method: "Formative quiz via polling app"
    rationale: "Provides immediate feedback and engages tech‑savvy students."

notes:
  inclusivity: "Use gender‑neutral language and avoid jargon; explain acronyms."
  reflection: "Encourage students to reflect on how concepts relate to their lives."
```

## Learning Objective Refiner {#learning-objective-refiner}

**Tags:** pedagogy, analysis, writing  
**Safety class:** read‑only

**Purpose:** Analyse and refine learning objectives to ensure they are specific, measurable, achievable, relevant and time‑bound (SMART) and aligned with Bloom's taxonomy.

**Inputs:**
- objectives: {{list_of_objectives}}
- grade_level: {{education_level}}

**Expected Outputs:**
- Updated objectives rewritten in SMART format
- Bloom's taxonomy classification (e.g. Remember, Understand, Apply, Analyse, Evaluate, Create)
- Suggested assessment types to measure each objective
- Notes on necessary prerequisites or scaffolding

**Quality Checklist:**
- Verify that each objective contains an action verb and a measurable outcome
- Align difficulty level to grade_level; avoid unrealistic expectations
- Provide at least one formative assessment suggestion per objective
- Use concise language free of jargon[16]

**Safety Guardrails:**
- Do not disclose sensitive personal data about students
- Only provide general pedagogical guidance; educators should adapt to local policies

**Output Example:**
```json
{
  "revised_objectives": [
    {
      "original": "Understand photosynthesis",
      "revised": "Students will be able to describe the inputs and outputs of photosynthesis in their own words.",
      "bloom_level": "Understand",
      "assessment": "Short written explanation"
    },
    {
      "original": "Analyse the impact of deforestation",
      "revised": "Students will analyse how deforestation affects local ecosystems by creating a cause‑effect diagram.",
      "bloom_level": "Analyse",
      "assessment": "Concept map"
    }
  ],
  "notes": "Ensure prior knowledge of basic ecology before introducing these objectives."
}
```

## Content Evaluator {#content-evaluator}

**Tags:** analysis, writing, evaluation  
**Safety class:** read‑only

**Purpose:** Review a draft blog post or lesson material to assess clarity, structure, readability and inclusivity. Provide actionable feedback to improve flow and engagement.

**Inputs:**
- draft_text: {{markdown_or_plain_text}}
- audience: {{general | experts | students}}
- criteria: {{clarity | tone | structure | inclusivity | seo}} (list)

**Expected Outputs:**
- Scoring for each criterion with explanation
- Highlighted sections needing revision (e.g., long sentences, jargon, lack of headings)
- Suggestions to improve structure (e.g., move main idea to first paragraph[5], break paragraphs, use lists[3])
- Recommendations for inclusive language and accessible design[16][17]

**Quality Checklist:**
- Keep feedback constructive and specific; point to the exact place needing improvement
- Refer to the length guidelines (70 words per paragraph, 300–700 words total)[18]
- Check for appropriate tone and voice; avoid bureaucratic language[19]
- Suggest adding subheadings and visuals where appropriate[20][21]

**Safety Guardrails:**
- Do not alter the author's intent; suggestions should respect the original message
- Avoid changing culturally specific expressions unless they hinder clarity or inclusivity
- Do not recommend SEO tactics that misrepresent the content's intent

**Output Example:**
```yaml
feedback:
  clarity:
    score: 0.7
    notes: "The introduction buries the main argument in the third paragraph. Move the thesis to the opening."
  structure:
    score: 0.6
    notes: "Paragraphs exceed 120 words; break them into smaller units and use bullet lists."
  inclusivity:
    score: 0.9
    notes: "Language is mostly inclusive, but replace 'guys' with 'everyone' and spell out acronyms."

recommendations:
  - "Add subheadings for each major section."
  - "Use simple sentences and active voice."
  - "Include a relevant image to illustrate the main concept."
```

## Engagement Strategist {#engagement-strategist}

**Tags:** engagement, writing, community  
**Safety class:** advisory

**Purpose:** Suggest techniques to captivate readers or learners, increase participation and foster a community around educational content.

**Inputs:**
- topic: {{subject_area}}
- audience: {{general | students | educators | parents}}
- tone: {{friendly | professional | reflective}}
- platform: {{blog | classroom | social_media}}

**Expected Outputs:**
- Opening hooks such as provocative questions or anecdotes[10]
- Recommendations for interactive elements (polls, quizzes, comment prompts, peer discussion)[15]
- Guidance on regular posting schedules and promotion[22]
- Community‑building tips, including user‑generated content and social sharing[23]

**Quality Checklist:**
- Make sure each engagement tactic fits the audience and platform (e.g., polls work well on social media; discussion prompts suit classrooms)
- Encourage two‑way communication—ask readers to share experiences or questions[10]
- Balance frequency and quality: recommend a schedule that the creator can sustain[22]
- Highlight the importance of visuals and multimedia to maintain interest[21][14]

**Safety Guardrails:**
- Avoid manipulative engagement tactics (clickbait titles or misleading spoilers)[24]
- Respect privacy; do not encourage sharing personal data in comments
- Remind creators to moderate discussions to prevent harassment or misinformation

**Output Example:**
```json
{
  "hooks": ["Did you ever wonder why birds sing before dawn?", "Imagine learning algebra through a treasure hunt…"],
  "interactive_elements": ["Embed a quiz after the second section", "Invite readers to share their own study tips in the comments"],
  "schedule": "Post every Tuesday and engage on social media twice per week",
  "community_tips": ["Highlight reader contributions in a monthly roundup", "Create a hashtag for class discussions"]
}
```

## Inclusive Language Checker {#inclusive-language-checker}

**Tags:** inclusivity, writing, ethics  
**Safety class:** advisory

**Purpose:** Assess text for inclusive language and accessibility, providing suggestions to replace problematic terms and improve readability. Ensuring inclusivity promotes psychological safety and respects diverse identities[16].

**Inputs:**
- text: {{markdown_or_plain_text}}
- focus: {{language | design | both}}

**Expected Outputs:**
- List of detected non‑inclusive or potentially offensive terms with explanations[16]
- Suggested replacements (e.g. gender‑neutral pronouns, person‑first language)
- Recommendations for visual design (contrast, colour choices, font size) when focus includes design[17]
- Summary of overall inclusivity and accessibility score

**Quality Checklist:**
- Verify that all acronyms are spelled out on first use[25]
- Suggest inclusive alternatives for gendered or ableist terms[26]
- Check for appropriate contrast and readability if design is assessed[17]
- Encourage language that reflects respect for all audiences[26]

**Safety Guardrails:**
- Do not enforce changes that alter intended meaning; offer alternatives and explanations
- Avoid recommending design changes that conflict with institutional branding; note when to consult a designer
- Respect cultural expressions unless they exclude or harm others

**Output Example:**
```yaml
issues:
  - term: "guys"
    explanation: "May exclude non‑male readers"
    suggestion: "everyone", "team"
  - term: "crazy idea"
    explanation: "Ableist language; can be replaced by neutral alternatives"
    suggestion: "unconventional idea"

visual_recommendations:
  - "Increase contrast between text and background for accessibility"
  - "Use sans‑serif fonts like Arial or Verdana at 12pt or larger"

summary:
  score: 0.85
  notes: "Most of the text is inclusive; a few terms and design choices require attention."
```

## SEO Enhancer {#seo-enhancer}

**Tags:** seo, writing, analysis  
**Safety class:** read‑only

**Purpose:** Provide guidance on optimizing educational content for search engines without sacrificing clarity or integrity[27]. Includes keyword suggestions, title and meta description advice, and internal/external linking strategies[28].

**Inputs:**
- topic: {{content_topic}}
- audience: {{students | educators | general_public}}
- existing_keywords: {{comma_separated_list}} (optional)

**Expected Outputs:**
- Recommended primary and secondary keywords based on topic and audience
- Draft title tag and meta description (within character limits)[29]
- Suggestions for internal and external links to credible sources[30]
- Notes on balancing SEO with readability and inclusivity

**Quality Checklist:**
- Ensure keywords align with readers' search intent[31]
- Avoid keyword stuffing; use natural language and active voice[32]
- Include at least one internal link and one external link to credible sources[30]
- Keep title tag (50–60 characters) and meta description (145–155 characters) within limits[29]

**Safety Guardrails:**
- Do not recommend deceptive or irrelevant keywords
- Respect privacy policies; avoid suggesting personal data as keywords
- Ensure external sources are reputable and accessible

**Output Example:**
```json
{
  "keywords": ["project‑based learning", "student engagement", "hands‑on activities"],
  "title_tag": "Project‑Based Learning: Engaging Students Through Hands‑On Activities",
  "meta_description": "Discover how project‑based learning boosts student engagement through hands‑on activities and storytelling.",
  "internal_links": ["/blog/benefits‑of‑pbl"],
  "external_links": ["https://www.edutopia.org/project‑based‑learning"]
}
```

## Multimedia & Interactive Designer {#multimedia-interactive-designer}

**Tags:** multimedia, engagement, inclusivity  
**Safety class:** advisory

**Purpose:** Recommend appropriate multimedia and interactive elements to enhance comprehension and engagement. These suggestions consider diverse learning styles and accessibility[14].

**Inputs:**
- topic: {{subject_area}}
- audience: {{students | general_public | mixed}}
- learning_styles: {{visual | auditory | kinesthetic | mixed}}
- budget: {{low | medium | high}}

**Expected Outputs:**
- List of suggested media types (images, videos, podcasts, diagrams, simulations, quizzes) with rationale[14]
- Accessibility notes: captions, alt text, high contrast visuals[17]
- Ideas for interactive features or gamification (e.g. quizzes, badges, simulations)[33]
- Tips for sourcing royalty‑free media and crediting creators[34]

**Quality Checklist:**
- Match media types to learning_styles distribution: e.g., podcasts for auditory learners, simulations for kinesthetic learners[35]
- Ensure all visual content includes alt text and sufficient contrast[17]
- Suggest free or low‑cost resources when budget is low[36]
- Include at least one interactive element to encourage active learning[33]

**Safety Guardrails:**
- Avoid recommending media that requires expensive licences unless budget is high
- Do not propose interactive elements that collect personal data without consent
- Respect copyright; link to open educational resources or specify permission needed

**Output Example:**
```yaml
media:
  - type: "Video"
    description: "Short explainer with captions summarising the scientific method."
  - type: "Diagram"
    description: "Flowchart illustrating research steps, accessible via alt text."
  - type: "Interactive Quiz"
    description: "Multiple‑choice quiz at the end to test understanding with instant feedback."

accessibility:
  - "Provide captions and transcripts for videos."
  - "Ensure images have alt text and high contrast."
```

## Audience Understanding Survey {#audience-understanding-survey}

**Tags:** analysis, research, engagement  
**Safety class:** advisory

**Purpose:** Design a survey to understand the interests, needs and backgrounds of the intended audience. Gathering this data helps tailor content and improve relevance[12].

**Inputs:**
- audience_type: {{students | educators | general_public}}
- information_goals: {{interests | challenges | preferences | demographics}}

**Expected Outputs:**
- A list of survey questions designed to elicit useful information (multiple choice, Likert scale, open‑ended)
- Guidance on distribution channels (email, social media, classroom, blog sidebar)
- Privacy considerations and consent language
- Tips on analysing survey results and applying insights

**Quality Checklist:**
- Keep questions clear, concise and inclusive[16]
- Avoid leading or biased questions
- Include demographic questions only if necessary and with explanation of purpose
- Provide instructions for protecting respondents' data and anonymity

**Safety Guardrails:**
- Obtain informed consent; clarify how data will be used and stored
- Do not collect sensitive personal information unless absolutely necessary and with appropriate safeguards
- Comply with data protection laws (GDPR, etc.)

**Output Example:**
```json
{
  "questions": [
    {
      "type": "multiple_choice",
      "text": "Which topics do you want to learn more about?",
      "options": ["Project‑based learning", "Assessment strategies", "Educational technology", "Diversity and inclusion"]
    },
    {
      "type": "scale",
      "text": "Rate your confidence in integrating technology into your teaching.",
      "scale": 5
    },
    {
      "type": "open",
      "text": "What challenges do you face when creating lesson plans?"
    }
  ],
  "distribution": ["Email newsletter", "Blog pop‑up survey", "Social media poll"],
  "privacy_note": "Responses are anonymous and will only be used to improve our educational resources."
}
```

## Student Feedback Collector {#student-feedback-collector}

**Tags:** analysis, feedback, engagement  
**Safety class:** advisory

**Purpose:** Generate a plan for collecting and analysing student feedback on lessons or educational content. Feedback helps refine teaching methods and content quality.

**Inputs:**
- context: {{course | blog | webinar | workshop}}
- feedback_methods: {{survey | reflection_journals | exit_tickets | interviews}}
- frequency: {{after_each_lesson | midterm | end_of_term}}

**Expected Outputs:**
- Recommended feedback questions or prompts tailored to context
- Logistics for collecting feedback (platforms, timing, anonymity)
- Strategies for analysing feedback and identifying trends
- Suggestions for closing the loop: communicating changes back to learners

**Quality Checklist:**
- Ensure questions are open, non‑judgemental and allow constructive criticism[16]
- Protect anonymity to encourage honest responses
- Provide a clear process for summarising and acting on feedback
- Include at least one prompt for positive feedback (what worked well?)

**Safety Guardrails:**
- Do not request personally identifiable information without clear necessity
- Adhere to institutional policies on student feedback confidentiality
- Avoid using feedback to penalise learners; use it for improvement

**Output Example:**
```yaml
questions:
  - "What aspects of the lesson helped you understand the topic better?"
  - "What could be improved for future sessions?"
  - "Rate the usefulness of the interactive activities on a scale of 1‑5."

collection:
  method: "Anonymous online survey"
  timing: "At the end of each module"

analysis:
  - "Group responses by theme and highlight recurring suggestions."
  - "Share a summary with students and explain how their input will inform changes."
```

## Reflection Prompter {#reflection-prompter}

**Tags:** analysis, writing, pedagogy  
**Safety class:** read‑only

**Purpose:** Generate questions or prompts that encourage authors or educators to reflect on their work and identify areas for improvement. Reflection strengthens continuous improvement and self‑awareness.

**Inputs:**
- context: {{blog_post | lesson | project}}
- focus: {{content_quality | student_response | personal_growth}}

**Expected Outputs:**
- List of reflective questions tailored to the context and focus
- Recommendations for documenting reflections (journals, blogs, portfolio entries)
- Suggestions for sharing reflections with peers or mentors for feedback

**Quality Checklist:**
- Questions should provoke critical thinking rather than yes/no responses
- Encourage consideration of both strengths and weaknesses
- Link reflections back to goals and intended outcomes[12]
- Suggest follow‑up actions based on reflections

**Safety Guardrails:**
- Reflection prompts should not blame or shame; frame challenges as opportunities for growth
- Respect privacy; reflections may include personal information that should remain confidential
- Avoid psychological prompts that may require professional support

**Output Example:**
```json
{
  "questions": [
    "What did readers or students respond to most strongly?",
    "How well did my structure support comprehension?",
    "Were there any barriers to engagement or inclusivity?",
    "What would I do differently next time?"
  ],
  "documentation": "Encourage keeping a reflective journal after each publication or lesson.",
  "peer_sharing": "Schedule monthly peer feedback sessions to discuss reflections and share best practices."
}
```

## Content Calendar Planner {#content-calendar-planner}

**Tags:** structure, planning, publication  
**Safety class:** advisory

**Purpose:** Create a schedule for publishing educational content across channels (blog, social media, newsletters) to maintain consistency and audience engagement[22].

**Inputs:**
- topics: {{list_of_topics}}
- frequency: {{weekly | biweekly | monthly}}
- platforms: {{blog | newsletter | social_media}}
- time_horizon: {{number_of_weeks_or_months}}

**Expected Outputs:**
- Calendar table outlining publication dates, topics and platforms
- Recommended buffer times for research, drafting, editing and review
- Reminders for promotional actions (e.g. social shares, email alerts)[22]
- Notes on avoiding burnout and maintaining quality over quantity

**Quality Checklist:**
- Balance frequency with realistic production capacity[22]
- Schedule variety in content types (articles, videos, interactive pieces) to cater to different learning styles[14]
- Include time for feedback incorporation and editing[37]
- Ensure the calendar aligns with academic or organisational events

**Safety Guardrails:**
- Do not overcommit; adjust schedule if workload becomes unsustainable
- Respect embargoes or confidentiality around upcoming announcements
- Avoid scheduling posts during periods when target audiences are unavailable (e.g., holidays)

**Output Example:**
```yaml
calendar:
  - date: "2025-10-05"
    topic: "Inclusive Teaching Techniques"
    platform: "Blog"
    tasks: ["Research sources", "Draft article", "Edit and proofread", "Prepare visuals"]
  - date: "2025-10-12"
    topic: "Interactive Learning Tools"
    platform: "Newsletter"
    tasks: ["Compile tool list", "Write summaries", "Design layout", "Schedule email"]
  - date: "2025-10-15"
    topic: "Student Voices Feature"
    platform: "Social Media"
    tasks: ["Collect student quotes", "Create graphics", "Publish thread", "Monitor engagement"]
```

## Citation & Credibility Validator {#citation-credibility-validator}

**Tags:** ethics, analysis, research  
**Safety class:** read‑only

**Purpose:** Check that all claims in a draft are supported by credible sources and that citations follow appropriate standards. It evaluates source quality, recency and relevance.

**Inputs:**
- draft_text: {{markdown_or_plain_text}}
- citation_style: {{APA | MLA | Chicago | other}}
- reference_list: {{list_of_cited_works}}

**Expected Outputs:**
- Identification of uncited claims or weak sources
- Assessment of each source's credibility (peer‑reviewed, official reports, reputable organisations)
- Suggested replacements for outdated or non‑authoritative sources
- Reformatted reference list according to citation_style

**Quality Checklist:**
- Ensure every factual statement has at least one supporting citation
- Cross‑check the recency of sources; flag anything beyond chosen timeframe[13]
- Recommend citing original studies or official guidelines over secondary reports
- Verify consistency in citation formatting and ordering

**Safety Guardrails:**
- Do not fabricate citations or misrepresent sources
- Avoid recommending sources that violate copyrights or paywalls unless necessary
- Respect disciplinary norms around self‑citation and preprints

**Output Example:**
```yaml
issues:
  - claim: "Game‑based learning always improves test scores."
    problem: "No citation provided; sweeping generalisation."
    suggestion: "Cite a meta‑analysis on gamification outcomes."
  - source: "Blog X, 2015"
    problem: "Outdated and not peer‑reviewed"
    suggestion: "Replace with a 2024 journal article on similar topic"

reformatted_references:
  - "Smith, J. (2024). The impact of gamification on student engagement. *Journal of Educational Research*, 98(2), 123‑134."
  - "UNESCO. (2023). Guidelines for inclusive teaching. UNESCO Publishing."
```

## Resource Summarizer {#resource-summarizer}

**Tags:** research, summarization, tools  
**Safety class:** read‑only

**Purpose:** Compile a curated list of educational tools, references or open educational resources (OER) related to a topic, summarising their purpose, cost and licensing. This helps educators and writers quickly locate quality materials.

**Inputs:**
- topic: {{subject_area}}
- resource_types: {{books | articles | videos | tools | datasets}}
- max_items: {{number}}

**Expected Outputs:**
- Table or list of resources with title, description, author/organisation, date, cost (if any) and licensing terms
- Short summary for each resource (1–2 sentences)
- Notes on why the resource is valuable and how it could be integrated into teaching or writing
- Links to access or download the resource (where permissible)

**Quality Checklist:**
- Prioritise peer‑reviewed, official or reputable sources; avoid low‑quality blogs or commercial advertisements
- Include open access or free options wherever possible[36]
- Ensure descriptions are concise and avoid plagiarism[16]
- Check for updated versions; note publication dates and edition numbers

**Safety Guardrails:**
- Respect copyright; provide only links and summaries
- Do not encourage downloading copyrighted material without permission
- Avoid listing tools that require personal data without explaining privacy practices

**Output Example:**
```yaml
resources:
  - title: "Khan Academy – Calculus"
    type: "Video"
    author: "Khan Academy"
    date: "2023"
    cost: "Free"
    license: "Creative Commons BY‑NC‑SA"
    summary: "Series of short videos explaining calculus concepts with practice exercises."
    link: "https://www.khanacademy.org/math/calculus"
  - title: "PhET Interactive Simulations"
    type: "Tool"
    author: "University of Colorado Boulder"
    date: "2024"
    cost: "Free"
    license: "Creative Commons Attribution"
    summary: "Interactive simulations covering physics, chemistry and maths topics."
    link: "https://phet.colorado.edu/"
```

## Curriculum Alignment Checker {#curriculum-alignment-checker}

**Tags:** pedagogy, analysis, compliance  
**Safety class:** advisory

**Purpose:** Evaluate whether lesson plans or course materials align with specified curriculum standards or frameworks. This assists educators in meeting institutional or national requirements.

**Inputs:**
- lesson_plan: {{json_or_yaml}}
- standards: {{framework_name}}
- grade_level: {{education_level}}

**Expected Outputs:**
- Mapping of lesson activities to relevant standard descriptors
- Identification of gaps or over‑coverage
- Recommendations to adjust activities or objectives for better alignment
- Notes on documentation or evidence needed for compliance

**Quality Checklist:**
- Confirm that each learning objective is linked to at least one standard
- Avoid duplication; ensure balanced coverage across standards
- Suggest modifications that maintain learning flow and engagement
- Use clear language to describe alignment; avoid jargon[4]

**Safety Guardrails:**
- Do not reinterpret standards; refer to official wording and cite sources
- Avoid prescribing curriculum changes that conflict with local policy
- Respect academic freedom; provide recommendations rather than mandates

**Output Example:**
```json
{
  "alignment": [
    {
      "objective": "Describe photosynthesis",
      "standard": "NGSS MS‑LS1‑6",
      "evidence": "Instruction segment on process"
    },
    {
      "objective": "Analyse environmental impact of deforestation",
      "standard": "NGSS MS‑LS2‑4",
      "evidence": "Discussion activity"
    }
  ],
  "gaps": [
    {
      "standard": "NGSS MS‑LS1‑7",
      "missing": "No activity covers cellular respiration"
    }
  ],
  "recommendations": ["Add a brief introduction to cellular respiration", "Include an exercise comparing photosynthesis and respiration"]
}
```

## Assessment Designer {#assessment-designer}

**Tags:** pedagogy, evaluation, planning  
**Safety class:** advisory

**Purpose:** Design formative or summative assessments tailored to learning objectives, ensuring fair evaluation and constructive feedback.

**Inputs:**
- learning_objectives: {{list_of_objectives}}
- assessment_type: {{quiz | project | presentation | portfolio | mixed}}
- grade_level: {{education_level}}
- skills_focus: {{knowledge | analysis | creativity | collaboration}}

**Expected Outputs:**
- Assessment description outlining tasks, criteria and scoring rubric
- Mapping of assessment items to learning objectives
- Suggestions for rubrics, including criteria descriptors and point values
- Recommendations for feedback methods and timing

**Quality Checklist:**
- Align assessment tasks with objectives and skills focus; avoid mismatch[12]
- Provide clear instructions and criteria to students[7]
- Include opportunities for self‑assessment or peer review where appropriate
- Ensure assessments are equitable and accessible (e.g., offer choice of formats; allow extra time when needed)[16]

**Safety Guardrails:**
- Avoid high‑stakes assessments without prior formative practice
- Respect privacy and confidentiality of assessment results
- Do not design assessments that discriminate against learners with disabilities

**Output Example:**
```yaml
assessment:
  type: "Project"
  description: "Students create a short documentary explaining local water cycle processes."
  rubric:
    - criterion: "Content accuracy"
      points: 10
      descriptors: ["All facts correct", "Minor inaccuracies", "Significant errors"]
    - criterion: "Creativity and storytelling"
      points: 5
    - criterion: "Technical quality"
      points: 5

objectives_mapping:
  - objective: "Explain the stages of the water cycle"
    item: "Narration"
  - objective: "Collaborate effectively"
    item: "Group project work"

feedback:
  method: "Individual written feedback and class showcase"
  timing: "Within one week of submission"
```

## Gamified Learning Challenge Designer {#gamified-learning-challenge-designer}

**Tags:** engagement, design, gamification  
**Safety class:** advisory

**Purpose:** Create game‑like challenges or competitions to enhance motivation and learning. Suitable for use in classrooms, workshops or blogs to encourage readers to apply concepts.

**Inputs:**
- topic: {{subject_area}}
- difficulty: {{easy | medium | hard}}
- learning_objectives: {{list_of_outcomes}}
- format: {{quiz | scavenger_hunt | role_play | simulation}}

**Expected Outputs:**
- Description of the game mechanics and rules
- List of tasks or questions aligned with objectives and difficulty
- Points or rewards system (badges, leaderboards, etc.)[38]
- Safety and fairness considerations (e.g., equal access, time limits)

**Quality Checklist:**
- Ensure tasks directly reinforce learning objectives[12]
- Provide clear instructions and scoring criteria
- Make challenges accessible to all learners; offer alternatives when necessary[17]
- Include debrief or reflection after the challenge to consolidate learning[7]

**Safety Guardrails:**
- Avoid competitive elements that could demotivate lower‑performing participants
- Respect privacy; do not display full names on leaderboards without consent
- Do not include unsafe or harmful activities in simulations

**Output Example:**
```json
{
  "game": "Climate Change Scavenger Hunt",
  "mechanics": "Teams search for clues around the classroom related to greenhouse gases, effects and solutions.",
  "tasks": [
    "Find a diagram of the carbon cycle and explain each part",
    "Identify three effects of global warming from provided articles",
    "Propose one individual action to reduce your carbon footprint"
  ],
  "scoring": {
    "correct_answer": 2,
    "creative_answer_bonus": 1,
    "completion_bonus": 5
  },
  "debrief": "Teams share answers and discuss what they learned about climate change."
}
```

## Accessibility Auditor {#accessibility-auditor}

**Tags:** inclusivity, analysis, ethics  
**Safety class:** advisory

**Purpose:** Evaluate educational content (web pages, documents, presentations) for accessibility compliance and inclusivity. Provide actionable recommendations to meet standards like WCAG.

**Inputs:**
- content_url: {{webpage_or_file}}
- criteria: {{visual | auditory | cognitive | motor | all}}

**Expected Outputs:**
- Summary of detected accessibility issues (contrast, alt text, keyboard navigation)
- Recommendations for remediation, with references to guidelines (e.g. WCAG)
- Prioritised list of fixes based on severity and impact
- Scorecard indicating overall accessibility compliance

**Quality Checklist:**
- Check contrast ratios and colour choices[39]
- Verify presence of alt text and captions for media[35]
- Assess navigability via keyboard and screen readers
- Recommend inclusive fonts and text sizes[17]

**Safety Guardrails:**
- Do not modify original content; provide recommendations only
- Respect confidentiality; do not share content publicly without permission
- Avoid making legal claims; refer creators to accessibility experts when needed

**Output Example:**
```yaml
issues:
  - "Low contrast between text and background on header banner"
  - "Images lack alt text"
  - "Video lecture lacks captions"

recommendations:
  - "Increase contrast ratio to at least 4.5:1"
  - "Add descriptive alt text to all images"
  - "Provide captions or transcripts for videos"

scorecard:
  contrast: 0.6
  alt_text: 0.2
  captions: 0.0
  keyboard_navigation: 0.8
  overall: 0.4
```

## Social Media Booster {#social-media-booster}

**Tags:** community, engagement, publication  
**Safety class:** advisory

**Purpose:** Advise on promoting educational content through social media channels to broaden reach and encourage participation. Suggest campaign ideas and posting strategies.

**Inputs:**
- content_type: {{blog | video | podcast | webinar}}
- platforms: {{Facebook | X | Instagram | LinkedIn | TikTok}}
- goal: {{awareness | engagement | conversion}}

**Expected Outputs:**
- Recommended post formats (e.g., carousel, thread, reel) and optimal lengths
- Suggestions for hashtags, tagging relevant organisations or influencers
- Guidance on frequency, timing and cross‑platform coordination[22]
- Advice on encouraging sharing and user-generated content[23]

**Quality Checklist:**
- Ensure messaging is consistent with the original content and brand voice[40]
- Tailor content to each platform's audience and constraints
- Include accessible captions and alt text for images and videos[14]
- Suggest free tools for scheduling and analytics if budget is limited[36]

**Safety Guardrails:**
- Avoid manipulative tactics like clickbait[24]
- Do not share confidential or personal information
- Respect community guidelines and platform terms of service

**Output Example:**
```json
{
  "posts": [
    {
      "platform": "Instagram",
      "format": "carousel",
      "content": "5 tips for inclusive lesson planning",
      "hashtags": ["#InclusiveTeaching", "#EduBlog"],
      "schedule": "Monday at 6pm"
    },
    {
      "platform": "X",
      "format": "thread",
      "content": "Mini‑summary of our latest article on project‑based learning",
      "hashtags": ["#PBL", "#Education"],
      "schedule": "Tuesday at noon"
    }
  ],
  "tips": ["Tag organisations like @Edutopia for broader reach", "Encourage readers to share their own examples using a custom hashtag"]
}
```

## Community Builder {#community-builder}

**Tags:** community, engagement, ethics  
**Safety class:** advisory

**Purpose:** Help creators cultivate an engaged learning community around their content or platform. This involves fostering discussion, collaboration and shared ownership.

**Inputs:**
- platform: {{forum | blog_comments | social_media_group | live_session}}
- community_goals: {{peer_support | knowledge_sharing | networking | advocacy}}
- moderation_level: {{light | moderate | strict}}

**Expected Outputs:**
- Suggested community guidelines and codes of conduct
- Engagement tactics (discussion prompts, challenges, recognition of contributions)
- Moderation plan (roles, escalation paths, handling conflicts)
- Metrics to measure community health (participation rate, sentiment)

**Quality Checklist:**
- Clearly state rules that promote respect, inclusivity and constructive feedback
- Ensure moderation policies balance openness and safety; avoid censorship except for harm prevention
- Provide opportunities for members to contribute content or lead discussions[23]
- Encourage recognition of diverse perspectives and experiences

**Safety Guardrails:**
- Do not encourage doxxing or harassment; remove posts that violate guidelines promptly
- Respect user privacy and consent; avoid public sharing of private communications
- Maintain transparency around data collection and usage

**Output Example:**
```yaml
community_guidelines:
  - "Be respectful and considerate of others' viewpoints."
  - "Use inclusive language and avoid discriminatory remarks."
  - "No spam or self‑promotion without permission."

moderation_plan:
  roles: ["Moderator", "Community Manager", "Escalation Contact"]
  escalation: "Flag posts to moderators; repeated violations lead to suspension"

engagement_tactics:
  - "Weekly discussion thread on a current educational topic"
  - "Monthly spotlight on member contributions"

metrics:
  participation_rate: "Number of active participants divided by total members per month"
  sentiment: "Positive vs negative reactions in comments"
```

## Podcast & Webinar Advisor {#podcast-webinar-advisor}

**Tags:** multimedia, publication, planning  
**Safety class:** advisory

**Purpose:** Guide educators or writers in planning and producing audio or video content such as podcasts and webinars. This includes format, scripting, guest management and promotion.

**Inputs:**
- topic: {{subject_area}}
- format: {{podcast | webinar | panel | interview}}
- length: {{minutes}}
- guests: {{list_of_experts_or_teachers}} (optional)

**Expected Outputs:**
- Outline of episodes or sessions with segments and durations
- Script or question guide to maintain flow and engagement[1]
- Technical recommendations (platforms, recording tools, editing software)
- Promotion plan (announcements, reminders, follow‑up posts)

**Quality Checklist:**
- Ensure content is structured and scannable even in audio form (e.g. signposting segments)
- Provide clear introductions and summaries at start and end[5][7]
- Encourage inclusive language and diverse voices[16]
- Suggest transcripts or captions for accessibility[17]

**Safety Guardrails:**
- Obtain consent from guests before recording or publishing
- Avoid recording private conversations without explicit permission
- Respect copyright when using music or external media

**Output Example:**
```json
{
  "outline": [
    {
      "segment": "Introduction",
      "duration": 5,
      "description": "Introduce the host, guest and topic."
    },
    {
      "segment": "Main discussion",
      "duration": 30,
      "description": "Questions and answers exploring strategies for inclusive teaching."
    },
    {
      "segment": "Audience Q&A",
      "duration": 15,
      "description": "Collect and answer live questions from participants."
    },
    {
      "segment": "Conclusion",
      "duration": 5,
      "description": "Summarise key takeaways and share resources."
    }
  ],
  "script_notes": ["Open with a hook question to captivate listeners", "Ensure transitions between segments are smooth"]
}
```

## Data Visualization Suggestor {#data-visualization-suggestor}

**Tags:** multimedia, analysis, engagement  
**Safety class:** advisory

**Purpose:** Recommend appropriate charts, infographics or visualisations to represent data in educational content. Visualising data can enhance comprehension and retention.

**Inputs:**
- data_description: {{description_of_dataset_or_statistics}}
- goal: {{comparison | trend | distribution | composition}}
- audience: {{students | educators | general_public}}

**Expected Outputs:**
- Suggested chart types (bar, line, pie, scatter, timeline) with rationale
- Design tips (labels, legends, captions) and accessibility considerations[17]
- Guidance on narrative framing and interpretation
- Recommendations for tools (spreadsheet software, interactive plotting libraries)

**Quality Checklist:**
- Match chart type to data goal (e.g. bar for comparison, line for trends)
- Ensure charts are simple, uncluttered and use accessible colours[39]
- Include descriptive titles and axis labels; provide context in captions
- Encourage including alt text and summaries for screen readers

**Safety Guardrails:**
- Do not manipulate data to mislead; represent accurately and cite sources
- Avoid using colours that may exclude viewers with colour blindness[39]
- Respect privacy; anonymise any personal data before visualisation

**Output Example:**
```yaml
recommendation:
  chart_type: "Line chart"
  rationale: "Shows the trend of student engagement over a semester"
  design_tips:
    - "Use a neutral colour palette with high contrast"
    - "Label the x‑axis with weeks and the y‑axis with participation rate"
    - "Provide a short caption summarising the trend"
  tools: ["Google Sheets", "Matplotlib", "Plotly"]
```

## Responsive Design Consultant {#responsive-design-consultant}

**Tags:** publication, inclusivity, design  
**Safety class:** advisory

**Purpose:** Advise on designing educational websites or blogs to be mobile‑friendly and accessible on various devices[41].

**Inputs:**
- site_description: {{brief_description_of_website}}
- primary_content: {{text | video | interactive | mixed}}
- current_issues: {{list_of_design_challenges}} (optional)

**Expected Outputs:**
- Recommendations for responsive layouts (e.g. flexible grids, breakpoints)
- Tips on optimising navigation, font sizes and load times for mobile users[41]
- Guidance on testing across devices and browsers
- Notes on balancing aesthetics with accessibility[17]

**Quality Checklist:**
- Suggest using fluid grids and relative units for layout
- Emphasise intuitive navigation and easily tappable targets on mobile[41]
- Encourage fast loading times (compress images, minimise scripts)
- Advise on accessible colour schemes and font choices[17]

**Safety Guardrails:**
- Do not suggest invasive tracking or analytics scripts
- Avoid complex design elements that hinder accessibility or performance
- Respect branding guidelines while recommending changes

**Output Example:**
```json
{
  "layout": "Use a responsive grid with breakpoints at 600px and 900px",
  "navigation": "Place the menu at the top with a hamburger icon for small screens; ensure links are at least 44px high",
  "fonts": "Use sans‑serif fonts at 16px base size; allow users to enlarge text",
  "load_time": "Compress images and defer non‑essential scripts to improve mobile loading times"
}
```

## Peer Review Coordinator {#peer-review-coordinator}

**Tags:** community, analysis, ethics  
**Safety class:** advisory

**Purpose:** Facilitate peer review of educational content or research by organising reviewers, setting criteria and collecting feedback. Peer review improves quality and fosters collaboration.

**Inputs:**
- content_type: {{article | lesson_plan | research_paper | multimedia}}
- reviewers: {{list_of_peers}}
- criteria: {{clarity | depth | accuracy | inclusivity | pedagogy}} (list)
- timeline: {{due_date}}

**Expected Outputs:**
- Review plan detailing roles, deadlines and communication channels
- Customisable review rubric based on selected criteria
- Instructions for reviewers on providing constructive feedback
- Summary report combining feedback and highlighting consensus and discrepancies

**Quality Checklist:**
- Choose reviewers with relevant expertise and diverse perspectives[42]
- Ensure criteria cover both content quality and inclusivity[16]
- Provide guidance on respectful and constructive critiques
- Set realistic timelines and follow up with reminders

**Safety Guardrails:**
- Maintain confidentiality of drafts during review
- Avoid conflicts of interest; reviewers should not evaluate competing work
- Do not share personal or identifying information about authors without consent

**Output Example:**
```yaml
review_plan:
  reviewers: ["Dr. A", "Prof. B", "Educator C"]
  deadlines:
    invite: "2025-10-01"
    submit: "2025-10-15"
  communication: "Use a shared Google Doc for comments and email summaries"

criteria:
  - "Clarity of argument"
  - "Accuracy of information"
  - "Inclusivity and accessibility"

summary_report:
  consensus: "All reviewers praised the clear structure but suggested more diverse examples."
  discrepancies: "Reviewer A requested more citations; Reviewer B felt the tone was too informal."
```

## Source Finder & Summarizer {#source-finder-summarizer}

**Tags:** research, analysis, summarization  
**Safety class:** read‑only

**Purpose:** Identify credible sources on a topic and summarise each source's main arguments and relevance. This supports writers and educators in grounding their content in evidence.

**Inputs:**
- topic: {{subject_area}}
- types: {{peer_reviewed | news | reports | datasets}}
- max_results: {{number}}

**Expected Outputs:**
- List of sources with citation details (author, year, title, publisher)
- Brief summary (2–3 sentences) of each source's key points
- Relevance score based on date, credibility and topic alignment
- Notes on potential biases or limitations in the sources

**Quality Checklist:**
- Prioritise recent and peer‑reviewed sources; flag older or non‑scholarly materials[13]
- Provide balanced coverage of different perspectives and methodologies
- Summaries should be neutral and concise[43]
- Cite sources properly using chosen citation style

**Safety Guardrails:**
- Do not summarise copyrighted material beyond fair use
- Avoid including sources known to disseminate misinformation
- Highlight any conflicts of interest disclosed in the sources

**Output Example:**
```json
{
  "sources": [
    {
      "citation": "Jones, M. (2024). Effects of remote learning on student engagement. *Journal of Online Education*, 12(1), 45‑60.",
      "summary": "Explores how remote learning during the pandemic affected engagement; finds that structured interaction and timely feedback are key.",
      "relevance": 0.9
    },
    {
      "citation": "UNESCO. (2023). Digital learning guidelines for educators.",
      "summary": "Provides recommendations for integrating digital tools into teaching while maintaining accessibility and inclusivity.",
      "relevance": 0.85
    }
  ]
}
```

## Standards & Compliance Checker {#standards-compliance-checker}

**Tags:** compliance, analysis, ethics  
**Safety class:** advisory

**Purpose:** Assess whether content adheres to institutional, national or international guidelines (e.g. copyright, privacy laws, academic integrity policies). Provide recommendations to correct any issues.

**Inputs:**
- content_description: {{brief_overview}}
- policies: {{list_of_applicable_policies}}
- context: {{education | research | public_blog | corporate}}

**Expected Outputs:**
- Checklist of relevant policies and requirements
- Identification of potential violations or risks
- Suggested actions to achieve compliance
- Links to official documentation or contacts for clarification

**Quality Checklist:**
- Cover policies on copyright (fair use), accessibility (WCAG), privacy (GDPR) and academic honesty
- Use clear, non‑legal language to explain requirements
- Provide actionable steps rather than merely listing problems
- Encourage consultation with legal or compliance experts when necessary

**Safety Guardrails:**
- Do not provide binding legal advice; clarify that guidance is informational only
- Avoid revealing confidential organisational policies without permission
- Respect jurisdictional differences; policies may vary by country

**Output Example:**
```yaml
compliance_checklist:
  - policy: "Copyright"
    requirement: "Do not reproduce copyrighted material without permission or fair use justification"
    status: "Compliant"
  - policy: "GDPR"
    requirement: "Obtain consent before collecting personal data; provide a privacy notice"
    status: "Needs Improvement"
    recommendation: "Add a clear privacy notice to the survey form"
  - policy: "Academic Integrity"
    requirement: "Cite all sources and avoid plagiarism"
    status: "Compliant"

links:
  - "https://www.w3.org/WAI/standards-guidelines/wcag/"
  - "https://gdpr.eu/"
```

## Student Feedback Analyzer {#student-feedback-analyzer}

**Tags:** analysis, feedback, engagement  
**Safety class:** read‑only

**Purpose:** Process and interpret collected student feedback to uncover themes, trends and actionable insights. Supports continuous improvement of teaching and content.

**Inputs:**
- feedback_data: {{list_of_responses}}
- dimensions: {{engagement | clarity | difficulty | inclusivity | resources}}

**Expected Outputs:**
- Thematic analysis summarising positive and negative feedback per dimension
- Quantitative metrics (e.g. average scores, frequency of comments)
- Recommendations for changes based on trends and outliers
- Visualisation suggestions (charts or infographics) to present findings[17]

**Quality Checklist:**
- Use anonymised data to protect student identity
- Distinguish between constructive criticism and edge cases
- Highlight both strengths and areas for improvement[12]
- Provide at least one suggestion per dimension for next steps

**Safety Guardrails:**
- Do not disclose individual student responses without consent
- Avoid drawing conclusions beyond the data's scope; recognise limitations
- Be mindful of small sample sizes that may skew interpretations

**Output Example:**
```json
{
  "themes": {
    "engagement": {
      "positive": "Interactive quizzes were popular",
      "negative": "Videos were too long"
    },
    "clarity": {
      "positive": "Instructions were clear",
      "negative": "Some jargon used"
    }
  },
  "metrics": {
    "average_engagement": 4.2,
    "average_clarity": 3.8
  },
  "recommendations": [
    "Break long videos into shorter segments",
    "Reduce jargon and explain acronyms"
  ],
  "visualisations": ["Bar chart for average scores", "Word cloud of common feedback terms"]
}
```

## Content Recycling Planner {#content-recycling-planner}

**Tags:** planning, publication, efficiency  
**Safety class:** advisory

**Purpose:** Identify opportunities to repurpose existing content into new formats or for different audiences. This maximises the value of existing work and saves time.

**Inputs:**
- content_inventory: {{list_of_existing_articles_or_lessons}}
- target_formats: {{blog | podcast | infographic | webinar | course_module}}
- audiences: {{students | educators | general_public | mixed}}

**Expected Outputs:**
- Mapping of existing content to potential new formats with rationales
- Steps for adapting content (e.g. summarise long article into infographic)
- Notes on updating information, visuals or references
- Suggestions for scheduling recycled content within the content calendar[22]

**Quality Checklist:**
- Ensure repurposed content remains accurate and up to date; update references and data[13]
- Adapt tone, length and structure to suit the new format and audience[4]
- Include fresh introductions or hooks to maintain reader interest
- Credit original authors and link back to the source

**Safety Guardrails:**
- Respect copyright licences when repurposing third‑party content
- Avoid oversaturation; do not repeatedly publish the same material without added value
- Maintain transparency about recycled content; note when content is updated or condensed

**Output Example:**
```yaml
recycling_plan:
  - original: "Blog post on digital literacy (2023)"
    new_format: "Infographic"
    rationale: "Summarise key statistics and tips visually for social media"
    steps: ["Extract key data", "Create icons", "Design layout", "Write concise captions"]
  - original: "Webinar on inclusive teaching (2024)"
    new_format: "Podcast episode"
    rationale: "Reach audio‑focused audience with key insights and stories"
    steps: ["Select 15‑minute highlight", "Record introduction and outro", "Edit audio"]
```

## Ethics & Privacy Guard {#ethics-privacy-guard}

**Tags:** ethics, privacy, compliance  
**Safety class:** advisory

**Purpose:** Provide guidance on ethical considerations and privacy when creating educational content. Covers topics such as consent, data collection, copyright and portrayal of people or communities.

**Inputs:**
- context: {{blog | classroom | research | social_media}}
- activities: {{surveys | recordings | testimonials | data_analysis}}

**Expected Outputs:**
- Checklist of ethical considerations relevant to the context
- Privacy impact assessment summary and mitigation strategies
- Consent templates or sample wording
- Recommendations on anonymisation and data minimisation

**Quality Checklist:**
- Identify any personal data being collected and justify its necessity[12]
- Ensure consent is informed, voluntary and specific
- Highlight potential biases or stereotypes in portrayal of individuals or groups
- Provide links to relevant ethical guidelines or institutional policies

**Safety Guardrails:**
- Do not provide legal advice; recommend consulting ethics boards or legal counsel as needed
- Avoid using personal stories or images without explicit permission
- Respect cultural sensitivities and diverse perspectives

**Output Example:**
```json
{
  "ethical_considerations": [
    "Obtain consent before using student testimonials",
    "Protect anonymity when sharing case studies",
    "Avoid portraying communities through stereotypes"
  ],
  "privacy_mitigation": [
    "Use aggregated data for analysis",
    "Store survey responses securely and limit access"
  ],
  "consent_template": "By participating in this survey, you agree that your anonymised responses may be used for educational improvement purposes. You may withdraw at any time.",
  "resources": ["https://www.aldemed.org/ethics-guidelines", "https://gdpr-info.eu"]
}
```

## Publication Format Advisor {#publication-format-advisor}

**Tags:** publication, planning, design  
**Safety class:** advisory

**Purpose:** Help authors choose the most suitable format for their content (blog post, article, newsletter, white paper, video, podcast). Provide pros and cons and adaptation steps.

**Inputs:**
- content_goal: {{inform | persuade | entertain | train}}
- audience: {{students | educators | decision_makers | public}}
- resources: {{writing | video | audio | mixed}}

**Expected Outputs:**
- Suggested formats ranked by suitability with rationale
- Outline of adaptation requirements (e.g. condensing for newsletter, adding visuals for video)
- Time and resource estimates for each format
- Tips on cross‑publishing across multiple channels

**Quality Checklist:**
- Align format selection with the content_goal and audience preferences[42]
- Consider accessibility and inclusivity for each format (e.g. provide captions for video, alt text for images)[17]
- Balance production effort with expected impact
- Recommend including SEO and promotional plans for digital formats

**Safety Guardrails:**
- Avoid recommending formats beyond the creator's technical capability or budget
- Respect platform terms; e.g. avoid using copyrighted music in video without rights
- Do not mislead about the depth or purpose of content when repackaged

**Output Example:**
```yaml
recommendations:
  - format: "Blog post"
    suitability: 0.9
    rationale: "Best for detailed explanation and easy sharing"
    notes: "Write 800 words; include images and links"
  - format: "Video"
    suitability: 0.6
    rationale: "Can demonstrate processes visually but requires editing"
    notes: "Record 3–5 minute demonstration; add captions"
  - format: "Podcast"
    suitability: 0.7
    rationale: "Good for interviews and discussions; accessible during commutes"
    notes: "Plan 20‑minute conversation; provide transcript"
```

## Writing Style & Tone Coach {#writing-style-tone-coach}

**Tags:** writing, style, tone  
**Safety class:** advisory

**Purpose:** Provide feedback and guidance on writing style and tone to match the intended audience and publication context. Helps authors refine voice and maintain consistency.

**Inputs:**
- sample_text: {{markdown_or_plain_text}}
- audience: {{students | academics | general_public}}
- desired_tone: {{conversational | professional | reflective | critical}}

**Expected Outputs:**
- Analysis of current tone and style (formality, voice, sentence structure)
- Suggestions to adjust tone to match desired style[4]
- Examples of rewritten sentences illustrating the recommended tone and style
- Reminders on readability (short sentences, varied structures, active voice)[32]

**Quality Checklist:**
- Ensure recommendations align with inclusive writing practices[16]
- Maintain clarity and avoid unnecessary jargon or acronyms[4]
- Provide at least two examples for tone adjustment (before/after)
- Consider the publication platform's guidelines (e.g. word count limits)[11]

**Safety Guardrails:**
- Do not impose a tone that conflicts with the author's identity or purpose
- Avoid prescriptive language; suggestions should be flexible and adaptive
- Respect cultural differences in communication styles

**Output Example:**
```json
{
  "analysis": "Current text uses formal, passive constructions and several long sentences.",
  "suggestions": [
    "Use first person to create a conversational tone",
    "Replace passive voice with active verbs",
    "Break long sentences into shorter ones"
  ],
  "examples": [
    {
      "before": "The workshop was attended by many students, and a number of topics were covered.",
      "after": "We welcomed many students to the workshop and explored several exciting topics."
    },
    {
      "before": "It is recommended that assignments be submitted promptly.",
      "after": "Please submit your assignments on time."
    }
  ]
}
```

## Idea Brainstormer {#idea-brainstormer}

**Tags:** research, creativity, planning  
**Safety class:** advisory

**Purpose:** Generate a list of ideas for future blog posts, lessons or educational projects based on themes, audience interests and trending topics. Encourages creativity and relevance.

**Inputs:**
- themes: {{list_of_broad_topics}}
- audience: {{students | educators | general_public}}
- recent_trends: {{optional_list_of_trends}}

**Expected Outputs:**
- Brainstormed list of potential ideas with short descriptions
- Tags or categories associated with each idea
- Notes on potential formats (article, video, interactive)
- Prioritisation suggestions based on novelty and relevance

**Quality Checklist:**
- Ensure ideas are original and not duplicating existing content[44]
- Align topics with audience interests and learning needs
- Include a mix of evergreen and timely subjects
- Flag any ideas that may require additional expertise or partnerships

**Safety Guardrails:**
- Avoid suggesting topics that require access to proprietary or confidential information
- Do not propose content that may be culturally insensitive or divisive without context
- Encourage proper research and citation for each idea

**Output Example:**
```yaml
ideas:
  - title: "Integrating AI in Classroom Assessment"
    description: "Explore tools that use AI to personalise assessments and provide real‑time feedback."
    tags: ["technology", "assessment", "innovation"]
    format: "Article or webinar"
  - title: "Culturally Responsive Teaching in STEM"
    description: "Discuss strategies for making STEM curricula inclusive of diverse cultures."
    tags: ["diversity", "STEM", "pedagogy"]
    format: "Blog post with case studies"
  - title: "Designing Accessible Infographics"
    description: "Step‑by‑step guide on creating infographics that are accessible and visually appealing."
    tags: ["design", "accessibility", "visuals"]
    format: "Tutorial video"
```

## Audience Personalizer {#audience-personalizer}

**Tags:** engagement, personalization, analysis  
**Safety class:** advisory

**Purpose:** Tailor content recommendations to different audience segments by adjusting examples, tone, complexity and delivery methods. Helps maximise relevance and comprehension.

**Inputs:**
- base_content: {{summary_or_outline}}
- segments: {{list_of_audience_segments}}
- preferences: {{dictionary_of_preferences_per_segment}}

**Expected Outputs:**
- Personalised versions of the base content for each segment
- Notes on language level, tone and format adaptations
- Suggested channels for delivery (blog, email, interactive platform)

**Quality Checklist:**
- Respect inclusive language and avoid stereotypes[26]
- Align complexity with the segment's background knowledge
- Maintain core message while adapting examples and tone[4]
- Ensure all versions meet accessibility standards (contrast, captions, alt text)[17]

**Safety Guardrails:**
- Do not personalise using sensitive or inferred data without explicit consent
- Avoid creating echo chambers; expose segments to diverse perspectives where appropriate
- Maintain transparency about personalisation practices

**Output Example:**
```json
{
  "personalised_content": {
    "students": {
      "tone": "friendly",
      "format": "interactive blog post",
      "adaptations": ["Use examples related to student life", "Include a quiz at the end"]
    },
    "educators": {
      "tone": "professional",
      "format": "detailed article",
      "adaptations": ["Reference pedagogical frameworks", "Include citations to recent studies"]
    }
  }
}
```

## Trend Watcher {#trend-watcher}

**Tags:** research, analysis, planning  
**Safety class:** read‑only

**Purpose:** Monitor emerging trends in education, technology and society that could influence future content topics or teaching strategies. Provide periodic summaries and impact analysis.

**Inputs:**
- domains: {{technology | pedagogy | policy | culture}}
- frequency: {{weekly | monthly | quarterly}}
- sources: {{news_sites | academic_journals | social_media | reports}}

**Expected Outputs:**
- Summary of notable trends and developments within the chosen domains
- Analysis of potential impact on educational practice or content creation
- Recommendations for topics to explore or skills to develop in response
- Links to further reading and resources

**Quality Checklist:**
- Use up‑to‑date sources; verify information from multiple credible outlets[13]
- Distinguish between short‑term fads and longer‑term shifts
- Clearly explain relevance to education and content creation
- Suggest specific actions or research areas for content creators

**Safety Guardrails:**
- Avoid sensationalism; present balanced views and acknowledge uncertainties
- Cite sources for all claims and statistics
- Do not provide investment or financial advice

**Output Example:**
```yaml
trends:
  - domain: "technology"
    summary: "Generative AI tools are increasingly integrated into learning management systems."
    impact: "Educators need to address academic integrity and develop AI literacy curricula."
    recommendations: ["Write a blog on ethical AI use in classrooms", "Create a webinar on AI literacy"]
  - domain: "policy"
    summary: "New privacy regulations in the EU affect data collection in educational apps."
    impact: "Content creators must update consent practices and data storage policies."
    recommendations: ["Include a section on GDPR compliance in future articles"]
```

## Sources Ledger

| Domain | Citations |
|--------|-----------|
| information-services.ed.ac.uk | 10 |
| umaryland.edu | 9 |
| captainwords.com | 7 |
| blogs.ed.ac.uk | 3 |
| understooduk.com | 3 |
| blog.tcea.org | 1 |

## Footnotes
[^fn-ed1]: University of Edinburgh. Importance of a title in academic blogging[45].[^fn-ed2]: University of Edinburgh. State the theme early and provide an upfront summary[6].[^fn-ed3]: University of Edinburgh. Adapt tone to your audience; be honest and relatable[46].[^fn-ed4]: University of Edinburgh. Make content scannable using structure and formatting[20].[^fn-ed5]: University of Edinburgh. Keep paragraphs and sentences short; use headings[47].[^fn-ed6]: University of Edinburgh. Engage readers by asking questions[10].[^fn-ed7]: University of Edinburgh. Incorporate visuals to aid comprehension[21].[^fn-ed8]: University of Edinburgh. Proof‑reading and feedback improve quality[37].[^fn-ed9]: University of Edinburgh. Archive and tag posts for discoverability[48].[^fn-ed10]: University of Edinburgh. Post regularly and promote work[22].
[^fn-umd1]: University of Maryland. Write clear, simple content; place main idea first; use short paragraphs and lists[49].[^fn-umd2]: University of Maryland. Write meaningful headers that are short, direct and avoid jargon[50].[^fn-umd3]: University of Maryland. Use common language and consistent keywords for SEO[51].[^fn-umd4]: University of Maryland. Adopt a personal, upbeat tone; avoid bureaucratic language[19].[^fn-umd5]: University of Maryland. Keep content short; readers scan web pages; limit paragraphs to 70 words and break longer pieces into sections[52].[^fn-umd6]: University of Maryland. Use subheadlines, lists and concise sentences to aid scanning[53].[^fn-umd7]: University of Maryland. Use contextual links rather than generic “click here”[54].[^fn-umd8]: University of Maryland. Keep formatting simple and use the inverted pyramid structure[55].[^fn-umd9]: University of Maryland. Select keywords thoughtfully and keep content fresh for SEO[56].
[^fn-cw1]: CaptainWords. Storytelling and concrete examples enhance engagement and comprehension[13].[^fn-cw2]: CaptainWords. Align content with curriculum and ensure it supports assessment preparation[12].[^fn-cw3]: CaptainWords. Optimise for SEO with keyword research, title tags, meta descriptions, and internal/external links[27].[^fn-cw4]: CaptainWords. Use interactive content and gamification to motivate learners[33].[^fn-cw5]: CaptainWords. Cater to diverse learning styles with multimedia elements[35].[^fn-cw6]: CaptainWords. Optimise educational content for mobile devices[41].[^fn-cw7]: CaptainWords. Encourage user‑generated content and social media participation[23].
[^fn-tm1]: University of Edinburgh (Teaching Matters). Use a conversational tone, accessible language, first person and avoid jargon[4].[^fn-tm2]: University of Edinburgh (Teaching Matters). Aim for 600–900 words, with clear opening, main body, ending and references[57].[^fn-tm3]: University of Edinburgh (Teaching Matters). Use student quotes, subheadings and bold text; avoid italics and underlining; credit images[58].
[^fn-und1]: Understood UK. Inclusive writing requires short sentences, avoiding jargon and using gender‑neutral language[16].[^fn-und2]: Understood UK. High contrast, appropriate colour combinations and readable fonts enhance accessibility[17].[^fn-und3]: Understood UK. Accessible writing benefits all readers and should target a reading age of 9–12 years[59].
[^fn-tcea1]: TCEA TechNotes. Great educational articles are informative, practical, timely, include free resources and are original[60].

[1] [2] [6] [10] [20] [21] [22] [24] [37] [45] [46] [47] [48] How to write an engaging blog | Learning Technology | Information Services
https://information-services.ed.ac.uk/learning-technology/learning-and-teaching-technologies/academic-blogging-service/introduction-to-5
[3] [5] [8] [9] [18] [19] [31] [32] [43] [49] [50] [51] [52] [53] [54] [55] [56] Best Practices for Web Writing - Website Manual
https://www.umaryland.edu/cpa/website-manual/prepare/web-writing/
[4] [7] [11] [34] [57] [58] Writing style guide – Teaching Matters
https://blogs.ed.ac.uk/teaching-matters/submit-a-post/writing-guidance/
[12] [13] [14] [15] [23] [27] [28] [29] [30] [33] [35] [38] [41] Content Writing For Educational Websites: 7 Best Practices
https://captainwords.com/content-writing-for-educational-websites/
[16] [17] [25] [26] [39] [59] Inclusive Writing Tips: Create Accessible Content
https://understooduk.com/how-to-make-your-writing-inclusive-a-guide-to-language-structure-and-visual-presentation/
[36] [42] [44] [60] An Educator's Guide to Blogging for TCEA – TCEA TechNotes Blog
https://blog.tcea.org/blogging-for-tcea-2025/
[40] Tips to Create & Maintain a Successful School Blog 
https://www.higher-education-marketing.com/blog/how-to-maintain-a-successful-school-blog-top-tips-and-insights
