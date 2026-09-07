# Resume/JD Matcher — Project Plan

## Project Goal

Build an NLP-powered Resume/JD Matcher that analyzes a candidate's resume against a job description and produces an explainable ATS-style compatibility score and improvement suggestions.

---

# Phase 1 — Project Foundation

- [ ] Create clean Python project structure
- [ ] Add dependency management
- [ ] Add `.gitignore`
- [ ] Add configuration system
- [ ] Add basic application entry point
- [ ] Add logging
- [ ] Add initial testing structure

# Phase 2 — Resume Input

- [ ] Support PDF resumes
- [ ] Support DOCX resumes
- [ ] Extract raw text
- [ ] Handle corrupted/empty files
- [ ] Add resume extraction tests

# Phase 3 — Job Description Input

- [ ] Accept job descriptions
- [ ] Clean job-description text
- [ ] Add JD preprocessing
- [ ] Add JD validation
- [ ] Add tests

# Phase 4 — Text Processing

- [ ] Normalize text
- [ ] Sentence/word processing
- [ ] Remove unnecessary noise
- [ ] Detect resume sections
- [ ] Detect JD sections
- [ ] Create reusable NLP preprocessing utilities

# Phase 5 — Entity and Skill Extraction

- [ ] Integrate spaCy
- [ ] Extract organizations
- [ ] Extract education-related information
- [ ] Extract experience-related information
- [ ] Extract technical skills
- [ ] Extract soft skills
- [ ] Build normalized skill representation
- [ ] Add extraction tests

# Phase 6 — Baseline Matching

- [ ] Implement keyword matching
- [ ] Calculate skill overlap
- [ ] Identify matched skills
- [ ] Identify missing skills
- [ ] Create initial matching score
- [ ] Add scoring tests

# Phase 7 — Statistical NLP Matching

- [ ] Implement TF-IDF representation
- [ ] Implement TF-IDF similarity
- [ ] Compare TF-IDF score with keyword score
- [ ] Add tests
- [ ] Document limitations

# Phase 8 — Semantic Matching

- [ ] Evaluate sentence-embedding models
- [ ] Add sentence-transformers support
- [ ] Generate resume embeddings
- [ ] Generate JD embeddings
- [ ] Implement cosine similarity
- [ ] Compare semantic similarity against baseline
- [ ] Add tests

# Phase 9 — Explainable ATS Scoring

- [ ] Design weighted scoring system
- [ ] Combine skill matching and semantic similarity
- [ ] Account for experience relevance
- [ ] Account for education relevance where appropriate
- [ ] Generate score breakdown
- [ ] Add score validation
- [ ] Add tests

# Phase 10 — Improvement Suggestions

- [ ] Detect missing skills
- [ ] Detect weak resume sections
- [ ] Suggest relevant skills
- [ ] Suggest improvements to resume content
- [ ] Explain score reductions
- [ ] Add suggestion tests

# Phase 11 — Multiple Job Descriptions

- [ ] Support multiple JDs
- [ ] Calculate score for each JD
- [ ] Rank JDs
- [ ] Generate comparison report
- [ ] Add tests

# Phase 12 — API

- [ ] Design API structure
- [ ] Add resume upload endpoint
- [ ] Add JD input endpoint
- [ ] Add matching endpoint
- [ ] Add result schema
- [ ] Add API tests
- [ ] Add error handling

# Phase 13 — User Interface

- [ ] Design simple interface
- [ ] Resume upload
- [ ] JD input/upload
- [ ] Score display
- [ ] Matched skills display
- [ ] Missing skills display
- [ ] Suggestions display
- [ ] Multiple-JD comparison

# Phase 14 — Quality

- [ ] Increase test coverage
- [ ] Improve error handling
- [ ] Add input validation
- [ ] Add performance checks
- [ ] Improve documentation
- [ ] Add example inputs
- [ ] Add example outputs
- [ ] Document architecture
- [ ] Document scoring methodology

# Phase 15 — Portfolio Readiness

- [ ] Improve README
- [ ] Add architecture diagram
- [ ] Add installation instructions
- [ ] Add usage examples
- [ ] Add screenshots
- [ ] Document NLP techniques
- [ ] Document limitations
- [ ] Document future improvements
- [ ] Add project demo instructions
