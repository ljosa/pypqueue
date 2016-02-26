import os
import os.path
import shutil
import tempfile
import unittest
import pypqueue

def make_queue(d):
    for subdir in ["tmp", "new", "cur", "done", "failed"]:
        os.mkdir(os.path.join(d, subdir))


class SubmitTest(unittest.TestCase):
    def test_submit(self):
        d = tempfile.mkdtemp(prefix="pypqueue_test_submit")
        try:
            make_queue(d)
            pypqueue.submit(d, 'myjob', spec='myspec')
            new_jobs = os.listdir(os.path.join(d, "new"))
            self.assertEqual(len(new_jobs), 1)
            job_name = new_jobs[0]
            with open(os.path.join(d, "new", job_name, "spec")) as f:
                spec = f.read()
            self.assertEqual(spec, "myspec")
        finally:
            shutil.rmtree(d)
