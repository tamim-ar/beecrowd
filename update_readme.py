import os
import re

# ===== CONFIG =====
TOTAL_PROBLEMS = 2411   # Total problems on beecrowd
SOLUTIONS_FOLDER = "solutions"

BADGE_STYLE = "flat-square"
LOGO_COLOR = {
    "beecrowd": "323232",
    "Python": "60A4FB",
    "Java": "4298E2",
    "JavaScript": "F7DF1E",
    "C": "555555",
    "C++": "00599C",
}

LANGUAGE_EXTENSIONS = {
    "Python": [".py"],
    "Java": [".java"],
    "JavaScript": [".js"],
    "C": [".c", ".h"],
    "C++": [".cpp", ".hpp", ".cc", ".cxx"],
}
# ==================

def count_solutions():
    if not os.path.exists(SOLUTIONS_FOLDER):
        return 0
    with os.scandir(SOLUTIONS_FOLDER) as entries:
        return sum(1 for entry in entries if entry.is_dir())

def count_solutions_by_language():
    counts = {lang: 0 for lang in LANGUAGE_EXTENSIONS}
    for root, _, files in os.walk(SOLUTIONS_FOLDER):
        for file in files:
            for lang, exts in LANGUAGE_EXTENSIONS.items():
                if any(file.endswith(ext) for ext in exts):
                    counts[lang] += 1
    return counts

def generate_badges(solved, total, counts):
    percentage = round((solved / total) * 100, 2) if total > 0 else 0
    return {
        "progress": f"https://img.shields.io/badge/Solved-{solved}%2F{total}%20({percentage}%25)-{LOGO_COLOR['beecrowd']}?style={BADGE_STYLE}",
        "Python": f"https://img.shields.io/badge/Python%203-{counts['Python']}%20solutions-{LOGO_COLOR['Python']}?style={BADGE_STYLE}&logo=python",
        "Java": f"https://img.shields.io/badge/Java-{counts['Java']}%20solutions-{LOGO_COLOR['Java']}?style={BADGE_STYLE}&logo=java",
        "JavaScript": f"https://img.shields.io/badge/JavaScript-{counts['JavaScript']}%20solutions-{LOGO_COLOR['JavaScript']}?style={BADGE_STYLE}&logo=javascript",
        "C": f"https://img.shields.io/badge/C-{counts['C']}%20solutions-{LOGO_COLOR['C']}?style={BADGE_STYLE}&logo=c",
        "C++": f"https://img.shields.io/badge/C%2B%2B-{counts['C++']}%20solutions-{LOGO_COLOR['C++']}?style={BADGE_STYLE}&logo=cplusplus",
    }

def update_readme(badges):
    readme_template = '''<div align="center">
  <h1>🐝 beecrowd Solutions</h1>
  
  Solutions to [beecrowd](https://www.beecrowd.com.br/judge/en) problems
  
  ---
  
  ![Beecrowd Progress]({progress})
  <br/>
  ![Python]({Python})
  ![Java]({Java})
  ![JavaScript]({JavaScript})
  <br/>
  ![C]({C})
  ![C++]({C++})
  
  ---
</div>

## ✨ Features
- ✅ Clean & optimized solutions
- ✅ Python, Java, JavaScript, C & C++ solutions
- ✅ Perfect for learning algorithms

## 👨‍💻 Author
**Tamim Ahasan Rijon**  
📧 [tamimahasan.ar@gmail.com](mailto:tamimahasan.ar@gmail.com)  
🌐 [Portfolio](https://tamim-ar.netlify.app/)

## 📜 License
Licensed under the [MIT License](./LICENSE).
'''
    content = readme_template.format(**badges)
    
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    solved = count_solutions()
    counts = count_solutions_by_language()
    badges = generate_badges(solved, TOTAL_PROBLEMS, counts)
    update_readme(badges)

    print("\n🚀 README Badges Updated Successfully!\n")
    print(f"📊 Solved: {solved}/{TOTAL_PROBLEMS} ({round((solved / TOTAL_PROBLEMS) * 100, 2)}%)\n")
    print("📌 Solutions by Language:")
    for lang, count in counts.items():
        print(f"   • {lang:<10}: {count} solutions")
    print("\n✅ Done!\n")
