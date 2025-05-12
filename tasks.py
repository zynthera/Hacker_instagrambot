from config import Config
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class TaskManager:
    def __init__(self):
        self.tasks = {}

    def assign_task(self, group_id, user_id, task_description):
        if group_id not in Config.ALLOWED_GROUPS:
            logger.warning("Group %s is not permitted to assign tasks.", group_id)
            return
        if group_id not in self.tasks:
            self.tasks[group_id] = {}
        self.tasks[group_id][user_id] = task_description
        logger.info("Task assigned to %s in group %s: %s", user_id, group_id, task_description)

    def get_tasks(self, group_id):
        return self.tasks.get(group_id, {})