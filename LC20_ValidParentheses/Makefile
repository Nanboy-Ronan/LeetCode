TGT = ValidParentheses
SRCS = ValidParentheses.c Stack.c
OBJ = ValidParentheses.o Stack.o
CC = gcc


$(TGT): $(OBJ)
	$(CC) $(^) -o $@

#test.o: test.c
#	$(CC) $^ -c -o $@
#tst.o: tst.c
#	$(CC) $^ -c -o $@
#%.o: %.c
#	$(CC) $< -c

clean:
	rm -f $(TGT) $(OBJ)