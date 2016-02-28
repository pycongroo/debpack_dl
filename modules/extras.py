"""modulo de funciones auxiliares en funcion principal."""
from glob import glob


def get_links(source_path):
    """Obtiene lista de enlaces guardados en el archivo."""
    arch = open(source_path)
    lineas = arch.readlines()
    links = map(lambda x: x.replace('\n', ''), lineas)
    print links
    return links


def get_directory(source_path):
    """Obtiene el directorio del archivo."""
    return source_path[:source_path.rfind('/')]


def get_dw_name(link):
    """Obtiene nombre de fichero."""
    return link.rsplit('/')[-1]


def get_package_dirs(path):
    dirs = glob("%s/*/" % path)
    print dirs
    return dirs


def incompleto(path_dir):
    total = len(open("%s/links.txt" % path_dir).readlines())
    c_debs = len(glob("%s/*deb" % path_dir))
    return c_debs < total
