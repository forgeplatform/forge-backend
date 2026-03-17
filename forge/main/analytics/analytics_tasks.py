# Python
import logging

# AWX
from forge.main.analytics.subsystem_metrics import DispatcherMetrics, CallbackReceiverMetrics
from forge.main.dispatch.publish import task
from forge.main.dispatch import get_task_queuename

logger = logging.getLogger('forge.main.scheduler')


@task(queue=get_task_queuename)
def send_subsystem_metrics():
    DispatcherMetrics().send_metrics()
    CallbackReceiverMetrics().send_metrics()
