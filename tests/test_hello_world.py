import unittest
from airflow.models import DagBag

class TestExampleDAG(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.dagbag = DagBag(dag_folder="dags/", include_examples=False)

    def test_dag_loaded(self):
        """Check that the DAG file is correctly imported into the DagBag"""
        self.assertIn('example_dag', self.dagbag.dags)
        self.assertGreater(len(self.dagbag.dags['example_dag'].tasks), 0)

    def test_task_dependencies(self):
        """Check the task dependencies in the example_dag"""
        dag = self.dagbag.get_dag(dag_id='example_dag')
        start_task = dag.get_task('start_task')
        hello_task = dag.get_task('hello_task')
        world_task = dag.get_task('world_task')

        self.assertEqual(start_task.downstream_task_ids, {'hello_task'})
        self.assertEqual(hello_task.upstream_task_ids, {'start_task'})
        self.assertEqual(hello_task.downstream_task_ids, {'world_task'})
        self.assertEqual(world_task.upstream_task_ids, {'hello_task'})

if __name__ == '__main__':
    unittest.main()
