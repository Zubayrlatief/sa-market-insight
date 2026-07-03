"""Export the HTML report to PDF via headless Chrome/Edge print-to-PDF.

Uses whichever browser is installed - no extra Python dependencies, and
the PDF is a faithful render of the HTML including the inline SVG charts.
"""

import subprocess
from pathlib import Path

BROWSERS = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    "/usr/bin/google-chrome",
    "/usr/bin/chromium-browser",
]


def find_browser():
    for path in BROWSERS:
        if Path(path).exists():
            return path
    return None


def html_to_pdf(html_path: Path, pdf_path: Path) -> Path:
    """Print html_path to pdf_path. Raises RuntimeError if no browser found."""
    browser = find_browser()
    if not browser:
        raise RuntimeError("No Chrome/Edge installation found for PDF export")
    cmd = [
        browser,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path.resolve()}",
        html_path.resolve().as_uri(),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
    if not pdf_path.exists():
        raise RuntimeError(f"PDF export failed: {result.stderr[-500:]}")
    return pdf_path
