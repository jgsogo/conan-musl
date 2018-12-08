from conans import ConanFile, tools, AutoToolsBuildEnvironment


class MuslConan(ConanFile):
    name = "musl"
    version = "1.1.20"

    settings = "os", "arch", "compiler", "build_type"
    options = {'shared': [True, False]}
    default_options = {'shared': False}

    def configure(self):
        print("*"*20)
        print(self.settings.os)
        print(self.settings.os_build)

    def source(self):
        url = "https://www.musl-libc.org/releases/musl-{version}.tar.gz".format(version=self.version)
        tools.get(url)

    def build(self):
        with tools.chdir("musl-{v}".format(v=self.version)):
            args = ['--disable-static' if self.options.shared else '--disable-shared']
            autotools = AutoToolsBuildEnvironment(self)
            autotools.configure(args=args)
            autotools.make()

