from ninja import Schema, Field

class PlayerSchema(Schema):
    id: int
    player_id: str
    username: str
    email: str
    password: str

class BoostSchema(Schema):
    id: int
    title: str

class CompletedLevelSchema(Schema):
    player_id: str
    level_id: int
