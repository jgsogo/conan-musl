from conans import ConanFile, tools, AutoToolsBuildEnvironment


class MuslConan(ConanFile):
    name = "musl"
    version = "1.1.20"

    settings = "os", "arch", "compiler", "build_type"
    options = {'shared': [True, False]}
    default_options = {'shared': False}

    def configure(self):
        if self.settings.os != "Linux":
            raise ConanInvalidConfiguration("Required Linux to compile")

    def source(self):
        url = "https://www.musl-libc.org/releases/musl-{version}.tar.gz".format(version=self.version)
        tools.get(url)

    def build(self):
        with tools.chdir("musl-{v}".format(v=self.version)):
            args = ['--disable-static' if self.options.shared else '--disable-shared']
            autotools = AutoToolsBuildEnvironment(self)
            autotools.configure(args=args)
            autotools.make()

    def package(self):
        with tools.chdir("musl-{v}".format(v=self.version)):
            autotools = AutoToolsBuildEnvironment(self)
            autotools.install()

