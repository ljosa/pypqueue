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


class GetJobsTest(unittest.TestCase):
    def test_get_jobs(self):
        d = tempfile.mkdtemp(prefix="pypqueue_test_submit")
        try:
            make_queue(d)
            pypqueue.submit(d, 'myjob', spec='myspec_1')
            pypqueue.submit(d, 'myjob', spec='myspec_2')
            pypqueue.submit(d, 'notmyjob', spec='notmyspec')
            jobs = pypqueue.get_jobs(d, 'myjob', 'new')
            self.assertEqual(len(jobs), 2)
            self.assertEqual(set([jobs[0].get('spec'),
                                  jobs[1].get('spec')]),
                             set(['myspec_1', 'myspec_2']))
        finally:
            shutil.rmtree(d)
        
