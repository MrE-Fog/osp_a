#	$OpenBSD: Makefile,v 1.68 2014/01/25 04:35:32 dtucker Exp $

REGRESS_TARGETS=	t1 t2 t3 t4 t5 t6 t7 t8 t9 t10 t-exec
tests:		$(REGRESS_TARGETS)

# Interop tests are not run by default
interop interop-tests: t-exec-interop

clean:
	for F in $(CLEANFILES); do rm -f $(OBJ)$$F; done
	test -z "${SUDO}" || ${SUDO} rm -f ${SUDO_CLEAN}
	rm -rf $(OBJ).putty

distclean:	clean

LTESTS=	connect \
		proxy-connect \
		connect-privsep \
		proto-version \
		proto-mismatch \
		exit-status \
		envpass \
		transfer \
		banner \
		rekey \
		stderr-data \
		stderr-after-eof \
		broken-pipe \
		try-ciphers \
		yes-head \
		login-timeout \
		agent \
		agent-getpeereid \
		agent-timeout \
		agent-ptrace \
		keyscan \
		keygen-change \
		keygen-convert \
		key-options \
		scp \
		sftp \
		sftp-chroot \
		sftp-cmds \
		sftp-badcmds \
		sftp-batch \
		sftp-glob \
		sftp-perm \
		reconfigure \
		dynamic-forward \
		forwarding \
		multiplex \
		reexec \
		brokenkeys \
		cfgmatch \
		addrmatch \
		localcommand \
		forcecommand \
		portnum \
		keytype \
		kextype \
		cert-hostkey \
		cert-userkey \
		host-expand \
		keys-command \
		forward-control \
		integrity \
		krl
#		dhgex \

INTEROP_TESTS=	putty-transfer putty-ciphers putty-kex conch-ciphers
#INTEROP_TESTS+=ssh-com ssh-com-client ssh-com-keygen ssh-com-sftp

#LTESTS= 	cipher-speed

USER!=		id -un
CLEANFILES=	t2.out t3.out t6.out1 t6.out2 t7.out t7.out.pub copy.1 copy.2 \
		t8.out t8.out.pub t9.out t9.out.pub t10.out t10.out.pub \
		authorized_keys_${USER} known_hosts pidfile testdata \
		ssh_config sshd_config.orig ssh_proxy sshd_config sshd_proxy \
		rsa.pub rsa host.rsa rsa-agent rsa-agent.pub \
		ls.copy banner.in banner.out empty.in \
		scp-ssh-wrapper.scp ssh_proxy_envpass remote_pid \
		sshd_proxy_bak rsa_ssh2_cr.prv rsa_ssh2_crnl.prv \
		known_hosts-cert host_ca_key* cert_host_key* cert_user_key* \
		putty.rsa2 sshd_proxy_orig ssh_proxy_bak \
		key.rsa-* key.dsa-* key.ecdsa-* \
		authorized_principals_${USER} expect actual ready \
		sshd_proxy.* authorized_keys_${USER}.* modpipe revoked-* krl-* \
		ssh.log failed-ssh.log sshd.log failed-sshd.log \
		regress.log failed-regress.log ssh-log-wrapper.sh \
		sftp-server.sh sftp-server.log sftp.log setuid-allowed \
		data ed25519-agent ed25519-agent.pub key.ed25519-512 \
		key.ed25519-512.pub

SUDO_CLEAN+=	/var/run/testdata_${USER} /var/run/keycommand_${USER}

# Enable all malloc(3) randomisations and checks
TEST_ENV=      "MALLOC_OPTIONS=AFGJPRX"

TEST_SSH_SSHKEYGEN?=ssh-keygen

CPPFLAGS=-I..

t1:
	${TEST_SSH_SSHKEYGEN} -if ${.CURDIR}/rsa_ssh2.prv | diff - ${.CURDIR}/rsa_openssh.prv
	tr '\n' '\r' <${.CURDIR}/rsa_ssh2.prv > ${.OBJDIR}/rsa_ssh2_cr.prv
	${TEST_SSH_SSHKEYGEN} -if ${.OBJDIR}/rsa_ssh2_cr.prv | diff - ${.CURDIR}/rsa_openssh.prv
	awk '{print $$0 "\r"}' ${.CURDIR}/rsa_ssh2.prv > ${.OBJDIR}/rsa_ssh2_crnl.prv
	${TEST_SSH_SSHKEYGEN} -if ${.OBJDIR}/rsa_ssh2_crnl.prv | diff - ${.CURDIR}/rsa_openssh.prv

