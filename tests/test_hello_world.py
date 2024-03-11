import unittest
from unittest.mock import patch
from airflow.models import DagBag

class TestExampleDAG(unittest.TestCase):
    @patch("airflow.models.DagBag")
    def test_dag_loaded(self, mock_dag_bag):
        """Check that the DAG file is correctly imported into the DagBag"""
        mock_dag_bag.return_value.dags.keys.return_value = ['hello_world']
        mock_dag_bag.return_value.dags.__getitem__.return_value.tasks = ['task1', 'task2']

        dagbag = DagBag(dag_folder="dags/", include_examples=False)

        self.assertIn('hello_world', dagbag.dags)
        self.assertGreater(len(dagbag.dags['hello_world'].tasks), 0)

    @patch("airflow.models.DagBag")
    def test_task_dependencies(self, mock_dag_bag):
        """Check the task dependencies in the hello_world"""
        dag_id = 'hello_world'
        mock_dag_bag.return_value.get_dag.return_value.task_dict = {
            'start_task': MockTask('start_task', downstream_list=['hello_task']),
            'hello_task': MockTask('hello_task', upstream_list=['start_task'], downstream_list=['world_task']),
            'world_task': MockTask('world_task', upstream_list=['hello_task'])
        }

        dagbag = DagBag(dag_folder="dags/", include_examples=False)
        dag = dagbag.get_dag(dag_id=dag_id)

        start_task = dag.get_task('start_task')
        hello_task = dag.get_task('hello_task')
        world_task = dag.get_task('world_task')

        self.assertEqual(start_task.downstream_task_ids, {'hello_task'})
        self.assertEqual(hello_task.upstream_task_ids, {'start_task'})
        self.assertEqual(hello_task.downstream_task_ids, {'world_task'})
        self.assertEqual(world_task.upstream_task_ids, {'hello_task'})

class MockTask:
    def __init__(self, task_id, upstream_list=None, downstream_list=None):
        self.task_id = task_id
        self.upstream_task_ids = set(upstream_list) if upstream_list else set()
        self.downstream_task_ids = set(downstream_list) if downstream_list else set()

if __name__ == '__main__':
    unittest.main()
