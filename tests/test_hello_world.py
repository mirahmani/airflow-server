import unittest
import DagBag
#from airflow.models import DagBag

class TestMySimpleDag(unittest.TestCase):
    """Test for my_simple_dag"""

    def setUp(self):
        self.dagbag = DagBag()

    def test_dag_loaded(self):
        """Check the DAG is in the DagBag"""
        dag = self.dagbag.get_dag(dag_id='hello_world')
        self.assertTrue(dag is not None, "DAG not found in DagBag")

    def test_task_count(self):
        """Check the number of tasks in the DAG"""
        dag = self.dagbag.get_dag(dag_id='hello_world')
        self.assertEqual(len(dag.tasks), 3, "Wrong number of tasks in the DAG")

    def test_contain_task(self):
        """Check that a specific task is in the DAG"""
        dag = self.dagbag.get_dag(dag_id='hello_world')
        task_ids = list(map(lambda task: task.task_id, dag.tasks))
        self.assertIn('start_task', task_ids, "Task not found in the DAG")
        self.assertIn('hello_task', task_ids, "Task not found in the DAG")
        self.assertIn('world_task', task_ids, "Task not found in the DAG")

    def test_dependencies_of_my_simple_task(self):
        """Check the dependencies of my_simple_task"""
        dag = self.dagbag.get_dag(dag_id='hello_world')
        hello_task = dag.get_task('hello_task')

        upstream_task_ids = list(map(lambda task: task.task_id, hello_task.upstream_list))
        self.assertEqual(len(upstream_task_ids), 1, "hello_task has upstream dependencies")

        downstream_task_ids = list(map(lambda task: task.task_id, hello_task.downstream_list))
        self.assertEqual(len(downstream_task_ids), 1, "hello_task has downstream dependencies")

if __name__ == '__main__':
    unittest.main()
