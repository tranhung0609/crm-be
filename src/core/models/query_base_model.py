import inspect

from fastapi import Query
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel, ValidationError


class QueryBaseModel(BaseModel):
    def __init_subclass__(cls, *args, **kwargs):
        field_default = Query(...)
        new_params = []
        for field in cls.__fields__.values():
            default = Query(field.default) if not field.required else field_default
            annotation = inspect.Parameter.empty

            new_params.append(
                inspect.Parameter(
                    field.alias,
                    inspect.Parameter.POSITIONAL_ONLY,
                    default=default,
                    annotation=annotation,
                )
            )

        async def _as_query(**data):
            try:
                return cls(**data)
            except ValidationError as e:
                raise RequestValidationError(e.raw_errors)

        sig = inspect.signature(_as_query)
        sig = sig.replace(parameters=new_params)
        _as_query.__signature__ = sig  # type: ignore
        setattr(cls, "as_query", _as_query)

    @staticmethod
    def as_query(parameters: list) -> "QueryBaseModel":
        raise NotImplementedError