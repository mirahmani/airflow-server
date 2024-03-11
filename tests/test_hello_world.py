import pytest
from airflow.models import DagBag

@pytest.fixture(scope="session")
def dag_bag():
    return DagBag(dag_folder="dags/", include_examples=False)

def test_dag_loaded(dag_bag):
    """Check that the DAG file is correctly imported into the DagBag"""
    assert 'example_dag' in dag_bag.dags
    assert len(dag_bag.dags['example_dag'].tasks) > 0

def test_task_dependencies(dag_bag):
    """Check the task dependencies in the example_dag"""
    dag = dag_bag.get_dag(dag_id='example_dag')
    start_task = dag.get_task('start_task')
    hello_task = dag.get_task('hello_task')
    world_task = dag.get_task('world_task')

    assert start_task.downstream_task_ids == {'hello_task'}
    assert hello_task.upstream_task_ids == {'start_task'}
    assert hello_task.downstream_task_ids == {'world_task'}
    assert world_task.upstream_task_ids == {'hello_task'}
