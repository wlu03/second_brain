!============================================================
! CS 2200 Homework 2 Part 2: Tower of Hanoi
!
! Apart from initializing the stack,
! please do not edit mains functionality. You do not need to
! save the return address before jumping to hanoi in
! main.
!============================================================

main:
	lea		$sp, stack				! loads the address of stack in $sp
	lw      $sp, 0($sp) 			! Loads the value of the number into $sp
	
    lea     $at, hanoi              ! loads address of hanoi label into $at

    lea     $a0, testNumDisks2      ! loads address of number into $a0
    lw      $a0, 0($a0)             ! loads value of number into $a0

    jalr    $at, $ra                ! jump to hanoi, set $ra to return addr
    halt                            ! when we return, just halt

hanoi:
    ! TODO: perform post-call portion of
    ! the calling convention. Make sure to
    ! save any registers you will be using!

	addi	$sp, $sp, -1			! Adding Framepointer
	sw		$fp, 0($sp)				! storing the frame pointer on stack
	add		$fp, $sp, $zero			! fp <- sp's address
	
	! TODO: Implement the following pseudocode in assembly:
	! IF ($a0 == 1)
    !    GOTO base
    ! ELSE
    !    GOTO else
                                    
	addi	$t2, $zero, 1			! t0<-1
	beq		$t2, $a0, base			! go to base if $a0 == 1

else:
   	! TODO: perform recursion after decrementing
   	! the parameter by 1. Remember, $a0 holds the
    ! parameter value.
                                    
	addi	$sp, $sp, -1			! Callee adds the return address
	sw		$ra, 0($sp)				! Callee adds the return address
	
	addi	$a0, $a0, -1			! n-1
	lea		$at, hanoi				! preparing to return to hanoi
	jalr	$at, $ra				! jump to hanoi where ra is saved beforehand
	
	lw		$ra, 0($sp)				! pop after
	addi	$sp, $sp, 1

    ! TODO: Implement the following pseudocode in assembly:
    ! $v0 = 2 * $v0 + 1 
   	! RETURN $v0
                                    
	add		$v0, $v0, $v0			! $v0 = 2 * $v0 + 1 
	addi	$v0, $v0, 1				! $v0 = 2 * $v0 + 1 
	beq		$zero, $zero, teardown	! finished!

base:
    ! TODO: Return 1 
	addi	$v0, $zero, 1			! $v0 <- 1 

teardown:
    ! TODO: perform pre-return portion
    ! of the calling convention
    ! return to caller
    					            
  	addi	$sp, $fp, 0				! restore the stack pointer using the frame pointer
  	lw		$fp, 0($sp)				! restore frame pointer
  	addi	$sp, $sp, 1				! restore frame pointer
  	
  	jalr	$ra, $zero				! return to caller
    
stack: .word 0xFFFF                 ! the stack begins here


! Words for testing \/

! 1
testNumDisks1:
    .word 0x0001

! 10
testNumDisks2:
    .word 0x000a

! 20
testNumDisks3:
    .word 0x0014
