import argparse

def parsers():
    parser = argparse.ArgumentParser(
        usage='python generator --base "c:/Users/Mateus/Desktop/test" --entities Arroz Feijao ArrozComFeijao --package uea.cozinha'
    )
    parser.add_argument(
        '--base',
        type=str,
        default=None,
        help='Relativa path to main java package.',
        required=True,
    )
    parser.add_argument(
        '--entities',
        nargs='+',
        type=str,
        default=None,
        help='List of entities.',
        required=True,
    )
    parser.add_argument(
        '--package',
        type=str,
        default=None,
        help='Package name.',
        required=True,
    )

    return parser.parse_args()