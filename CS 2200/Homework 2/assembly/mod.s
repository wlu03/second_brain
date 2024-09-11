!============================================================
! CS 2200 Homework 2 Part 1: mod
!
! Edit any part of this file necessary to implement the
! mod operation. Store your result in $v0.
!============================================================

mod:
    addi    $a0, $zero, 28      ! $a0 = 28, the number a to compute mod(a,b)
    addi    $a1, $zero, 13      ! $a1 = 13, the number b to compute mod(a,b)

	addi	$t0, $a0, 0 		! use t0 as x <- a
	nand    $t1, $a1, $a1       ! storing -b
	addi    $t1, $t1, 1         ! storing -b
	
while:
	blt $t0, $a1, end           ! while x <= b, blt only jumps if x>b 
		
	add $t0, $t0, $t1           ! x = x + (-b)
		
	beq $zero, $zero, while     ! while loop (always jump because true)
	
end: 
	add $v0, $v0, $t0          ! store the value of x in $v0
	halt