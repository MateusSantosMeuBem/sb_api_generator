import os
from templates import (
    struct,
)
from personal_parser import (
    parsers
)
from structer import (
    make_struct
)

if __name__ == '__main__':
    
    args = parsers()

    base_dir = args.base

    entities = [
        {
            'class_name': f'{entity[0].upper()}{entity[1:]}',
            'lower_class_name': f'{entity[0].upper()}{entity[1:]}',
        }
        for entity in args.entities
    ]

    fields = {
        'package_name': args.package,
        'entities': entities
    }

    if not os.path.isdir(base_dir):
        exit(f'<{base_dir}> is not a valid directory!')

    make_struct(
        struct=struct,
        base_dir=base_dir,
        fields=fields,
    )
    
    