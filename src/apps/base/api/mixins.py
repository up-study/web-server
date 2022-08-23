class SerializerPerAction:
    def get_serializer_class(self):
        assert self.action_serializers, (
            f"{self.__class__.__name__} needs to define a"
            "`action_serializers`"
        )
        assert self.action_serializers.get("default"), (
            f"{self.__class__.__name__} needs to define a"
            "`default` in `action_serializers` attribute"
        )

        self.serializer_class = self.action_serializers.get(
            self.action, self.action_serializers["default"]
        )

        return super(SerializerPerAction, self).get_serializer_class()
