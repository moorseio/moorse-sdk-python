from dto.template.component.template_component import TemplateComponent
from dto.template.component.template_component_example import TemplateComponentExample
from enums.template.component.template_component_format import TemplateComponentFormat
from enums.template.component.template_component_type import TemplateComponentType

class TemplateImageComponent(TemplateComponent):

    def __init__(
        self,
        type: TemplateComponentType,
        example: TemplateComponentExample = None
    ):
        super().__init__(
            type = type,
            text = None,
            format = TemplateComponentFormat.IMAGE,
            example = example,
            buttons = None
        )