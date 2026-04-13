
# schemas/list_tasks_schema.py

list_tasks_schema = {
    "type": "object",
    "required": ["tasks"],
    "properties": {
        "tasks": {
            "type": "array",
            "minItems": 0,
            "items": {
                "type": "object",
                "required": [
                    "task_id",
                    "user_id",
                    "content",
                    "is_done",
                    "created_time",
                    "ttl"
                ],
                "properties": {
                    "task_id": {"type": "string"},
                    "user_id": {"type": "string"},
                    "content": {"type": "string"},
                    "is_done": {"type": "boolean"},
                    "created_time": {"type": "integer"},
                    "ttl": {"type": "integer"}
                },
                "additionalProperties": False
            }
        }
    },
    "additionalProperties": False
}