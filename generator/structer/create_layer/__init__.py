def create_layer(
    template: str,
    entity: dict,
) -> None:
    format_entity = template.format(**entity)
    add_braces = format_entity.replace('<left_brace>', '{').replace('<right_brace>', '}')
    return add_braces