import os

from structer.create_layer import (
    create_layer
)
from structer.create_package import (
    create_package
)
from structer.make_file import (
    make_file
)

def make_struct(
    struct: dict,
    fields: dict,
    base_dir: str,
) -> None:
    layer_filenames = {
        'models': 'model',
        'repositories': 'repository',
        'services': 'service',
        'resources': 'resource',
    }

    for layer, template in struct.items():
        package_path: str = create_package(
            base_dir=base_dir,
            leaves=layer,
        )
        tail_name = layer_filenames.get(layer, {}).title()
        tail_name = tail_name if tail_name.lower() != 'model' else ''
        for entity in fields.get('entities', {}):
            make_file(
                path_name=os.path.join(package_path, f'{entity.get("class_name")}{tail_name}.java'),
                file_content=create_layer(
                    entity={
                        **entity,
                        'package_name': fields.get('package_name', {}),
                    },
                    template=template,
                ),
            )