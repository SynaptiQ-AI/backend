def validate_data(data: dict) -> bool:
return isinstance(data, dict) and len(data) > 0