from .value_objects import (
    Content,
    Message,
    SocialNetwork,
    Post,
)
from .interfaces import (
    AbstractContentFactory,
    AbstractMessageFactory,
    AbstractSocialNetworkFactory,
    AbstractPostFactory,
)


class PostFactory(AbstractPostFactory):
    def new_post(self):
        return Post()