t2:
	cat ${.CURDIR}/rsa_openssh.prv > $(OBJ)/t2.out
	chmod 600 $(OBJ)/t2.out
	${TEST_SSH_SSHKEYGEN} -yf $(OBJ)/t2.out | diff - ${.CURDIR}/rsa_openssh.pub

t3:
	${TEST_SSH_SSHKEYGEN} -ef ${.CURDIR}/rsa_openssh.pub >$(OBJ)/t3.out
	${TEST_SSH_SSHKEYGEN} -if $(OBJ)/t3.out | diff - ${.CURDIR}/rsa_openssh.pub

t4:
	${TEST_SSH_SSHKEYGEN} -lf ${.CURDIR}/rsa_openssh.pub |\
		awk '{print $$2}' | diff - ${.CURDIR}/t4.ok

t5:
	${TEST_SSH_SSHKEYGEN} -Bf ${.CURDIR}/rsa_openssh.pub |\
		awk '{print $$2}' | diff - ${.CURDIR}/t5.ok

t6:
	${TEST_SSH_SSHKEYGEN} -if ${.CURDIR}/dsa_ssh2.prv > $(OBJ)/t6.out1
	${TEST_SSH_SSHKEYGEN} -if ${.CURDIR}/dsa_ssh2.pub > $(OBJ)/t6.out2
	chmod 600 $(OBJ)/t6.out1
	${TEST_SSH_SSHKEYGEN} -yf $(OBJ)/t6.out1 | diff - $(OBJ)/t6.out2

$(OBJ)/t7.out:
	${TEST_SSH_SSHKEYGEN} -q -t rsa -N '' -f $@

t7: $(OBJ)/t7.out
	${TEST_SSH_SSHKEYGEN} -lf $(OBJ)/t7.out > /dev/null
	${TEST_SSH_SSHKEYGEN} -Bf $(OBJ)/t7.out > /dev/null

$(OBJ)/t8.out:
	${TEST_SSH_SSHKEYGEN} -q -t dsa -N '' -f $@

t8: $(OBJ)/t8.out
	${TEST_SSH_SSHKEYGEN} -lf $(OBJ)/t8.out > /dev/null
	${TEST_SSH_SSHKEYGEN} -Bf $(OBJ)/t8.out > /dev/null

$(OBJ)/t9.out:
	test "${TEST_SSH_ECC}" != yes || \
	${TEST_SSH_SSHKEYGEN} -q -t ecdsa -N '' -f $@

t9: $(OBJ)/t9.out
	test "${TEST_SSH_ECC}" != yes || \
	${TEST_SSH_SSHKEYGEN} -lf $(OBJ)/t9.out > /dev/null
	test "${TEST_SSH_ECC}" != yes || \
	${TEST_SSH_SSHKEYGEN} -Bf $(OBJ)/t9.out > /dev/null


$(OBJ)/t10.out:
	${TEST_SSH_SSHKEYGEN} -q -t ed25519 -N '' -f $@

t10: $(OBJ)/t10.out
	${TEST_SSH_SSHKEYGEN} -lf $(OBJ)/t10.out > /dev/null
	${TEST_SSH_SSHKEYGEN} -Bf $(OBJ)/t10.out > /dev/null

t-exec:	${LTESTS:=.sh}
	@if [ "x$?" = "x" ]; then exit 0; fi; \
	for TEST in ""$?; do \
		echo "run test $${TEST}" ... 1>&2; \
		(env SUDO="${SUDO}" TEST_ENV=${TEST_ENV} ${TEST_SHELL} ${.CURDIR}/test-exec.sh ${.OBJDIR} ${.CURDIR}/$${TEST}) || exit $$?; \
	done

t-exec-interop:	${INTEROP_TESTS:=.sh}
	@if [ "x$?" = "x" ]; then exit 0; fi; \
	for TEST in ""$?; do \
		echo "run test $${TEST}" ... 1>&2; \
		(env SUDO="${SUDO}" TEST_ENV=${TEST_ENV} ${TEST_SHELL} ${.CURDIR}/test-exec.sh ${.OBJDIR} ${.CURDIR}/$${TEST}) || exit $$?; \
	done

# Not run by default
interop: ${INTEROP_TARGETS}
