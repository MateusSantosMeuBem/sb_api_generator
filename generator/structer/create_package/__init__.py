def create_package(
        base_dir: str,
        leaves: str
) -> str:
    import os

    full_directory: str = os.path.join(base_dir, leaves)
    os.makedirs(full_directory, exist_ok=True)
    print(f'Package <{leaves}> created successfully!')

    return full_directory