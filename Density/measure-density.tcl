


#Loading the .psf file
mol load psf system.psf
#Loading the trajectory file
mol addfile traj.dcd waitfor all step 1

#allign the protein#
package require pbctools
set cell [pbc get -all]
set l [atomselect  top "protein and name CA" frame 0]
package require ilstools 
ILStools::shift_to_center $l
pbc wrap -all -sel "not protein" -compound resid -center com -centersel "protein and name CA"

set num_steps [molinfo 0 get numframes]
set sel1 [atomselect 0 "protein and name CA"]
set ref [atomselect 0 "protein and name CA" frame 0]
set all  [atomselect 0 "all"]
set sel [atomselect 0 "resname DOPE and name P and (z<0)"]

set nf [molinfo 0 get numframes]
set filex [open "x.dat" w] 
set filey [open "y.dat" w]
#open the file to write the data

#Looping through all the frames##
for {set j 0} {$j<=$nf} {incr j 1} {

	puts $j
	$sel frame $j
	$sel1 frame $j
	$all frame $j
	$sel update
	$sel1 update
	$all update

	set fit [measure fit $sel1 $ref]
	$all move $fit
	
#Measuring the contact between the protein residues and the DOPE phosphorus atom#
	set x [$sel get x]
	set y [$sel get y]
#Get the residue that forms any contact with protein atom

		puts -nonewline $filex "$x"
		puts -nonewline $filey "$y"
		
	}



close $filex
close $filey

puts done
#quit

