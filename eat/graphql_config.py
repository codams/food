from ariadne import QueryType, make_executable_schema, load_schema_from_path, MutationType, snake_case_fallback_resolvers
from ariadne_django.scalars import date_scalar
import food.resolvers

type_defs = [
    load_schema_from_path("food/schema.graphql"),
    load_schema_from_path("eat/schema.graphql"),
]

query = QueryType()
query.set_field("foods", food.resolvers.list_foods)
query.set_field("days", food.resolvers.list_days)
query.set_field('food', food.resolvers.get_food)

mutation = MutationType()
mutation.set_field("createFood", food.resolvers.create_food)
mutation.set_field("createDay", food.resolvers.create_day)
mutation.set_field("updateFoodDate", food.resolvers.update_food_date)

schema = make_executable_schema(type_defs, query, mutation, date_scalar, snake_case_fallback_resolvers)