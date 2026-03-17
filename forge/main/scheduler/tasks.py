# Python
import logging

# Django
from django.conf import settings

# AWX
from forge import MODE
from forge.main.scheduler import TaskManager, DependencyManager, WorkflowManager
from forge.main.dispatch.publish import task
from forge.main.dispatch import get_task_queuename

logger = logging.getLogger('forge.main.scheduler')


def run_manager(manager, prefix):
    if MODE == 'development' and settings.AWX_DISABLE_TASK_MANAGERS:
        logger.debug(f"Not running {prefix} manager, AWX_DISABLE_TASK_MANAGERS is True. Trigger with GET to /api/debug/{prefix}_manager/")
        return
    manager().schedule()


@task(queue=get_task_queuename)
def task_manager():
    run_manager(TaskManager, "task")


@task(queue=get_task_queuename)
def dependency_manager():
    run_manager(DependencyManager, "dependency")


@task(queue=get_task_queuename)
def workflow_manager():
    run_manager(WorkflowManager, "workflow")
