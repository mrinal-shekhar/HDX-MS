#Loading the .psf file
mol load psf system.psf
#Loading the trajectory file
mol addfile eq.1.dcd waitfor all step 1

#allign the protein#
set sel0 [atomselect 0 "protein"]
set sel1 [atomselect 0 "resname DOPE and name P"]

set nf [molinfo 0 get numframes]
set file [open "contact.dat" w] 
#open the file to write the data

#Looping through all the frames##
for {set j 0} {$j<=$nf} {incr j 1} {
	puts $j
	$sel0 frame $j
	$sel1 frame $j

	$sel0 update
	$sel1 update	
#Measuring the contact between the protein residues and the DOPE phosphorus atom#
	set con [measure contacts 3.0 $sel0 $sel1]
#Get the residue that forms any contact with protein atom
	set data [lindex $con 0]
        if {$data!={}} {
		set m [atomselect top "protein and index $data"]
		set res [lsort -u [lsort -dictionary [$m get resid]]]
		#puts $file "$i"
		puts $file "$res"
	}


}
close $file

puts done
quit

