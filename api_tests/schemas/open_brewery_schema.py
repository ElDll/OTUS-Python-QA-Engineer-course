def open_brewery_schema(schema_type='object'):
    if schema_type == 'object':
        open_brewery_schema = {
            "$ref": "#/definitions/Welcome7",
            "definitions": {
                "Welcome7": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "id": {
                            "type": "string"
                        },
                        "name": {
                            "type": "string"
                        },
                        "brewery_type": {
                            "type": "string"
                        },
                        "street": {
                            "type": "string"
                        },
                        "address_2": {
                            "type": ["string", "null"]
                        },
                        "address_3": {
                            "type": ["string", "null"]
                        },
                        "city": {
                            "type": "string"
                        },
                        "state": {
                            "type": "string"
                        },
                        "county_province": {
                            "type": ["string", "null"]
                        },
                        "postal_code": {
                            "type": "string"
                        },
                        "country": {
                            "type": "string"
                        },
                        "longitude": {
                            "type": ["string", "null"]
                        },
                        "latitude": {
                            "type": ["string", "null"]
                        },
                        "phone": {
                            "type": "string"
                        },
                        "website_url": {
                            "type": "string",
                            "format": "uri",
                            "qt-uri-protocols": [
                                "http"
                            ]
                        },
                        "updated_at": {
                            "type": "string",
                            "format": "date-time"
                        },
                        "created_at": {
                            "type": "string",
                            "format": "date-time"
                        }
                    },
                    "required": [
                        "address_2",
                        "address_3",
                        "brewery_type",
                        "city",
                        "country",
                        "county_province",
                        "created_at",
                        "id",
                        "latitude",
                        "longitude",
                        "name",
                        "phone",
                        "postal_code",
                        "state",
                        "street",
                        "updated_at",
                        "website_url"
                    ],
                    "title": "Welcome7"
                }
            }
        }
    if schema_type == 'array':
        open_brewery_schema = {
            "type": "array",
            "items": {
                "$ref": "#/definitions/Welcome1Element"
            },
            "definitions": {
                "Welcome1Element": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "id": {
                            "type": "string"
                        },
                        "name": {
                            "type": "string"
                        },
                        "brewery_type": {
                            "type": "string"
                        },
                        "street": {
                            "type": ["string", "null"]
                        },
                        "address_2": {
                            "type": ["string", "null"]
                        },
                        "address_3": {
                            "type": ["string", "null"]
                        },
                        "city": {
                            "type": "string"
                        },
                        "state": {
                            "type": "string"
                        },
                        "county_province": {
                            "type": ["string", "null"]
                        },
                        "postal_code": {
                            "type": "string"
                        },
                        "country": {
                            "type": "string"
                        },
                        "longitude": {
                            "type": ["string", "null"]
                        },
                        "latitude": {
                            "type": ["string", "null"]
                        },
                        "phone": {
                            "type": ["string", "null"]
                        },
                        "website_url": {
                            "type": ["string", "null"],
                            "format": "uri",
                            "qt-uri-protocols": [
                                "http"
                            ]
                        },
                        "updated_at": {
                            "type": "string",
                            "format": "date-time"
                        },
                        "created_at": {
                            "type": "string",
                            "format": "date-time"
                        }
                    },
                    "required": [
                        "address_2",
                        "address_3",
                        "brewery_type",
                        "city",
                        "country",
                        "county_province",
                        "created_at",
                        "id",
                        "latitude",
                        "longitude",
                        "name",
                        "phone",
                        "postal_code",
                        "state",
                        "street",
                        "updated_at",
                        "website_url"
                    ],
                    "title": "Welcome1Element"
                }
            }
        }
    if schema_type == 'empty':
        open_brewery_schema = {
            "type": "array",
            "items": {},
            "definitions": {}
        }
    return open_brewery_schema
