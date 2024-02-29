from typing import Generic, Optional, TypeVar
from pydantic import BaseModel

T = TypeVar("T")

class ResponceSchemaBase(BaseModel):
    code: str = ""
    message: str = ""

    def custom_responce(self, code: str, message: str):
        self.code = code
        self.message = message
        return self
    
    def success_responce(self):
        self.code = "200"
        self.message = "Success"
        return self
    
    def fail_responce(self):
        self.code = "404"
        self.message = "Fail"
        return self

class DataResponce(ResponceSchemaBase, Generic[T]):
    data: Optional[T] = None

    def custom_responce(self, code: str, message: str, data: T):
        self.code = code
        self.message = message
        self.data: data
        return self
    
    def success_responce(self, data: T):
        self.code = "200"
        self.message = "Success"
        self.data = data
        return self
    
    def fail_response(self):
        self.code = "404"
        self.message = "Fail"
        return self

