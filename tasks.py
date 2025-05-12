from config import Config

class TaskManager:
    def __init__(self):
        self.tasks = {}

    def assign_task(self, group_id, user_id, task_description):
        if group_id not in Config.ALLOWED_GROUPS:
            print(f"Group {group_id} is not permitted to assign tasks.")
            return
        if group_id not in self.tasks:
            self.tasks[group_id] = {}
        self.tasks[group_id][user_id] = task_description
        print(f"Task assigned to {user_id} in group {group_id}: {task_description}")

    def get_tasks(self, group_id):
        return self.tasks.get(group_id, {})