from __future__ import annotations

import sys
from pathlib import Path
import unittest


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from publication_residue import remediate_publication_projection, scan_publication_residue  # noqa: E402


class PublicationResidueTests(unittest.TestCase):
    def test_removes_direct_decision_section_without_removing_conclusion(self) -> None:
        source = """# Paper

## 4. Author Decisions Before Publication

The author should decide whether to: (1) adopt it; and (2) publish it.

## 5. Conclusion

The argument remains.
"""
        result, _ = remediate_publication_projection(source)
        self.assertNotIn("Author Decisions", result)
        self.assertNotIn("The author should decide", result)
        self.assertIn("## 5. Conclusion", result)
        self.assertIn("The argument remains.", result)

    def test_preserves_research_questions_under_reader_facing_heading(self) -> None:
        source = """## 20. Research and Author Decisions

1. Determine the evidence threshold.
2. Test the counterexample.

## 21. Conclusion
"""
        result, _ = remediate_publication_projection(source)
        self.assertIn("## 20. Research Agenda and Open Questions", result)
        self.assertIn("Determine the evidence threshold", result)
        self.assertFalse(scan_publication_residue(result))

    def test_preserves_counterevidence_and_drops_instruction_tail(self) -> None:
        source = """## 16. Counterevidence, Attack Surface, and Publication Decisions

The claim fails under bypass.

Before publication, the author should decide whether to adopt the repair.

No choice recorded here publishes the paper.

## 17. Limitations

The limit remains.
"""
        result, _ = remediate_publication_projection(source)
        self.assertIn("## 16. Counterevidence and Attack Surface", result)
        self.assertIn("The claim fails under bypass.", result)
        self.assertNotIn("author should decide", result.lower())
        self.assertIn("## 17. Limitations", result)

    def test_normalizes_stale_review_and_prepublication_status(self) -> None:
        source = """This text is an AI-prepared successor revision candidate for author review.

The cited work is an unpublished author-review source.

Before publication, its primary sources should be checked.
"""
        result, _ = remediate_publication_projection(source)
        self.assertIn("AI-assisted integrated successor edition", result)
        self.assertIn("separately custodied reviewed source", result)
        self.assertIn("For a future evidence-qualified revision", result)
        self.assertFalse(scan_publication_residue(result))


if __name__ == "__main__":
    unittest.main()
