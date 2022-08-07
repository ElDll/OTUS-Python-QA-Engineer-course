def json_placeholder_schema(schema_type):
    if schema_type == 'posts':
        json_placeholder_schema = {
            "$ref": "#/definitions/Welcome9",
            "definitions": {
                "Welcome9": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "userId": {
                            "type": "integer"
                        },
                        "id": {
                            "type": "integer"
                        },
                        "title": {
                            "type": "string"
                        },
                        "body": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "body",
                        "id",
                        "title",
                        "userId"
                    ],
                    "title": "Welcome9"
                }
            }
        }
    if schema_type == 'comments':
        json_placeholder_schema = {
            "$ref": "#/definitions/Welcome4",
            "definitions": {
                "Welcome4": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "postId": {
                            "type": "integer"
                        },
                        "id": {
                            "type": "integer"
                        },
                        "name": {
                            "type": "string"
                        },
                        "email": {
                            "type": "string"
                        },
                        "body": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "body",
                        "email",
                        "id",
                        "name",
                        "postId"
                    ],
                    "title": "Welcome4"
                }
            }
        }
    if schema_type == 'albums':
        json_placeholder_schema = {
            "$ref": "#/definitions/Welcome2",
            "definitions": {
                "Welcome2": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "userId": {
                            "type": "integer"
                        },
                        "id": {
                            "type": "integer"
                        },
                        "title": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "id",
                        "title",
                        "userId"
                    ],
                    "title": "Welcome2"
                }
            }
        }
    if schema_type == 'photos':
        json_placeholder_schema = {
            "$ref": "#/definitions/Welcome5",
            "definitions": {
                "Welcome5": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "albumId": {
                            "type": "integer"
                        },
                        "id": {
                            "type": "integer"
                        },
                        "title": {
                            "type": "string"
                        },
                        "url": {
                            "type": "string",
                            "format": "uri",
                            "qt-uri-protocols": [
                                "https"
                            ]
                        },
                        "thumbnailUrl": {
                            "type": "string",
                            "format": "uri",
                            "qt-uri-protocols": [
                                "https"
                            ]
                        }
                    },
                    "required": [
                        "albumId",
                        "id",
                        "thumbnailUrl",
                        "title",
                        "url"
                    ],
                    "title": "Welcome5"
                }
            }
        }
    if schema_type == 'users':
        json_placeholder_schema = {
            "$ref": "#/definitions/Welcome5",
            "definitions": {
                "Welcome5": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "id": {
                            "type": "integer"
                        },
                        "name": {
                            "type": "string"
                        },
                        "username": {
                            "type": "string"
                        },
                        "email": {
                            "type": "string"
                        },
                        "address": {
                            "$ref": "#/definitions/Address"
                        },
                        "phone": {
                            "type": "string"
                        },
                        "website": {
                            "type": "string"
                        },
                        "company": {
                            "$ref": "#/definitions/Company"
                        }
                    },
                    "required": [
                        "address",
                        "company",
                        "email",
                        "id",
                        "name",
                        "phone",
                        "username",
                        "website"
                    ],
                    "title": "Welcome5"
                },
                "Address": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "street": {
                            "type": "string"
                        },
                        "suite": {
                            "type": "string"
                        },
                        "city": {
                            "type": "string"
                        },
                        "zipcode": {
                            "type": "string"
                        },
                        "geo": {
                            "$ref": "#/definitions/Geo"
                        }
                    },
                    "required": [
                        "city",
                        "geo",
                        "street",
                        "suite",
                        "zipcode"
                    ],
                    "title": "Address"
                },
                "Geo": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "lat": {
                            "type": "string"
                        },
                        "lng": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "lat",
                        "lng"
                    ],
                    "title": "Geo"
                },
                "Company": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "name": {
                            "type": "string"
                        },
                        "catchPhrase": {
                            "type": "string"
                        },
                        "bs": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "bs",
                        "catchPhrase",
                        "name"
                    ],
                    "title": "Company"
                }
            }
        }
    if schema_type == 'empty':
        json_placeholder_schema = {
            "$ref": "#/definitions/Welcome8",
            "definitions": {
                "Welcome8": {
                    "type": "object",
                    "additionalProperties": False,
                    "title": "Welcome8"
                }
            }
        }
    return json_placeholder_schema