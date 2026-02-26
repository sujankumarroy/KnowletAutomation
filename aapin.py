import subprocess
import sys

ROOT_DIR = "/sdcard/.workspace/other/python/file_processing/"

# Define your scripts in the order they should execute
scripts = [
    "replace_cite.py",
    "replace_latex.py",
    "replace_spans.py",
    "update_notes_title.py",
    "link_css_js.py",
    "add_horizontal_scroll.py",
    "generate_notes_json.py",
    "generate_sitemap_xml.py"
]

def run_build():
    for script in scripts:
        print(f"--- Running {script} ---")
        script = ROOT_DIR + script
        try:
            # check=True ensures an exception is raised if the script returns a non-zero exit code
            subprocess.run([sys.executable, script], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error: {script} failed with exit code {e.returncode}")
            # Stop the build if a step fails
            sys.exit(1)
            
    print("\nBuild completed successfully!")

if __name__ == "__main__":
    run_build()
