import re
import os
from datetime import datetime
from collections import Counter
import json

class ResumeAnalyzer:
    """AI-powered resume analyzer using NLP techniques"""
    
    def __init__(self):
        """Initialize the resume analyzer"""
        self.skills_database = {
            'programming': [
                'python', 'java', 'javascript', 'c++', 'c#', 'php', 'ruby', 'go',
                'rust', 'swift', 'kotlin', 'typescript', 'scala', 'r', 'matlab',
                'html', 'css', 'sql', 'bash', 'powershell'
            ],
            'frameworks': [
                'django', 'flask', 'fastapi', 'spring', 'react', 'angular', 'vue',
                'nodejs', 'express', 'aws', 'azure', 'gcp', 'docker', 'kubernetes',
                'tensorflow', 'pytorch', 'sklearn', 'pandas', 'numpy'
            ],
            'databases': [
                'mysql', 'postgresql', 'mongodb', 'redis', 'elasticsearch',
                'oracle', 'sqlite', 'cassandra', 'dynamodb'
            ],
            'tools': [
                'git', 'jenkins', 'gitlab', 'github', 'jira', 'linux', 'windows',
                'macos', 'vim', 'vscode', 'intellij', 'postman'
            ],
            'soft_skills': [
                'leadership', 'communication', 'teamwork', 'problem-solving',
                'project management', 'analytical', 'creative', 'adaptability',
                'collaboration', 'time management'
            ]
        }
        
        self.experience_keywords = [
            'developed', 'designed', 'implemented', 'managed', 'led', 'created',
            'built', 'deployed', 'optimized', 'improved', 'enhanced', 'engineered',
            'architected', 'mentored', 'coordinated', 'directed'
        ]
    
    def extract_text_from_resume(self, file_path):
        """Extract text from resume file"""
        try:
            if file_path.endswith('.txt'):
                with open(file_path, 'r', encoding='utf-8') as f:
                    return f.read()
            else:
                raise ValueError("Currently supports .txt files. Please convert your resume to .txt format.")
        except FileNotFoundError:
            raise FileNotFoundError(f"Resume file not found: {file_path}")
    
    def extract_contact_info(self, text):
        """Extract contact information from resume"""
        contact = {
            'emails': [],
            'phones': [],
            'linkedin': None,
            'github': None
        }
        
        # Extract emails
        emails = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', text)
        contact['emails'] = list(set(emails))
        
        # Extract phone numbers
        phones = re.findall(r'[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}', text)
        contact['phones'] = list(set(phones))
        
        # Extract LinkedIn
        linkedin = re.findall(r'linkedin\.com/in/[\w\-]+', text, re.IGNORECASE)
        if linkedin:
            contact['linkedin'] = linkedin[0]
        
        # Extract GitHub
        github = re.findall(r'github\.com/[\w\-]+', text, re.IGNORECASE)
        if github:
            contact['github'] = github[0]
        
        return contact
    
    def extract_skills(self, text):
        """Extract skills from resume"""
        text_lower = text.lower()
        found_skills = {
            'programming': [],
            'frameworks': [],
            'databases': [],
            'tools': [],
            'soft_skills': []
        }
        
        for category, skills in self.skills_database.items():
            for skill in skills:
                if skill in text_lower:
                    found_skills[category].append(skill.title())
        
        # Remove duplicates
        for category in found_skills:
            found_skills[category] = list(set(found_skills[category]))
        
        return found_skills
    
    def extract_education(self, text):
        """Extract education information"""
        education = []
        
        # Degree patterns
        degree_patterns = [
            r"Bachelor['\s]?s?\s+(?:of\s+)?(?:Science|Arts|Engineering|Technology|Computer Science)",
            r"Master['\s]?s?\s+(?:of\s+)?(?:Science|Arts|Engineering|Technology|Computer Science)",
            r"Ph\.?D\.?\s+(?:in\s+)?[\w\s]+",
            r"B\.?S\.?\s+(?:in\s+)?[\w\s]+",
            r"M\.?S\.?\s+(?:in\s+)?[\w\s]+",
            r"B\.?A\.?\s+(?:in\s+)?[\w\s]+",
            r"M\.?A\.?\s+(?:in\s+)?[\w\s]+"
        ]
        
        for pattern in degree_patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            education.extend(matches)
        
        return list(set(education))
    
    def extract_experience_years(self, text):
        """Calculate years of experience from resume"""
        years_patterns = [
            r'(\d+)\+?\s+years?\s+(?:of\s+)?experience',
            r'(\d+)\s+years?\s+(?:of\s+)?professional',
            r'total experience[\s:]*(\d+)\s+years?'
        ]
        
        for pattern in years_patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return int(match.group(1))
        
        return 0
    
    def count_action_verbs(self, text):
        """Count action verbs (indicators of strong accomplishments)"""
        text_lower = text.lower()
        verb_count = {}
        
        for verb in self.experience_keywords:
            count = len(re.findall(r'\b' + verb + r'\b', text_lower))
            if count > 0:
                verb_count[verb.title()] = count
        
        return verb_count
    
    def calculate_resume_score(self, analysis):
        """Calculate overall resume quality score (0-100)"""
        score = 0
        
        # Contact information (10 points)
        contact_score = 0
        if analysis['contact_info']['emails']:
            contact_score += 3
        if analysis['contact_info']['phones']:
            contact_score += 3
        if analysis['contact_info']['linkedin']:
            contact_score += 2
        if analysis['contact_info']['github']:
            contact_score += 2
        score += contact_score
        
        # Skills (25 points)
        total_skills = sum(len(v) for v in analysis['skills'].values())
        skills_score = min(25, (total_skills / 20) * 25)
        score += skills_score
        
        # Education (15 points)
        if analysis['education']:
            score += 15
        
        # Experience (20 points)
        years = analysis['years_of_experience']
        if years >= 5:
            score += 20
        elif years >= 3:
            score += 15
        elif years >= 1:
            score += 10
        else:
            score += 5
        
        # Action verbs (15 points)
        verb_count = sum(analysis['action_verbs'].values())
        action_verb_score = min(15, (verb_count / 10) * 15)
        score += action_verb_score
        
        # Length and content (15 points)
        word_count = len(analysis['word_count'])
        if word_count >= 300:
            score += 15
        elif word_count >= 200:
            score += 10
        else:
            score += 5
        
        return round(score, 2)
    
    def analyze_resume(self, file_path):
        """Perform complete resume analysis"""
        # Extract text
        resume_text = self.extract_text_from_resume(file_path)
        
        # Perform analysis
        analysis = {
            'timestamp': datetime.now().isoformat(),
            'filename': os.path.basename(file_path),
            'contact_info': self.extract_contact_info(resume_text),
            'skills': self.extract_skills(resume_text),
            'education': self.extract_education(resume_text),
            'years_of_experience': self.extract_experience_years(resume_text),
            'action_verbs': self.count_action_verbs(resume_text),
            'word_count': len(resume_text.split())
        }
        
        # Calculate score
        analysis['resume_score'] = self.calculate_resume_score(analysis)
        
        return analysis
    
    def generate_report(self, analysis):
        """Generate formatted analysis report"""
        report = f"""
{'='*80}
AI RESUME ANALYZER - DETAILED REPORT
{'='*80}

File: {analysis['filename']}
Generated: {analysis['timestamp']}

{'─'*80}
RESUME SCORE: {analysis['resume_score']}/100
{'─'*80}

CONTACT INFORMATION:
{'-'*80}
  Emails: {', '.join(analysis['contact_info']['emails']) if analysis['contact_info']['emails'] else 'Not found'}
  Phones: {', '.join(analysis['contact_info']['phones']) if analysis['contact_info']['phones'] else 'Not found'}
  LinkedIn: {analysis['contact_info']['linkedin'] if analysis['contact_info']['linkedin'] else 'Not found'}
  GitHub: {analysis['contact_info']['github'] if analysis['contact_info']['github'] else 'Not found'}

TECHNICAL SKILLS:
{'-'*80}
  Programming Languages: {', '.join(analysis['skills']['programming']) if analysis['skills']['programming'] else 'None detected'}
  Frameworks: {', '.join(analysis['skills']['frameworks']) if analysis['skills']['frameworks'] else 'None detected'}
  Databases: {', '.join(analysis['skills']['databases']) if analysis['skills']['databases'] else 'None detected'}
  Tools & Platforms: {', '.join(analysis['skills']['tools']) if analysis['skills']['tools'] else 'None detected'}
  Soft Skills: {', '.join(analysis['skills']['soft_skills']) if analysis['skills']['soft_skills'] else 'None detected'}

EDUCATION:
{'-'*80}
  {chr(10).join('  • ' + edu for edu in analysis['education']) if analysis['education'] else '  Not found'}

EXPERIENCE:
{'-'*80}
  Years of Experience: {analysis['years_of_experience']}
  Action Verbs Found: {sum(analysis['action_verbs'].values())}
  Top Action Verbs: {', '.join([f"{k}({v})" for k, v in sorted(analysis['action_verbs'].items(), key=lambda x: x[1], reverse=True)[:5]])}

CONTENT ANALYSIS:
{'-'*80}
  Total Words: {analysis['word_count']}
  Total Skills Identified: {sum(len(v) for v in analysis['skills'].values())}

RECOMMENDATIONS:
{'-'*80}
"""
        
        # Generate recommendations
        recommendations = []
        
        if not analysis['contact_info']['emails']:
            recommendations.append("  • Add your email address")
        if not analysis['contact_info']['phones']:
            recommendations.append("  • Include your phone number")
        if not analysis['contact_info']['linkedin']:
            recommendations.append("  • Add your LinkedIn profile")
        if not analysis['education']:
            recommendations.append("  • Add educational background")
        if analysis['years_of_experience'] < 2:
            recommendations.append("  • Highlight any relevant experience")
        if sum(analysis['action_verbs'].values()) < 5:
            recommendations.append("  • Use more action verbs (developed, implemented, led, etc.)")
        if analysis['word_count'] < 300:
            recommendations.append("  • Expand resume to include more details (aim for 300+ words)")
        if analysis['resume_score'] < 50:
            recommendations.append("  • Consider restructuring to highlight key skills and achievements")
        
        if recommendations:
            report += '\n'.join(recommendations)
        else:
            report += "  ✓ Your resume looks great! Keep it polished and updated."
        
        report += f"\n\n{'='*80}\n"
        
        return report


def main():
    """Main function"""
    print("="*80)
    print("AI RESUME ANALYZER".center(80))
    print("Intelligent Talent Screening Tool".center(80))
    print("="*80)
    
    analyzer = ResumeAnalyzer()
    
    # Get file path from user
    resume_path = input("\nEnter the path to your resume (.txt file): ").strip()
    
    try:
        # Analyze resume
        print("\n📊 Analyzing resume...\n")
        analysis = analyzer.analyze_resume(resume_path)
        
        # Generate and display report
        report = analyzer.generate_report(analysis)
        print(report)
        
        # Save report
        output_path = resume_path.replace('.txt', '_analysis_report.txt')
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"✓ Report saved to: {output_path}\n")
        
        # Save JSON analysis
        json_path = resume_path.replace('.txt', '_analysis.json')
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(analysis, f, indent=2)
        print(f"✓ JSON data saved to: {json_path}\n")
        
    except FileNotFoundError as e:
        print(f"\n❌ Error: {e}\n")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}\n")


if __name__ == "__main__":
    main()