\# AI Resume Analyzer



An intelligent talent screening tool powered by Machine Learning and Natural Language Processing (NLP). Automatically analyzes resumes, extracts key information, and provides a comprehensive scoring system.



\## Features



✅ \*\*Contact Information Extraction\*\*

\- Extract emails, phone numbers

\- Identify LinkedIn and GitHub profiles

\- Verify complete contact details



✅ \*\*Skill Recognition\*\*

\- Programming languages detection

\- Framework and technology identification

\- Database and tools recognition

\- Soft skills assessment



✅ \*\*Education Analysis\*\*

\- Degree extraction

\- Educational qualification identification

\- Academic background assessment



✅ \*\*Experience Evaluation\*\*

\- Years of experience calculation

\- Action verb counting

\- Achievement measurement

\- Experience level categorization



✅ \*\*Resume Scoring System\*\*

\- Comprehensive scoring algorithm (0-100)

\- Multi-factor evaluation

\- Quality assessment

\- Comparative ranking



✅ \*\*Automated Reporting\*\*

\- Detailed analysis reports

\- Actionable recommendations

\- JSON export capability

\- Performance metrics



\## Requirements



\- Python 3.7+

\- No external ML libraries required (uses regex and NLP patterns)



\## Installation



1\. \*\*Clone the repository\*\*

```bash

git clone https://github.com/WangilaWakhongola/ai-resume-analyzer.git

cd ai-resume-analyzer

```



2\. \*\*Create a virtual environment (optional)\*\*

```bash

python -m venv venv



\# On Windows:

venv\\Scripts\\activate



\# On macOS/Linux:

source venv/bin/activate

```



3\. \*\*Install dependencies\*\*

```bash

pip install -r requirements.txt

```



\## Usage



\### Basic Usage



```bash

python resume\_analyzer.py

```



Then enter the path to your resume file (must be `.txt` format):

```

Enter the path to your resume (.txt file): /path/to/resume.txt

```



\### Output Files



The tool generates three output files:



1\. \*\*Console Report\*\* - Formatted analysis displayed in terminal

2\. \*\*Text Report\*\* - Saved as `resume\_analysis\_report.txt`

3\. \*\*JSON Data\*\* - Saved as `resume\_analysis.json` for programmatic access



\### Example Report



```

================================================================================

AI RESUME ANALYZER - DETAILED REPORT

================================================================================



RESUME SCORE: 87.50/100



CONTACT INFORMATION:

&nbsp; Emails: john@example.com

&nbsp; Phones: (123) 456-7890

&nbsp; LinkedIn: linkedin.com/in/johndoe

&nbsp; GitHub: github.com/johndoe



TECHNICAL SKILLS:

&nbsp; Programming Languages: Python, Java, JavaScript, SQL

&nbsp; Frameworks: Django, React, Flask

&nbsp; Databases: PostgreSQL, MongoDB

&nbsp; Tools \& Platforms: Git, Docker, AWS



EXPERIENCE:

&nbsp; Years of Experience: 5

&nbsp; Action Verbs Found: 23

&nbsp; Top Action Verbs: Developed(5), Implemented(4), Led(3)



RECOMMENDATIONS:

&nbsp; ✓ Your resume looks great! Keep it polished and updated.

```



\## How It Works



\### ResumeAnalyzer Class



\#### Methods:



\- \*\*extract\_text\_from\_resume()\*\* - Reads resume file

\- \*\*extract\_contact\_info()\*\* - Extracts emails, phones, LinkedIn, GitHub

\- \*\*extract\_skills()\*\* - Identifies technical and soft skills

\- \*\*extract\_education()\*\* - Finds education credentials

\- \*\*extract\_experience\_years()\*\* - Calculates years of experience

\- \*\*count\_action\_verbs()\*\* - Counts achievement-related verbs

\- \*\*calculate\_resume\_score()\*\* - Generates overall quality score

\- \*\*analyze\_resume()\*\* - Performs complete analysis

\- \*\*generate\_report()\*\* - Creates formatted report



\### Scoring Algorithm



The resume score is calculated based on:



| Factor | Max Points | Criteria |

|--------|-----------|----------|

| Contact Info | 10 | Email, Phone, LinkedIn, GitHub |

| Technical Skills | 25 | Programming, Frameworks, Databases, Tools |

| Education | 15 | Degree detection |

| Experience | 20 | Years of professional experience |

| Action Verbs | 15 | Strong achievement keywords |

| Content Length | 15 | Word count (300+ words ideal) |

| \*\*Total\*\* | \*\*100\*\* | \*\*Overall Quality Score\*\* |



\## Project Structure



