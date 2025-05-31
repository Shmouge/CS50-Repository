#organize_repo.py imports
import os
import shutil

#Define file-to-folder mapping
structure = {
    "ProblemSet0": ["indoor.py", "playback.py", "faces.py", "einstein.py", "tip.py"],
    "ProblemSet1": ["deep.py"]
}

#Voice-friendly summaries
readme_notes = {
    "indoor.py": "Converts loud uppercase text into a lowercase indoor voice.",
    "playback.py": "Slows down speech by replacing spaces with '...'.",
    "faces.py": "Translates emoticon faces like :) and :( into emoji.",
    "einstein.py": "Calculates E = mc². Just plug in the mass.",
    "tip.py": "Simple tip calculator based on total and percent.",
    "deep.py": "Answers the Great Question of Life, the Universe, and Everything with style."
}

#Create folders, move files, and write local README.md
for folder, files in structure.items():
    os.makedirs(folder, exist_ok=True)

    with open(os.path.join(folder, "README.md"), "w") as readme:
        readme.write(f"# {folder}\n\n")
        readme.write("### Completed Exercises\n\n")
        for file in files:
            if os.path.exists(file):
                shutil.move(file, os.path.join(folder, file))
                desc = readme_notes.get(file, "No description.")
                readme.write(f"- **{file}** – {desc}\n")

#Top-level README
with open("README.md", "w") as root_readme:
    root_readme.write("# CS50 Python Repository\n\n")
    root_readme.write("Projects submitted for CS50’s Introduction to Programming with Python. Sorted by problem set.\n\n")
    root_readme.write("## Problem Sets\n")
    for folder in structure:
        root_readme.write(f"- [{folder}](./{folder})\n")

print("✅ Repo organized. README files created.")