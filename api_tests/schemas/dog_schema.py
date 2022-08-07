def dog_schema(message_type):
    schema = {
        "type": "object",
        "properties": {
            "message": message_type,
            "status": {"type": "string"},
        },
        "required": ["message", "status"]
    }
    return schema
