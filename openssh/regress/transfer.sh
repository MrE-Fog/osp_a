#	$OpenBSD: transfer.sh,v 1.2 2013/05/17 04:29:14 dtucker Exp $
#	Placed in the Public Domain.

tid="transfer data"

for p in 2; do
	verbose "$tid: proto $p"
	rm -f ${COPY}
	${SSH} -n -q -$p -F $OBJ/ssh_proxy somehost cat ${DATA} > ${COPY}
	if [ $? -ne 0 ]; then
		fail "ssh cat $DATA failed"
	fi
	cmp ${DATA} ${COPY}		|| fail "corrupted copy"

	for s in 10 100 1k 32k 64k 128k 256k; do
		trace "proto $p dd-size ${s}"
		rm -f ${COPY}
		dd if=$DATA obs=${s} 2> /dev/null | \
			${SSH} -q -$p -F $OBJ/ssh_proxy somehost "cat > ${COPY}"
		if [ $? -ne 0 ]; then
			fail "ssh cat $DATA failed"
		fi
		cmp $DATA ${COPY}		|| fail "corrupted copy"
	done
done
rm -f ${COPY}
