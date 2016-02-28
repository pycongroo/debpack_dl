"""Funciones para descargas debs."""
import sys
sys.path.append("externals/pynet")
sys.path.append("modules")

import pynet as net
import extras


class DownloadWorker():
    """Objeto manejador de descargas."""

    def __init__(self):
        self.dw_objects = []

    def add(self, path_source):
        dwo = DownloadObject(path_source)
        self.dw_objects.append(dwo)

    def download_all(self):
        total = len(self.dw_objects)
        for i in range(total):
            print("Descargando objeto %s de %s" % (i + 1, total))
            self.dw_objects[i].download()


class DownloadObject():
    """Objeto de descarga."""

    def __init__(self, path_source):
        # self.urls = []
        self.dir_source = extras.get_directory(path_source)
        self.urls = extras.get_links(path_source)
        print "archivo %s cargado con destino %s" % (
            path_source, self.dir_source)

    def download(self):
        total = len(self.urls)
        for i in range(total):
            print("Descargando archivo %s de %s" % (i + 1, total))
            path_dest = extras.get_dw_name(self.urls[i])
            net.download_file(
                self.urls[i],
                '%s/%s' % (self.dir_source, path_dest))


def download_debs(path='debs'):
    dww = DownloadWorker()
    pack_dirs = extras.get_package_dirs(path)
    pack_pends = filter(
        lambda pack: extras.incompleto(pack[:-1]),
        pack_dirs)
    for pack in pack_pends:
        dww.add('%s/links.txt' % pack[:-1])
    dww.download_all()


# download_debs()
