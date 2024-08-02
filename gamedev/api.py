from ninja import NinjaAPI
from testapp.api import testapp_router

api = NinjaAPI()

api.add_router("testapp",testapp_router)