#!/usr/bin/env python3
"""Extract readable text from PDFs for academic paper review without modifying the source."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


def extract_with_pdftotext(pdf_path: Path) -> tuple[str | None, str | None]:
    pdftotext_path = shutil.which("pdftotext")
    if not pdftotext_path:
        return None, "pdftotext is not installed"
    result = subprocess.run(
        [pdftotext_path, "-layout", "-nopgbrk", str(pdf_path), "-"],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return None, result.stderr.strip() or "pdftotext failed"
    text = result.stdout.strip()
    if not text:
        return None, "pdftotext produced empty output"
    return text, None


def extract_with_pypdf(pdf_path: Path) -> tuple[str | None, str | None]:
    try:
        from pypdf import PdfReader
    except Exception as exc:  # pragma: no cover - environment dependent
        return None, f"pypdf is unavailable: {exc}"
    try:
        reader = PdfReader(str(pdf_path))
    except Exception as exc:
        return None, f"unable to open PDF with pypdf: {exc}"
    pages: list[str] = []
    for page_number, page in enumerate(reader.pages, start=1):
        try:
            page_text = page.extract_text() or ""
        except Exception as exc:
            return None, f"pypdf failed on page {page_number}: {exc}"
        if page_text.strip():
            pages.append(page_text.strip())
    text = "\n\n".join(pages).strip()
    if not text:
        return None, "pypdf produced empty output"
    return text, None


def extract_text(pdf_path: Path, parser: str) -> tuple[str | None, str | None, str | None]:
    attempts = []
    if parser in {"auto", "pdftotext"}:
        attempts.append(("pdftotext", extract_with_pdftotext))
    if parser in {"auto", "pypdf"}:
        attempts.append(("pypdf", extract_with_pypdf))
    errors: list[str] = []
    for parser_name, extractor in attempts:
        text, error = extractor(pdf_path)
        if text is not None:
            return text, parser_name, None
        if error:
            errors.append(f"{parser_name}: {error}")
    return None, None, "; ".join(errors) or "no PDF parser attempted"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--parser", choices=["auto", "pdftotext", "pypdf"], default="auto")
    parser.add_argument("--max-chars", type=int, default=0, help="Trim output to this many characters; 0 means no trim.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    pdf_path = args.pdf.expanduser()
    if not pdf_path.exists() or not pdf_path.is_file():
        sys.stderr.write(f"missing file: {pdf_path}\n")
        return 2
    text, parser_name, error = extract_text(pdf_path, args.parser)
    if text is None:
        sys.stderr.write(f"failed to extract {pdf_path}: {error}\n")
        sys.stderr.write("If the PDF is image-only or extraction failed, provide OCR text or extracted text.\n")
        return 1
    if args.max_chars > 0:
        text = text[: args.max_chars]
    sys.stderr.write(f"parsed {pdf_path} with {parser_name}\n")
    sys.stdout.write(text)
    if text and not text.endswith("\n"):
        sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
