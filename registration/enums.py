from enum import Enum


class ModelChoicesEnum(Enum):
    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class GenderEnum(ModelChoicesEnum):
    MALE = 'Male'
    FEMALE = 'Female'


class MaritalStatusEnum(ModelChoicesEnum):
    SINGLE = 'Single'
    MARRIED = 'Married'


class ResidentStatusEnum(ModelChoicesEnum):
    RESIDENT = 'Resident'
    VISITOR = 'Visitor'