```

ai-resume-analyzer/

├── resume\_analyzer.py      # Main application

├── requirements.txt        # Dependencies

├── README.md              # This file

├── .gitignore            # Git ignore file

└── sample\_resume.txt     # Example resume

```



\## Supported Features



\### Skills Database



\*\*Programming Languages:\*\*

Python, Java, JavaScript, C++, C#, PHP, Ruby, Go, Rust, Swift, Kotlin, TypeScript, Scala, R, MATLAB, HTML, CSS, SQL, Bash, PowerShell



\*\*Frameworks:\*\*

Django, Flask, FastAPI, Spring, React, Angular, Vue, Node.js, Express, AWS, Azure, GCP, Docker, Kubernetes, TensorFlow, PyTorch, scikit-learn, Pandas, NumPy



\*\*Databases:\*\*

MySQL, PostgreSQL, MongoDB, Redis, Elasticsearch, Oracle, SQLite, Cassandra, DynamoDB



\*\*Tools \& Platforms:\*\*

Git, Jenkins, GitLab, GitHub, JIRA, Linux, Windows, macOS, VS Code, IntelliJ, Postman



\### Use Cases



\- \*\*HR Departments\*\* - Automated candidate screening

\- \*\*Recruitment Agencies\*\* - Bulk resume analysis

\- \*\*Job Applicants\*\* - Resume quality feedback

\- \*\*Career Coaching\*\* - Professional development guidance

\- \*\*Talent Management\*\* - Workforce capability assessment



\## Resume Format Requirements



\- \*\*Supported Format:\*\* `.txt` (plain text)

\- \*\*Encoding:\*\* UTF-8

\- \*\*Content:\*\* Clear, structured text format



\### Converting to TXT Format



\- \*\*From PDF:\*\* Use online converters or Adobe Acrobat

\- \*\*From DOCX:\*\* Save as "Plain Text" in Microsoft Word

\- \*\*From Google Docs:\*\* Download → Convert to TXT



\## Example Input



```

John Doe

john@example.com | (123) 456-7890

LinkedIn: linkedin.com/in/johndoe

GitHub: github.com/johndoe



PROFESSIONAL EXPERIENCE



Senior Software Engineer - Tech Company (2020-Present)

• Led development of microservices architecture using Django and Docker

• Implemented CI/CD pipeline reducing deployment time by 60%

• Mentored team of 5 junior developers



TECHNICAL SKILLS

Programming: Python, JavaScript, SQL, Java

Frameworks: Django, React, Flask, Spring

Databases: PostgreSQL, MongoDB, Redis

Tools: Git, Docker, Kubernetes, AWS



EDUCATION

Bachelor of Science in Computer Science

University Name, 2018

```



\## Command Line Options



Basic usage with default settings:

```bash

python resume\_analyzer.py

```



\## Performance



\- \*\*Analysis Time:\*\* < 1 second per resume

\- \*\*Memory Usage:\*\* Minimal (< 10MB)

\- \*\*Accuracy:\*\* High for standard resume formats

\- \*\*Scalability:\*\* Process multiple resumes sequentially



\## Limitations



\- Currently supports `.txt` format (more formats in future)

\- Best results with structured resumes

\- Accuracy depends on resume quality

\- Custom skills may not be detected



\## Future Enhancements



\- \[ ] PDF and DOCX support

\- \[ ] Machine Learning-based skill extraction

\- \[ ] Deep learning for education detection

\- \[ ] Web interface with Flask/Django

\- \[ ] Batch processing multiple resumes

\- \[ ] Skill matching with job descriptions

\- \[ ] Resume comparison and ranking

\- \[ ] ATS optimization suggestions

\- \[ ] Real-time feedback system

\- \[ ] API endpoint deployment



\## Technologies Used



\- \*\*Python 3\*\* - Core programming language

\- \*\*Regular Expressions\*\* - Pattern matching and extraction

\- \*\*Natural Language Processing\*\* - Text analysis

\- \*\*JSON\*\* - Data serialization



\## Contributing



Contributions are welcome! Please feel free to submit pull requests or open issues.



\## License



This project is open source and available for educational and commercial use.



\## Author



Emmanuel Wakhongola

\- GitHub: \[@WangilaWakhongola](https://github.com/WangilaWakhongola)

\- Email: wangilaemmanuel06@gmail.com



\## Contact \& Support



For questions, issues, or feature requests, please open an issue on GitHub or contact me directly.



---



\*\*Last Updated:\*\* January 2025

\*\*Version:\*\* 1.0.0



\## Disclaimer



This tool is designed to assist in resume screening but should not be the sole factor in hiring decisions. Always conduct thorough human review of candidates.

"# -AI-Resume-Analyzer" 
