from builders.base import BaseBuilder
from methods.case_management import lower
from methods.character_sorting import reverse


class BackwardsLower(BaseBuilder):

    def transform_data(self):
        return reverse(lower(self.text))
