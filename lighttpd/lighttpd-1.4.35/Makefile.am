SUBDIRS=src doc tests

EXTRA_DIST=autogen.sh SConstruct wolfStartUp

ACLOCAL_AMFLAGS = -I m4

distcleancheck_listfiles = find -type f -exec sh -c 'test -f $(srcdir)/{} || echo {}' ';'

AM_DISTCHECK_CONFIGURE_FLAGS=--with-openssl
