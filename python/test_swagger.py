import yaml
from swagger_spec_validator.validator20 import validate_spec

spec = """
definitions:
  MySchema:
    type: object
    additionalProperties:
    # patternProperties:
    #   "^[0-9]$":
          type: object
          properties:
            name: {type: string}
info: {title: WAF restful, version: 3.6.2.61}
parameters: {}
paths:
  /api/waf/v2/web_apps/{oid}:
    get:
      operationId: waf_restful.api.v2.web_apps.show_web_app
      parameters:
      - {in: path, name: oid, required: true, type: string}
      produces: [application/json]
      responses:
        '200':
          description: Show web app.
          schema: {$ref: '#/definitions/MySchema'}
swagger: '2.0'
tags: []
"""
spec = yaml.safe_load(spec)
validate_spec(spec)

