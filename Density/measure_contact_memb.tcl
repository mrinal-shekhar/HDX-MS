#Loading the .psf file
mol load psf system.psf
#Loading the trajectory file
mol addfile traj.dcd waitfor all step 1

#allign the protein#
set sel [atomselect 0 "resname DOPE and name P and (z>0 or z<5)"]

set nf [molinfo 0 get numframes]
set filex [open "x.dat" w] 
set filey [open "y.dat" w]
#open the file to write the data

#Looping through all the frames##
for {set j 0} {$j<=$nf} {incr j 1} {

	puts $j
	$sel frame $j
	$sel update
	
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
quit

