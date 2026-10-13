import argparse
import contextlib
import io
import tempfile
import unittest
from pathlib import Path

import host_recon


class RunTests(unittest.TestCase):
    def make_args(self, output=None):
        return argparse.Namespace(target="lab.example", output=output)

    def test_without_output_prints_report(self):
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            result = host_recon.run(self.make_args())

        self.assertEqual(result, 0)
        self.assertIn("[*] target : lab.example", stdout.getvalue())
        self.assertIn("[*] output : (stdout)", stdout.getvalue())

    def test_output_creates_report_file(self):
        with tempfile.TemporaryDirectory() as directory:
            output_path = Path(directory) / "report.txt"
            stdout = io.StringIO()
            with contextlib.redirect_stdout(stdout):
                result = host_recon.run(self.make_args(str(output_path)))

            self.assertEqual(result, 0)
            report = output_path.read_text(encoding="utf-8")
            self.assertIn("[*] target : lab.example", report)
            self.assertIn(f"[*] output : {output_path}", report)
            self.assertIn(f"[*] results written to {output_path}", stdout.getvalue())

    def test_existing_output_is_not_overwritten(self):
        with tempfile.TemporaryDirectory() as directory:
            output_path = Path(directory) / "report.txt"
            output_path.write_text("keep this\n", encoding="utf-8")
            stderr = io.StringIO()
            with contextlib.redirect_stderr(stderr):
                result = host_recon.run(self.make_args(str(output_path)))

            self.assertEqual(result, 1)
            self.assertEqual(output_path.read_text(encoding="utf-8"), "keep this\n")
            self.assertIn("unable to write output file", stderr.getvalue())

    def test_unavailable_output_directory_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            output_path = Path(directory) / "missing" / "report.txt"
            stderr = io.StringIO()
            with contextlib.redirect_stderr(stderr):
                result = host_recon.run(self.make_args(str(output_path)))

            self.assertEqual(result, 1)
            self.assertFalse(output_path.exists())
            self.assertIn("unable to write output file", stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
