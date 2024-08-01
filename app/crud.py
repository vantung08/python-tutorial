from app.models import Users
from app.pydantic_schema import UserSchema

async def create_user(schema_user: UserSchema):
    model_user = Users(**schema_user.model_dump())
    new_user = await Users.insert_one(model_user)
    created_user = await Users.get(new_user.id)
    return created_user

# async def read_single_user(schema_user: UserSchema, collection: AsyncIOMotorCollection):
#     model_user = UsersModel(**schema_user.model_dump())
#     new_user = await collection.insert_one(model_user.model_dump())
#     created_user = await collection.find_one({"_id": new_user.inserted_id})
#     return created_user