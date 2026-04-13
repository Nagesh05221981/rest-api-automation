# schemas/get_task_schema.py
get_task_schema = {
    "type": "object",
    "required": ["user_id", "content", "is_done", "created_time", "task_id", "ttl"],
    "properties": {
        "user_id": {"type": "string"},
        "content": {"type": "string"},
        "is_done": {"type": "boolean"},
        "created_time": {"type": "integer"},
        "task_id": {"type": "string"},
        "ttl": {"type": "integer"}
    }
}